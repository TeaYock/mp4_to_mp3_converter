from moviepy.editor import VideoFileClip
import os

#Creating directories for mp4 files
if not os.path.exists("mp4_files"):
    os.makedirs("mp4_files")

#Creating directories for mp3 files
if not os.path.exists("mp3_files"):
    os.makedirs("mp3_files")

test_path = "yt1s.com -  Devil May Cry 5  I AM THE STORM THAT IS APPROACHING BUT IN 4K_1080pFHR.mp4"
#Video to audio convertation function
def m4_convertation_mp3(file_name, bitrate):
    video = VideoFileClip(f"mp4_files/{file_name}")
    file_path_mp3 = file_name[:-len(".mp4")]+".mp3"
    video.audio.write_audiofile(f"mp3_files/{file_path_mp3}", bitrate=bitrate)
    video.close()

m4_convertation_mp3(test_path, "10k")
