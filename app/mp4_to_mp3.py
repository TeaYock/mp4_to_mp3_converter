from moviepy.editor import VideoFileClip
from pytube import YouTube
import os
import yt_dlp

#Creating directories for mp4 files
def creating_mp4_dir():
    if not os.path.exists("mp4_files"):
        os.makedirs("mp4_files")

#Creating directories for mp3 files
def creating_mp3_dir():
    if not os.path.exists("mp3_files"):
        os.makedirs("mp3_files")

#deleting file
def remove_file(file_path: str) -> None:
    try:
        os.remove(file_path)
    except Exception as e:
        print(f'Error deleting file: {e}')

#test video
#test_path = "yt1s.com -  Devil May Cry 5  I AM THE STORM THAT IS APPROACHING BUT IN 4K_1080pFHR.mp4"

#Video to audio convertation function
def mp4_convertation_mp3(file_name: str, bitrate: str = '320k') -> str:
    video = VideoFileClip(f"../mp4_files/{file_name}")
    file_path_mp3 = f"../mp3_files/{file_name[:-len('.mp4')]}.mp3"
    video.audio.write_audiofile(file_path_mp3, bitrate=bitrate)
    video.close()
    return file_path_mp3

#test url
#DMC_url="https://www.youtube.com/watch?v=d-ggzGbsEWE"
#Rec_url = "https://www.youtube.com/watch?v=WfVejsi42eI"

#YouTube url to audio convertation function
def youtube_convertation_mp3(youtube_url: str) -> str:
    #youtube to mp3 convertation using pytube
    try:
        video = YouTube(youtube_url)
        audio_stream = video.streams.filter(only_audio=True).first()
        audio_file_path = audio_stream.download(filename=f"../mp3_files/{video.title}.mp3")
        return audio_file_path

    #youtube to mp3 convertation using yt_dlp
    except:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': "../mp3_files/%(title)s.%(ext)s",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            title = info_dict.get('title', None)

        file_path_mp3 = f"../mp3_files/{title}.mp3"

        return file_path_mp3

#Test useges
#mp4_convertation_mp3(test_path, "10k")
#youtube_convertation_mp3(DMC_url)
