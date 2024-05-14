import qrcode
import cv2

def generate_qr_code(data, file_name):
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
    
    # Save the image to a file
    qr_img.save(file_name)

def decode_qr_code(file_name):
    # Read the image
    img = cv2.imread(file_name)

    # Initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR Code
    data, _, _ = detector.detectAndDecode(img)
    
    return data

# Example usage
data_to_encode = "Hello, This is the QR Code! that you generated here is the link to find the code: https://github.com/ujwala16"
qr_file = "my_qr_code.png"

# Generate QR Code
generate_qr_code(data_to_encode, qr_file)
print(f"QR Code generated and saved as '{qr_file}'")

# Decode QR Code
decoded_data = decode_qr_code(qr_file)
print(f"Decoded data from QR Code: {decoded_data}")
