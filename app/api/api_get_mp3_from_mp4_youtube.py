import os

from flask import Flask, request, send_file, redirect, render_template, Response, jsonify, make_response
from app.mp4_to_mp3 import mp4_convertation_mp3, youtube_convertation_mp3, remove_file_make_return_data, creating_mp4_dir, creating_mp3_dir
from os import path, remove
app = Flask(__name__)

# Make directories for mp3 and mp4
creating_mp4_dir()
creating_mp3_dir()

# Route handler for the homepage
@app.route('/')
def index() -> str:
    return render_template('test_page_mp4_to_mp3.html')

# Mp4 in mp3 convertation
@app.route('/mp4_convertation_mp3', methods=['POST'])
def mp4_convertation_mp3_api() -> Response:
    # Handling File Upload
    if 'mp4_file' not in request.files:
        return redirect(request.url)

    mp4_file = request.files['mp4_file']

    if mp4_file.filename == '':
        return redirect(request.url)

    # Converting
    if mp4_file:
        mp4_path = path.join('../mp4_files/', mp4_file.filename)
        mp4_file.save(mp4_path)
        try:
            mp3_path, mp3_filename = mp4_convertation_mp3(mp4_file_name=mp4_file.filename)
        except ValueError as e:
            os.remove(mp4_path)
            error_response = make_response(jsonify({'error': str(e)}), 400)
            return error_response

        # Converting mp3 file to byte stream and sending response to client
        response_data = remove_file_make_return_data(mp3_path=mp3_path, mp4_path=mp4_path)
        return send_file(response_data, mimetype='audio/mpeg',
                         as_attachment=True, download_name=mp3_filename)


# YouTube url to mp3 convertation with download on client side
@app.route('/youtube_convertation_mp3', methods=['GET'])
def youtube_convertation_mp3_api() -> Response:
    # Getting YouTube url from arguments
    youtube_url = request.args.get('url', '')

    # Converting
    mp3_path=youtube_convertation_mp3(youtube_url)
    mp3_name=path.basename(mp3_path)

    # Converting mp3 file to byte stream and sending response to client
    response_data = remove_file_make_return_data(mp3_path = mp3_path)
    return send_file(response_data, mimetype='audio/mpeg',
                     download_name=mp3_name)

if __name__ == '__main__':
    app.run(debug=True)