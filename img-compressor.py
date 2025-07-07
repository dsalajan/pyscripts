from PIL import Image
import os

# Define input and output paths
input_dir = r"C:\Users\David\Downloads\WhatsApp Unknown 2025-06-20 at 10.00.07"
output_dir = os.path.join(input_dir, "compressed_pdfs")
output_pdf = os.path.join(output_dir, "all_images_compressed.pdf")

# Create output directory if needed
os.makedirs(output_dir, exist_ok=True)

# Allowed image extensions
image_extensions = ('.jpg', '.jpeg', '.png')

# Resize factor (adjust for more or less compression)
resize_factor = 0.8
# Store processed images for PDF
pdf_images = []

# Go through each image in the folder
for filename in sorted(os.listdir(input_dir)):
    if filename.lower().endswith(image_extensions):
        try:
            path = os.path.join(input_dir, filename)
            img = Image.open(path)

            # Convert to RGB
            if img.mode != "RGB":
                img = img.convert("RGB")

            # Resize for compression
            new_size = (int(img.width * resize_factor), int(img.height * resize_factor))
            img = img.resize(new_size, Image.LANCZOS)

            # Append to list
            pdf_images.append(img)

            print(f"Added: {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Save all images to one PDF
if pdf_images:
    pdf_images[0].save(
        output_pdf,
        save_all=True,
        append_images=pdf_images[1:],
        format="PDF",
        optimize=True
    )
    size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"\n✅ All images saved to one PDF: {output_pdf} ({size_mb:.2f} MB)")
else:
    print("❌ No valid images found.")
