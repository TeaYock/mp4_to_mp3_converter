from pytest import fixture, raises, main, MonkeyPatch
from moviepy.editor import VideoFileClip, AudioFileClip
from pytube import YouTube
from io import BytesIO
from os import remove, path, makedirs
from shutil import rmtree
from pathlib import Path
from yt_dlp import YoutubeDL
from typing import NewType
from app.mp4_to_mp3 import (creating_mp4_dir, creating_mp3_dir, remove_file_make_response_data,
    mp4_convertation_mp3, youtube_convertation_mp3, Mp3Path)

@fixture(scope='module')
def dirs_creation():
    creating_mp4_dir()
    creating_mp3_dir()
    yield
    rmtree('../mp4_files')
    rmtree('../mp3_files')

def test_dir_creation(dirs_creation):
    assert path.exists('../mp4_files')
    assert path.exists('../mp3_files')

def test_mp4_convertation_mp3(dirs_creation):
    mp4_file_path = '../mp4_files/video_standart.mp4'
    mp4_clip = VideoFileClip('test_videos/video_standart.mp4')
    mp4_clip.write_videofile(mp4_file_path)

    mp3_path, mp3_filename = mp4_convertation_mp3(path.basename(mp4_file_path))

    assert path.exists(mp3_path)
    assert mp3_path == '../mp3_files/video_standart.mp3'
    assert mp3_filename == 'video_standart.mp3'

def test_mp4_convertation_mp3_no_audio(dirs_creation):
    mp4_file_path = '../mp4_files/video_no_audio.mp4'
    mp4_clip = VideoFileClip('test_videos/video_no_audio.mp4')
    mp4_clip.write_videofile(mp4_file_path)

    with raises(ValueError, match="The video file does not contain an audio track"):
        mp4_convertation_mp3(mp4_file_path)

def test_mp4_convertation_mp3_2_audio(dirs_creation):
    mp4_file_path = '../mp4_files/video_2_audio.mp4'
    mp4_clip = VideoFileClip('test_videos/video_2_audio.mp4')
    mp4_clip.write_videofile(mp4_file_path)

    mp3_path, mp3_filename = mp4_convertation_mp3(path.basename(mp4_file_path))

    assert path.exists(mp3_path)
    assert mp3_path == '../mp3_files/video_2_audio.mp3'
    assert mp3_filename == 'video_2_audio.mp3'

def test_mp4_convertation_mp3_no_videotrack(dirs_creation):
    mp4_file_path = '../mp4_files/video_no_videotrack.mp4'
    mp4_clip = AudioFileClip('test_videos/video_no_videotrack.mp4')
    mp4_clip.write_audiofile(mp4_file_path, codec='aac')

    mp3_path, mp3_filename = mp4_convertation_mp3(path.basename(mp4_file_path))

    assert path.exists(mp3_path)
    assert mp3_path == '../mp3_files/video_no_videotrack.mp3'
    assert mp3_filename == 'video_no_videotrack.mp3'

def test_remove_file_make_response_data(dirs_creation):
    # Create a dummy mp3 file
    mp3_path = Path('../mp4_files/dummy.mp3')
    mp3_path.write_bytes(b'dummy mp3 data')

    mp3_byte_data = remove_file_make_response_data(str(mp3_path))

    assert mp3_byte_data.read() == b'dummy mp3 data'
    assert not mp3_path.exists()


