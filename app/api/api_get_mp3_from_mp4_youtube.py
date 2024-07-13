from flask import Flask, request, send_file, after_this_request, redirect, render_template, Response
from app.mp4_to_mp3 import mp4_convertation_mp3, youtube_convertation_mp3, remove_file
import time
import io
import os
app = Flask(__name__)

@app.route('/')
def index() -> str:
    return render_template('test_page_mp4_to_mp3.html')

@app.route('/mp4_convertation_mp3', methods=['POST'])
def m4_convertation_mp3_api() -> Response:
    if 'mp4_file' not in request.files:
        return redirect(request.url)

    mp4_file = request.files['mp4_file']

    if mp4_file.filename == '':
        return redirect(request.url)

    if mp4_file:
        mp4_path = os.path.join('../mp4_files', mp4_file.filename)
        mp4_file.save(mp4_path)

    mp3_path = mp4_convertation_mp3(file_name=mp4_file.filename)

    return send_file(mp3_path, as_attachment=True)


#youtube url to mp3 convertation with download on client side
@app.route('/youtube_convertation_mp3', methods=['GET'])
def youtube_convertation_mp3_api():
    youtube_url = request.args.get('url', '')
    mp3_path=youtube_convertation_mp3(youtube_url)
    print(mp3_path)
    return_data = io.BytesIO()
    with open(mp3_path, 'rb') as fo:
        return_data.write(fo.read())
    return_data.seek(0)

    os.remove(mp3_path)

    return send_file(return_data, mimetype='audio/mpeg',
                     download_name='download_filename.mp3')

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
    
    try:
        return send_file(file_path, as_attachment=True)
    finally:
        time.sleep(10)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f'Error deleting file: {e}')
    """

if __name__ == '__main__':
    app.run(debug=True)