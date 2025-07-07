import os
import time

# Directory where iCloud Photos syncs your photos
photos_directory = r"E:/iphone_photos"

# Monitor the directory for new files
while True:
    new_files = [f for f in os.listdir(photos_directory) if f.endswith(".jpg")]

    if new_files:
        # Perform your desired action here (e.g., move files, upload to a web service)
        for filename in new_files:
            full_path = os.path.join(photos_directory, filename)
            # Perform your action, e.g., move the file or upload it

    time.sleep(300)  # Check every 5 minutes
