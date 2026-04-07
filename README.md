# 📸 Photo Editor using OpenCV & Streamlit

A simple yet powerful **interactive photo editing web application** built using **OpenCV** and **Streamlit**.
This app allows users to upload images and apply multiple image processing effects in real-time with an intuitive UI.

---

## 🚀 Features

### 🔹 Core Features

* 📤 Upload an image (JPG, PNG, JPEG)
* 📏 Resize image (width & height control)
* 🌞 Adjust brightness
* 🎚 Adjust contrast
* ⚫ Convert to grayscale
* 🌫 Apply blur effect
* 🔥 Apply warm filter
* ✨ Apply sharpen effect
* 🧑‍🎨 Portrait-style background blur
* 🔄 Rotate image
* 📥 Download edited image

---

### 🔹 Advanced Features

* 🧠 Edge Detection (Canny)
* ✏ Sketch Effect
* 🎨 Cartoon Effect

---

### 🔹 Interactive Features

* 👁 **Compare Mode**
  Toggle between original and edited image

* 🔘 **Toggle-Based Effects System**

  * Click once → Apply effect
  * Click again → Remove effect
  * Multiple effects can be stacked

---

## 🏗 Project Structure

```
photo-editor/
│
├── app.py              # Streamlit UI
├── image_utils.py      # OpenCV processing functions
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/photo-editor.git
cd photo-editor
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

### 🔹 Image Processing Pipeline

* The original image is stored in session state
* All effects are applied dynamically using a centralized **effects dictionary**
* Each effect is applied sequentially using OpenCV functions

### 🔹 State Management

* Uses `st.session_state` to:

  * Store original image
  * Store active effects
  * Handle compare mode

### 🔹 Toggle System

* Effects are controlled via boolean flags
* Enables:

  * Adding/removing effects independently
  * Clean and scalable design

---

## 🛠 Technologies Used

* **Python**
* **OpenCV** → Image processing
* **Streamlit** → Web UI
* **NumPy** → Image matrix operations
* **Pillow (PIL)** → Image loading

---

## 📸 Application Flow

```
Upload Image
     ↓
Resize Image
     ↓
Adjust Brightness & Contrast
     ↓
Apply Filters & Effects
     ↓
View Edited Image
     ↓
Compare with Original
     ↓
Download Image
```

---

## 🔥 Key Learning Outcomes

* Understanding of **OpenCV image processing techniques**
* Building **interactive web apps using Streamlit**
* Managing **application state using session_state**
* Designing a **modular and scalable architecture**
* Implementing **real-time image transformation pipelines**

---

## 🚀 Future Improvements

* 🎯 Face detection-based portrait blur (Haar Cascade / DNN)
* 🧠 Background removal using AI (rembg)
* 🎨 Preset filters (Instagram-style)
* 🔁 Undo / Redo functionality
* 🧩 Side-by-side comparison slider
* ☁ Deployment on Streamlit Cloud

---

## 💡 Interview Explanation

> This project demonstrates my ability to integrate computer vision with interactive web applications.
> I designed a modular pipeline where all transformations are controlled via a centralized state dictionary, enabling dynamic effect toggling and real-time updates.
> I also handled Streamlit’s stateless nature using session state to maintain user interactions like compare mode and effect persistence.

---

## 🙌 Acknowledgements

* OpenCV documentation
* Streamlit official docs

---

## 📌 Author

**Your Name**
🔗 LinkedIn: https://linkedin.com/in/your-profile
💻 GitHub: https://github.com/your-username

---
