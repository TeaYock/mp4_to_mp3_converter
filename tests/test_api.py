from os import path, remove
from shutil import rmtree
from tempfile import NamedTemporaryFile
from pytest import fixture
from app.api.api_get_mp3_from_mp4_youtube import app
from app.mp4_to_mp3 import creating_mp4_dir, creating_mp3_dir

# Test client creation, set location of html files
@fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    app.template_folder = path.join(path.dirname(path.abspath(__file__)), '../app/website')
    creating_mp4_dir()
    creating_mp3_dir()
    yield client
    rmtree('../mp4_files')
    rmtree('../mp3_files')


# Test the homepage
def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Upload your MP4 file to convert to MP3' in response.data
    assert b'<form action="http://localhost:5000/mp4_convertation_mp3"' in response.data


# Test the MP4 to MP3 convertation API
def test_mp4_convertation_mp3_api(client):
    mp4_file_path = 'test_videos/video_standart.mp4'
    expected_mp3_filename = f'{path.basename(mp4_file_path)[:-len('.mp4')]}.mp3'

    # Uploading file to API
    with open(mp4_file_path, 'rb') as mp4_file:
        data = {
            'mp4_file': (mp4_file, 'video_standart.mp4')
        }
        response = client.post('/mp4_convertation_mp3', content_type='multipart/form-data', data=data)

    # Checking the success of the response and the content type
    assert response.status_code == 200
    assert response.mimetype == 'audio/mpeg'

    # Checking file name in Content-Disposition header
    content_disposition = response.headers.get('Content-Disposition')
    assert expected_mp3_filename in content_disposition

    # Save byte data to a temporary file
    mp3_data = response.data
    with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_mp3:
        temp_mp3.write(mp3_data)
        temp_mp3_path = temp_mp3.name

    # Check temporary file type and remove it
    assert temp_mp3_path.endswith('.mp3')
    remove(temp_mp3_path)


# Test the YouTube to MP3 convertation API with a real YouTube URL
def test_youtube_convertation_mp3_api(client):
    youtube_url = 'https://www.youtube.com/watch?v=k80A5_9TClQ'
    expected_mp3_filename = 'Hunt Skeleton Meme.mp3'
    response = client.get('/youtube_convertation_mp3', query_string={'url': youtube_url})

    # Checking the success of the response and the content type
    assert response.status_code == 200
    assert response.mimetype == 'audio/mpeg'

    # Checking file name in Content-Disposition header
    content_disposition = response.headers.get('Content-Disposition')
    assert expected_mp3_filename in content_disposition

    # Save byte data to a temporary file
    mp3_data = response.data
    with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_mp3:
        temp_mp3.write(mp3_data)
        temp_mp3_path = temp_mp3.name

    # Check temporary file type and remove it
    assert temp_mp3_path.endswith('.mp3')
    remove(temp_mp3_path)