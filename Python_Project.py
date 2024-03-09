# This line imports the qrcode library, which provides functions to generate QR codes.
import qrcode
# This line defines a function called generate_qr_code that takes two parameters - message and file_name.
def generate_qr_code(message, file_name='invitation_qr_code.png'):
    # Create QR code instance
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    # Add data to the QR code
    qr.add_data(message)
    qr.make(fit=True)
    # Create an image from the QR code data
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image to a file
    img.save(file_name)
# This line prints a message indicating that the QR code has been successfully generated and saved.
    print(f"QR code generated and saved as {file_name}")
    
invitation_message = "Hello, You're invited to my party! Scan the QR code for details."
file_name = 'invitation_qr_code.png'
# Generate QR code with the invitation message
generate_qr_code(invitation_message, file_name)

# Abdulwahab Uthman Muhammad
