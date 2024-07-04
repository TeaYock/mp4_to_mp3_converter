from moviepy.editor import VideoFileClip
from pytube import YouTube
import os

#Creating directories for mp4 files
def crating_m4_dir():
    if not os.path.exists("mp4_files"):
        os.makedirs("mp4_files")

#Creating directories for mp3 files
def creating_mp3_dir():
    if not os.path.exists("mp3_files"):
        os.makedirs("mp3_files")

#test video
#test_path = "yt1s.com -  Devil May Cry 5  I AM THE STORM THAT IS APPROACHING BUT IN 4K_1080pFHR.mp4"

#Video to audio convertation function
def m4_convertation_mp3(file_name, bitrate):
    video = VideoFileClip(f"../mp4_files/{file_name}")
    file_path_mp3 = file_name[:-len(".mp4")]+".mp3"
    video.audio.write_audiofile(f"mp3_files/{file_path_mp3}", bitrate=bitrate)
    video.close()

#test url
#DMC_url="https://www.youtube.com/watch?v=d-ggzGbsEWE"

#YouTube url to audio convertation function
def youtube_convertation_mp3(youtube_url: str) -> str:
    video = YouTube(youtube_url)
    audio_stream = video.streams.filter(only_audio=True).first()
    audio_file_path = audio_stream.download(filename=f"../mp3_files/{video.title}.mp3")
    return audio_file_path


#Test useges
#m4_convertation_mp3(test_path, "10k")
#youtube_convertation_mp3(DMC_url)
