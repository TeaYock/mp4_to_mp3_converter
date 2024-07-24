from pytest import fixture, main, MonkeyPatch
from moviepy.editor import VideoFileClip
from pytube import YouTube
from io import BytesIO
from os import remove, path, makedirs
from shutil import rmtree
from yt_dlp import YoutubeDL
from typing import NewType
from app.mp4_to_mp3 import (creating_mp4_dir, creating_mp3_dir, remove_file_make_response_data,
    mp4_convertation_mp3, youtube_convertation_mp3, Mp3Path)

@fixture(scope='module')
def setup_dirs():
    creating_mp4_dir()
    creating_mp3_dir()
    yield
    rmtree('../mp4_files')
    rmtree('../mp3_files')

def test_creating_mp4_dir(setup_dirs):
    assert path.exists('../mp4_files')

def test_creating_mp3_dir(setup_dirs):
    assert path.exists('../mp3_files')

def test_remove_file_make_response_data(tmp_path):
    # Create a dummy mp3 file
    mp3_path = tmp_path / 'test.mp3'
    mp3_path.write_bytes(b'dummy mp3 data')

    mp3_byte_data = remove_file_make_response_data(str(mp3_path))

    assert mp3_byte_data.read() == b'dummy mp3 data'
    assert not mp3_path.exists()

def test_mp4_convertation_mp3(setup_dirs, tmp_path):
    mp4_file_path = tmp_path / '../mp4_files/video_standart.mp4'
    mp4_clip = VideoFileClip('test_videos/video_standart.mp4.mp4')
    mp4_clip.write_videofile(str(mp4_file_path))

    mp3_path, mp3_filename = mp4_convertation_mp3(str(mp4_file_path.name))

    assert path.exists(mp3_path)
    assert mp3_path == '../mp4_files/video_standart.mp3'
    assert mp3_filename == 'video_standart.mp3'
'''
def test_mp4_convertation_mp3_no_audio(setup_dirs, tmp_path):
    mp4_file_path = tmp_path / 'test_videos/video_no_audio.mp4'
    mp4_clip = VideoFileClip('../mp4_files')
    mp4_clip.write_videofile(str(mp4_file_path))

    mp3_path, mp3_filename = mp4_convertation_mp3(str(mp4_file_path.name))

    assert path.exists(mp3_path)
    assert mp3_filename == '../mp3_files'

def test_mp4_convertation_mp3_2_audio(setup_dirs, tmp_path):
    mp4_file_path = tmp_path / 'test_videos/video_2_audio.mp4'
    mp4_clip = VideoFileClip('../mp4_files')
    mp4_clip.write_videofile(str(mp4_file_path))

    mp3_path, mp3_filename = mp4_convertation_mp3(str(mp4_file_path.name))

    assert path.exists(mp3_path)
    assert mp3_filename == '../mp3_files'

def test_mp4_convertation_mp3_no_videotrack(setup_dirs, tmp_path):
    mp4_file_path = tmp_path / 'test_videos/video_no_videotrack.mp4'
    mp4_clip = VideoFileClip('../mp4_files')
    mp4_clip.write_videofile(str(mp4_file_path))

    mp3_path, mp3_filename = mp4_convertation_mp3(str(mp4_file_path.name))

    assert path.exists(mp3_path)
    assert mp3_filename == '../mp3_files'
'''

