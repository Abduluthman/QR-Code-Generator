# This line imports the qrcode library, which provides functions to generate QR codes.
import qrcode
# This line defines a function called generate_qr_code that takes two parameters - message and file_name.
def generate_qr_code(message, file_name='invitation_qr_code.png'):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1, #The version of the QR code (1 in this case).
        error_correction=qrcode.constants.ERROR_CORRECT_L, # The error correction level
        box_size=10, #The size of each box (pixel) in the QR code.
        border=4, #The number of boxes (pixels) that form the border of the QR code.
    )

    # Add data to the QR code
    qr.add_data(message)
# Using Make to generate the QR code based on the provided data. 
# The fit=True argument ensures that the QR code adjusts its size to fit the data.    
    qr.make(fit=True)

    # Create an image from the QR code data
# This line creates an image (img) from the QR code data using the make_image method.
# The fill_color parameter sets the color of the QR code, and back_color sets the background color.
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
# The generated QR code image is saved to a file with the specified file_name.
    img.save(file_name)
# This line prints a message indicating that the QR code has been successfully generated and saved.
    print(f"QR code generated and saved as {file_name}")

invitation_message = "Hello, You're invited to my party! Scan the QR code for details."

# Customize the file name if needed
file_name = 'invitation_qr_code.png'

# Generate QR code with the invitation message
generate_qr_code(invitation_message, file_name)


# Abdulwahab Uthman Muhammad