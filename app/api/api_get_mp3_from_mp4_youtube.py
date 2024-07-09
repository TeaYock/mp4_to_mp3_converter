from flask import Flask, request, send_file, after_this_request
from app.mp4_to_mp3 import m4_convertation_mp3, youtube_convertation_mp3, remove_file
import time
import os
app = Flask(__name__)


@app.route('/m4_convertation_mp3', methods=['POST'])
def m4_convertation_mp3_api():
    file_path="../mp3_files/[ Devil May Cry 5 ] I AM THE STORM THAT IS APPROACHING BUT IN 4K.mp3"
    return send_file(file_path, as_attachment=True)


#youtube url to mp3 convertation with download on client side
@app.route('/youtube_convertation_mp3', methods=['GET'])
def youtube_convertation_mp3_api():
    youtube_url = request.args.get('url', '')
    file_path=youtube_convertation_mp3(youtube_url)
#deleting mp3
    """
    @after_this_request
    def delete_mp3(response):
        time.sleep(30)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f'Error deleting file: {e}')
        return response
    """
    try:
        return send_file(file_path, as_attachment=True)
    finally:
        time.sleep(10)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f'Error deleting file: {e}')


if __name__ == '__main__':
    app.run(debug=True)