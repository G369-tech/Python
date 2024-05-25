import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

print("====== HariPrabodham ======")

# Getting user input for QR code data
user = input("Enter the data you want to make QR code for: ")

# Generating the QR code
myqr = qrcode.make(user)

# Saving the QR code as an image
myqr.save("hp.png")

# Decoding the QR code from the saved image
decoded_data = decode(Image.open("hp.png"))

# Printing the decoded data
print(decoded_data[0].data.decode("ascii"))