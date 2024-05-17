import streamlit as st
import qrcode
from PIL import Image
import cv2
import numpy as np
import io

def generate_qr_code(data):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

def decode_qr_code(image):
    # Convert PIL image to OpenCV format
    img = np.array(image.convert('RGB'))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR Code
    data, _, _ = detector.detectAndDecode(img)
    return data

# Streamlit App
st.title("QR Code Generator and Decoder")

# Sidebar for navigation
option = st.sidebar.selectbox("Select an option", ("Generate QR Code", "Decode QR Code"))

if option == "Generate QR Code":
    st.header("Generate QR Code")
    input_data = st.text_area("Enter data to encode in QR code")
    if st.button("Generate QR Code"):
        if input_data:
            qr_img = generate_qr_code(input_data)
            # Convert PIL image to bytes
            img_byte_arr = io.BytesIO()
            qr_img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            st.image(img_byte_arr, caption='Generated QR Code')
            with open('generated_qr_code.png', 'wb') as f:
                f.write(img_byte_arr)
            st.success(f"QR Code generated and saved as 'generated_qr_code.png'")
        else:
            st.error("Please enter data to encode in the QR code")

elif option == "Decode QR Code":
    st.header("Decode QR Code")
    uploaded_file = st.file_uploader("Upload a QR code image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded QR Code')
        decoded_data = decode_qr_code(image)
        if decoded_data:
            st.success(f"Decoded data: {decoded_data}")
        else:
            st.error("Failed to decode the QR code")
