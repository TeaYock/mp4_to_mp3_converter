from os import path, remove
from tempfile import NamedTemporaryFile
import io
from pytest import fixture, main
from app.api.api_get_mp3_from_mp4_youtube import app

# Test client creation, set location of html files
@fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    app.template_folder = path.join(path.dirname(path.abspath(__file__)), '../app/website')
    yield client

# Test the homepage
def test_index_page(client):
    response = client.get('/')

    # Проверка статуса ответа
    assert response.status_code == 200

    # Проверка, что возвращаемый HTML содержит ожидаемые элементы
    assert b'Upload your MP4 file to convert to MP3' in response.data
    assert b'<form action="http://localhost:5000/mp4_convertation_mp3"' in response.data

# Test the MP4 to MP3 convertation API
def test_mp4_convertation_mp3_api(client):
    mp4_file_path = 'test_videos/video_standart.mp4'
    expected_mp3_filename = f'{path.basename(mp4_file_path)[:-len('.mp4')]}.mp3'

    with open(mp4_file_path, 'rb') as mp4_file:
        data = {
            'mp4_file': (mp4_file, 'video_standart.mp4')
        }
        response = client.post('/mp4_convertation_mp3', content_type='multipart/form-data', data=data)

    assert response.status_code == 200
    assert response.mimetype == 'audio/mpeg'

    content_disposition = response.headers.get('Content-Disposition')
    assert expected_mp3_filename in content_disposition

    mp3_data = response.data
    with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_mp3:
        temp_mp3.write(mp3_data)
        temp_mp3_path = temp_mp3.name

    assert temp_mp3_path.endswith('.mp3')
    remove(temp_mp3_path)





if __name__ == '__main__':
    main()