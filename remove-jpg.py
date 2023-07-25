import os

def remove_jpg_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Removed: {file_path}")

# Specify the directory where the .jpg images should be removed
directory_path = "E:\wetransfer_4-rar_2023-05-12_0741\shp"

remove_jpg_images(directory_path)