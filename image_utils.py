import cv2
import numpy as np


# Function to resize an image to the specified width and height
def resize_image(image, width, height):
    return cv2.resize(image, (width, height))


# Brightenss adjustment 
def adjust_brightness(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)

    # Convert to int to avoid overflow
    v = v.astype(np.int16)

    v = v + value
    v = np.clip(v, 0, 255)

    # Convert back to uint8 (VERY IMPORTANT)
    v = v.astype(np.uint8)

    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)  #We use HSV color space → safer brightness control.


# Contrast adjustment
def adjust_contrast(image, alpha):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)
# alpha > 1 → increases contrast
# alpha < 1 → decreases contrast


# Function to apply gray scale filter to an image
def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Function to apply a blur filter to an image
def apply_blur(image, ksize):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)

# Function to apply a warm filter to an image
def apply_warm_filter(image):
    increase = np.array([0, 10, 20], dtype=np.uint8)
    return cv2.add(image, increase)

# Function to apply sharpen filter to an image
def sharpen_image(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)


# potrait background blur
def portrait_blur(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mask = cv2.GaussianBlur(gray, (21, 21), 0)

    blurred = cv2.GaussianBlur(image, (25, 25), 0)

    # Simple blending
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    result = np.where(mask > 127, image, blurred)

    return result

# Edge detection using canny
def edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, 100, 200)

# Sketch effect
def sketch_effect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

# cartoon effect
def cartoon_effect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9
    )

    color = cv2.bilateralFilter(image, 9, 300, 300)

    return cv2.bitwise_and(color, color, mask=edges)

# rotate image
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

# Function to apply multiple effects based on a dictionary of effects
def apply_effects(image, effects):
    result = image.copy()

    if effects.get("brightness"):
        result = adjust_brightness(result, effects["brightness"])

    if effects.get("contrast"):
        result = adjust_contrast(result, effects["contrast"])

    if effects.get("grayscale"):
        result = to_grayscale(result)

    if effects.get("blur"):
        result = apply_blur(result, 7)

    if effects.get("warm"):
        result = apply_warm_filter(result)

    if effects.get("sharpen"):
        result = sharpen_image(result)

    if effects.get("portrait"):
        result = portrait_blur(result)

    # Extra
    if effects.get("edge"):
        result = edge_detection(result)

    if effects.get("sketch"):
        result = sketch_effect(result)

    if effects.get("cartoon"):
        result = cartoon_effect(result)

    return result