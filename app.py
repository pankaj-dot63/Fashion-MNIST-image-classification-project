import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("cnn_model.keras")

# Fashion-MNIST classes
class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot"
]

st.title("👕 Fashion-MNIST CNN Classifier")
st.write("Upload an image and let the CNN predict the clothing category.")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        width=250
    )

    if st.button("🔍 Predict"):

        # Convert to grayscale
        image = image.convert("L")

        # Resize
        image = image.resize((28, 28))

        # Convert to numpy
        image = np.array(image)

        # Normalize
        image = image / 255.0

        # Reshape
        image = image.reshape(1, 28, 28, 1)

        # Prediction
        prediction = model.predict(image)

        predicted_index = np.argmax(prediction[0])

        predicted_class = class_names[predicted_index]

        confidence = prediction[0][predicted_index] * 100

        st.success(f"Prediction: {predicted_class}")

        st.info(f"Confidence: {confidence:.2f}%")