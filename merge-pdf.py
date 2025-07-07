import os
from PIL import Image
from pdf2docx import Converter

def convert_images_to_pdf(source_folder, output_pdf):
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    image_files = [
        os.path.join(source_folder, file)
        for file in sorted(os.listdir(source_folder))
        if file.lower().endswith(image_extensions)
    ]

    if not image_files:
        print("No image files found in the folder.")
        return None

    images = [Image.open(img).convert('RGB') for img in image_files]
    first_image = images[0]
    other_images = images[1:]

    output_path = os.path.join(source_folder, output_pdf)
    first_image.save(output_path, save_all=True, append_images=other_images)
    print(f"PDF saved successfully as: {output_path}")
    return output_path

def convert_pdf_to_word(pdf_file, output_docx):
    if not os.path.exists(pdf_file):
        print(f"PDF file not found: {pdf_file}")
        return

    cv = Converter(pdf_file)
    cv.convert(output_docx, start=0, end=None)
    cv.close()
    print(f"Word file saved successfully as: {output_docx}")

# Example usage
if __name__ == "__main__":
    folder_path = "C:/Users/David/Downloads/seminarii mecanica"  # Replace with your folder path
    pdf_filename = "merged_images.pdf"
    word_filename = "converted_output.docx"

    pdf_path = convert_images_to_pdf(folder_path, pdf_filename)
    if pdf_path:
        convert_pdf_to_word(pdf_path, os.path.join(folder_path, word_filename))
