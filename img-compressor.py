from PIL import Image
import os

# set the desired size of the compressed image in bytes
target_size = 15 * 1024 * 1024  # 64 MB

path = "C:/Users/David/Desktop/Harta-CNIS.png"
# load the PNG image
img = Image.open(path)

# get the current size of the image
current_size = os.path.getsize(path)

# calculate the compression ratio required to achieve the target size
compression_ratio = (target_size / current_size) ** 0.5

# resize the image using the compression ratio
new_size = (int(img.size[0] * compression_ratio), int(img.size[1] * compression_ratio))
img = img.resize(new_size, Image.LANCZOS)

# save the compressed image as a PNG file
img.save("C:/Users/David/Desktop/output_image.png", format="PNG")

# print the new size of the compressed image
print(f"Compressed image size: {os.path.getsize('C:/Users/David/Desktop/output_image.png') / (1024 * 1024)} MB")
