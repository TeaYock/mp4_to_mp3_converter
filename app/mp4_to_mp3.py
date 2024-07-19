from moviepy.editor import VideoFileClip
from pytube import YouTube
from io import BytesIO
from os import remove, path, makedirs
from yt_dlp import YoutubeDL

# Сreating directories for mp4 files
def creating_mp4_dir() -> None:
    if not path.exists("../mp4_files"):
        makedirs("../mp4_files")

# Creating directories for mp3 files
def creating_mp3_dir() -> None:
    if not path.exists("../mp3_files"):
        makedirs("../mp3_files")

# Deleting file and make return data in byte stream for response
# The file sent in the response cannot be deleted because it is being used to send to the client.
# Therefore, the file is loaded into a byte stream, which will be sent. After that, the file can be deleted.
def remove_file_make_response_data(mp3_path: str, mp4_path: str = None) -> BytesIO:
    mp3_byte_data = BytesIO()
    with open(mp3_path, 'rb') as mp3_file:
        mp3_byte_data.write(mp3_file.read())
    mp3_byte_data.seek(0)
    remove(mp3_path)
    if mp4_path:
        remove(mp4_path)
    return mp3_byte_data


# Video to audio convertation function
def mp4_convertation_mp3(mp4_file_name: str, bitrate: str = '320k') -> [str, str]:
    video = VideoFileClip(f"../mp4_files/{mp4_file_name}")
    mp3_file_path = f"../mp3_files/{mp4_file_name[:-len('.mp4')]}.mp3"
    mp3_filename = f"{mp4_file_name[:-len('.mp4')]}.mp3"
    if video.audio is None:
        video.close()
        raise ValueError("The video file does not contain an audio track")
    video.audio.write_audiofile(mp3_file_path, bitrate=bitrate)
    video.close()
    return mp3_file_path, mp3_filename

# YouTube url to audio convertation function
def youtube_convertation_mp3(youtube_url: str) -> str:
    #  YouTube to mp3 convertation using pytube
    try:
        video = YouTube(youtube_url)
        audio_stream = video.streams.filter(only_audio=True).first()
        mp3_file_path = audio_stream.download(filename=f"../mp3_files/{video.title}.mp3")
        return mp3_file_path

    #  YouTube to mp3 convertation using yt_dlp
    except:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': "../mp3_files/%(title)s.%(ext)s",
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            mp3_file_name = info_dict.get('title', None)

        mp3_file_path = f"../mp3_files/{mp3_file_name}.mp3"
        return mp3_file_path