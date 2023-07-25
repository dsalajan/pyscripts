from PIL import Image
import os
import hashlib

def convert_and_remove_duplicates(input_dir, output_dir):
    i = 0
    # Create the output director
    #  if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Dictionary to store hash values of images
    hash_dict = {}

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is an image
        if filename.endswith(('.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image
            image_path = os.path.join(input_dir, filename)
            img = Image.open(image_path)

            # Convert to PNG format
            if img.format != 'PNG':
                new_filename = os.path.splitext(filename)[0] + '.png'
                output_path = os.path.join(output_dir, new_filename)
                img.save(output_path, 'PNG')

            # Calculate the hash value of the image
            with open(image_path, 'rb') as f:
                image_hash = hashlib.md5(f.read()).hexdigest()

            # Check if the image is a duplicate
            if image_hash in hash_dict:
                # Remove duplicate image
                os.remove(image_path)
            else:
                # Save the image
                output_path = os.path.join(output_dir, filename)
                img.save(output_path)

                # Store the hash value of the image
                hash_dict[image_hash] = output_path

            # Close the image
            img.close()

        i = i + 1
        print(f"done image {filename} Total done: {i}")

# Example usage:
input_directory = 'E:\wetransfer_4-rar_2023-05-12_0741\shp'
output_directory = 'E:\wetransfer_4-rar_2023-05-12_0741\shp'

convert_and_remove_duplicates(input_directory, output_directory)
