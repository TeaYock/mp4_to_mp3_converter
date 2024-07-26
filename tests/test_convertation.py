from pytest import fixture, raises, main, MonkeyPatch
from moviepy.editor import VideoFileClip, AudioFileClip
from pytube import YouTube
from io import BytesIO
from os import remove, path, makedirs
from shutil import rmtree, copy
from pathlib import Path
from yt_dlp import YoutubeDL
from typing import NewType
from app.mp4_to_mp3 import (creating_mp4_dir, creating_mp3_dir, remove_file_make_response_data,
    mp4_convertation_mp3, youtube_convertation_mp3, Mp3Path, VideoProcessingError, NoAudioTrackError)

# Preparing folders for tests
@fixture(scope='module')
def dirs_creation():
    creating_mp4_dir()
    creating_mp3_dir()
    yield
    rmtree('../mp4_files')
    rmtree('../mp3_files')

# Checking folder creation
def test_dir_creation(dirs_creation):
    assert path.exists('../mp4_files')
    assert path.exists('../mp3_files')

# Test converting mp4 (1 video track, 1 audio track) to mp3
def test_mp4_convertation_mp3(dirs_creation):
    mp4_file_path = '../mp4_files/video_standart.mp4'
    mp4_file_name = path.basename(mp4_file_path)
    mp4_clip = VideoFileClip('test_videos/video_standart.mp4')
    mp4_clip.write_videofile(mp4_file_path)

    mp3_path, mp3_filename = mp4_convertation_mp3(mp4_file_name)

    assert path.exists(mp3_path)
    assert mp3_path == '../mp3_files/video_standart.mp3'
    assert mp3_filename == 'video_standart.mp3'

# Test converting mp4 (1 video track, without audio track) to mp3
def test_mp4_convertation_mp3_no_audio(dirs_creation):
    mp4_file_path = '../mp4_files/video_no_audio.mp4'
    mp4_file_name = path.basename(mp4_file_path)
    mp4_clip = VideoFileClip('test_videos/video_no_audio.mp4')
    mp4_clip.write_videofile(mp4_file_path)

    with raises(NoAudioTrackError, match=f'The video file {mp4_file_name} does not contain an audio track'):
        mp4_convertation_mp3(mp4_file_name)

# Test converting crashed mp4
def test_mp4_convertation_mp3_crashed(dirs_creation):
    mp4_source_path = 'test_videos/video_crashed.mp4'
    mp4_file_path = '../mp4_files/video_crashed.mp4'
    copy(mp4_source_path, mp4_file_path)
    mp4_file_name = path.basename(mp4_file_path)

    with raises(VideoProcessingError, match=f'Error processing video file {mp4_file_name}'):
        mp4_convertation_mp3(mp4_file_name)

# Test converting mp4 (1 video track, 2 audio track) to mp3
def test_mp4_convertation_mp3_2_audio(dirs_creation):
    mp4_file_path = '../mp4_files/video_2_audio.mp4'
    mp4_file_name = path.basename(mp4_file_path)
    mp4_clip = VideoFileClip('test_videos/video_2_audio.mp4')
    mp4_clip.write_videofile(mp4_file_path)

    mp3_path, mp3_filename = mp4_convertation_mp3(mp4_file_name)

    assert path.exists(mp3_path)
    assert mp3_path == '../mp3_files/video_2_audio.mp3'
    assert mp3_filename == 'video_2_audio.mp3'

# Test converting mp4 (without video track, 1 audio track) to mp3
def test_mp4_convertation_mp3_no_videotrack(dirs_creation):
    mp4_file_path = '../mp4_files/video_no_videotrack.mp4'
    mp4_file_name = path.basename(mp4_file_path)
    mp4_clip = AudioFileClip('test_videos/video_no_videotrack.mp4')
    mp4_clip.write_audiofile(mp4_file_path, codec='aac')

    mp3_path, mp3_filename = mp4_convertation_mp3(mp4_file_name)

    assert path.exists(mp3_path)
    assert mp3_path == '../mp3_files/video_no_videotrack.mp3'
    assert mp3_filename == 'video_no_videotrack.mp3'

# Test YouTube convertation to mp3
def test_youtube_convertation_mp3(dirs_creation):
    test_url = 'https://www.youtube.com/watch?v=k80A5_9TClQ'
    mp3_file_path = youtube_convertation_mp3(test_url)
    assert path.exists(mp3_file_path)

# Test data removing with byte stream returning
def test_remove_file_make_response_data(dirs_creation):
    # Create a dummy mp3 file
    mp3_path = Path('../mp4_files/dummy.mp3')
    mp3_path.write_bytes(b'dummy mp3 data')

    mp3_byte_data = remove_file_make_response_data(str(mp3_path))

    assert mp3_byte_data.read() == b'dummy mp3 data'
    assert not mp3_path.exists()


