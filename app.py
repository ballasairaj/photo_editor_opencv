# importing necessary libraries
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import image_utils as iu

# -------------------------------
# Page setup
# -------------------------------
st.title("📸 Photo Editor using OpenCV")
st.write("Upload and edit your image interactively")

# -------------------------------
# Session State Initialization
# -------------------------------
if "original_image" not in st.session_state:
    st.session_state.original_image = None

if "effects" not in st.session_state:
    st.session_state.effects = {
        "brightness": 0,
        "contrast": 1.0,
        "grayscale": False,
        "blur": False,
        "warm": False,
        "sharpen": False,
        "portrait": False,
        "edge": False,
        "sketch": False,
        "cartoon": False,
        "rotate": 0
    }

if "compare" not in st.session_state:
    st.session_state.compare = False

# -------------------------------
# Helper: Toggle Effect
# -------------------------------
def toggle_effect(effect_name):
    st.session_state.effects[effect_name] = not st.session_state.effects[effect_name]

# -------------------------------
# Upload Image
# -------------------------------
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    st.session_state.original_image = image

# Proceed only if image exists
if st.session_state.original_image is not None:

    image = st.session_state.original_image.copy()

    # -------------------------------
    # Resize
    # -------------------------------
    st.sidebar.header("Resize")
    width = st.sidebar.slider("Width", 100, 1000, image.shape[1])
    height = st.sidebar.slider("Height", 100, 1000, image.shape[0])

    image = iu.resize_image(image, width, height)

    # -------------------------------
    # Adjustments
    # -------------------------------
    st.sidebar.header("Adjustments")

    st.session_state.effects["brightness"] = st.sidebar.slider(
        "Brightness", -50, 50, st.session_state.effects["brightness"]
    )

    st.session_state.effects["contrast"] = st.sidebar.slider(
        "Contrast", 0.5, 3.0, st.session_state.effects["contrast"]
    )

    # -------------------------------
    # Feature Toggles
    # -------------------------------
    st.sidebar.header("Filters")

    if st.sidebar.button("Grayscale"):
        toggle_effect("grayscale")

    if st.sidebar.button("Blur"):
        toggle_effect("blur")

    if st.sidebar.button("Warm Filter"):
        toggle_effect("warm")

    if st.sidebar.button("Sharpen"):
        toggle_effect("sharpen")

    if st.sidebar.button("Portrait Blur"):
        toggle_effect("portrait")

    # -------------------------------
    # Extra Features
    # -------------------------------
    st.sidebar.header("Extra Features")

    if st.sidebar.button("Edge Detection"):
        toggle_effect("edge")

    if st.sidebar.button("Sketch"):
        toggle_effect("sketch")

    if st.sidebar.button("Cartoon"):
        toggle_effect("cartoon")

    st.session_state.effects["rotate"] = st.sidebar.slider(
        "Rotate", 0, 360, st.session_state.effects["rotate"]
    )

    # -------------------------------
    # Apply Effects Pipeline
    # -------------------------------
    edited = image.copy()

    edited = iu.adjust_brightness(edited, st.session_state.effects["brightness"])
    edited = iu.adjust_contrast(edited, st.session_state.effects["contrast"])

    if st.session_state.effects["grayscale"]:
        edited = iu.to_grayscale(edited)

    if st.session_state.effects["blur"]:
        edited = iu.apply_blur(edited, 7)

    if st.session_state.effects["warm"]:
        edited = iu.apply_warm_filter(edited)

    if st.session_state.effects["sharpen"]:
        edited = iu.sharpen_image(edited)

    if st.session_state.effects["portrait"]:
        edited = iu.portrait_blur(edited)

    if st.session_state.effects["edge"]:
        edited = iu.edge_detection(edited)

    if st.session_state.effects["sketch"]:
        edited = iu.sketch_effect(edited)

    if st.session_state.effects["cartoon"]:
        edited = iu.cartoon_effect(edited)

    if st.session_state.effects["rotate"] != 0:
        edited = iu.rotate_image(edited, st.session_state.effects["rotate"])

    # -------------------------------
    # Compare Button
    # -------------------------------
    if st.button("👁 Compare (Click to View Original)"):
        st.session_state.compare = not st.session_state.compare

    # -------------------------------
    # Display Logic
    # -------------------------------
    st.subheader("Output Image")

    if st.session_state.compare:
        display = image  # original resized image
    else:
        display = edited

    if len(display.shape) == 2:
        st.image(display, channels="GRAY")
    else:
        st.image(cv2.cvtColor(display, cv2.COLOR_BGR2RGB))

    # -------------------------------
    # Download Button
    # -------------------------------
    _, buffer = cv2.imencode('.png', edited)

    st.download_button(
        label="Download Image",
        data=buffer.tobytes(),
        file_name="edited_image.png",
        mime="image/png"
    )