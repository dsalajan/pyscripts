import qrcode
from PIL import Image, ImageDraw

# Define the website and logo file paths
website_url = ""
square_size = 0

# Generate the QR code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=4,
    border=4,
)
qr.add_data(website_url)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white")

# Draw a white square in the center of the QR code image
draw = ImageDraw.Draw(qr_img)
qr_size = qr_img.size[0]
# square_x = int((qr_size - square_size*3) / 2)
# square_y = int((qr_size - square_size*3) / 2)
# draw.rectangle((square_x, square_y, square_x + square_size*3, square_y + square_size*3), fill="white")

# Save the QR code image
qr_img = qr_img.resize((qr_size*4, qr_size*4), resample=Image.LANCZOS)

# Save the final QR code image
qr_img.save("C:/Users/David/Desktop/qr_code_f_csm.png")