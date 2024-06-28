from moviepy.editor import VideoFileClip
import os

#Creating directories for mp4 files
if not os.path.exists("mp4_files"):
    os.makedirs("mp4_files")

#Creating directories for mp3 files
if not os.path.exists("mp3_files"):
    os.makedirs("mp3_files")

#Video to audio convertation
video = VideoFileClip("mp4_files/yt1s.com -  Devil May Cry 5  I AM THE STORM THAT IS APPROACHING BUT IN 4K_1080pFHR.mp4")
video.audio.write_audiofile("mp3_files/BuryTheLight.mp3")
video.close()
