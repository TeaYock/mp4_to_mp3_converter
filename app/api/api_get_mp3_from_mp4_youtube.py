from flask import Flask, send_file
app = Flask(__name__)

@app.route('/m4_convertation_mp3')
def download_file():
    file_path="../mp3_files/[ Devil May Cry 5 ] I AM THE STORM THAT IS APPROACHING BUT IN 4K.mp3"
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)