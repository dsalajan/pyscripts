from moviepy.editor import *

def convert_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(mp3_file)

# Provide the file paths for the input MP4 and output MP3 files
input_file = "C:/Users/David/Desktop/speaking/4.mp4"
output_file = "C:/Users/David/Desktop/speaking/4.mp3"

# Call the function to convert MP4 to MP3
convert_to_mp3(input_file, output_file)