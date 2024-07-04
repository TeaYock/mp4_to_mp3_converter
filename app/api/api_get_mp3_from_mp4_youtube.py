from flask import Flask, request, send_file
from app.mp4_to_mp3 import m4_convertation_mp3, youtube_convertation_mp3
app = Flask(__name__)

"""
@app.route('/m4_convertation_mp3')
def m4_convertation_mp3_api():
    file_path="../mp3_files/[ Devil May Cry 5 ] I AM THE STORM THAT IS APPROACHING BUT IN 4K.mp3"
    return send_file(file_path, as_attachment=True)
"""

#youtube url to mp3 convertation with download on client side
@app.route('/youtube_convertation_mp3', methods=['GET'])
def youtube_convertation_mp3_api():
    youtube_url = request.args.get('url', '')
    file_path=youtube_convertation_mp3(youtube_url)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)