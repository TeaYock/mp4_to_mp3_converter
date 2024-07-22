from flask_restx import Api, Resource, fields
from api_get_mp3_from_mp4_youtube import app, mp4_convertation_mp3_api, youtube_convertation_mp3_api

# Initialize the API with documentation at /swagger/
api = Api(app, doc='/swagger/',
          version='1.0',
          title='MP4/YouTube to MP3 API',
          description='API to convert MP4 files and YouTube URLs to MP3.',
          servers=[
              {
                  'url': 'http://localhost:5000/',
                  'description': 'Local server'
              }
          ])

# Defining a namespace for the API
ns = api.namespace('mp3_online_convertation', description='MP4 to MP3 and YouTube to MP3 convertation operations')
convertation_ns = api.namespace('conversion', description='Conversion operations')

# Model for downloading MP4 file
upload_parser = api.parser()
upload_parser.add_argument('mp4_file', location='files', type='FileStorage',
                           required=True, help='The MP4 file to be uploaded')

# Model for YouTube URL
youtube_model = convertation_ns.model('YouTube', {
    'url': fields.String(required=True, description='The YouTube URL to be converted to MP3')
})

# Error model no audio
error_model_audio = api.model('ErrorAudio', {
    'error': fields.String(description='Error message', example='The video file does not contain an audio track')
})

# Standard error model
error_model = api.model('Error', {
    'error': fields.String(description='Error message', example='Bad request due to missing parameters')
})

# Resource class for converting MP4 to MP3
@ns.route('/mp4_convertation_mp3')
class MP4ToMP3(Resource):
    @api.expect(upload_parser, validate=True)
    @api.response(200, 'Success', headers={'Content-Disposition': 'attachment; filename=output.mp3'})
    @api.response(400, 'Bad Request', model=error_model_audio)
    @api.response(500, 'Internal Server Error')
    def post(self):
        return mp4_convertation_mp3_api()

# Resource class for converting YouTube URL to MP3
@ns.route('/youtube_convertation_mp3')
class YouTubeToMP3(Resource):
    @api.doc(youtube_model, params={'url': 'The YouTube URL to be converted to MP3'})
    @api.response(200, 'Success', headers={'Content-Disposition': 'attachment; filename=output.mp3'})
    @api.response(400, 'Bad Request', model=error_model)
    @api.response(500, 'Internal Server Error')
    def get(self):
        return youtube_convertation_mp3_api()

if __name__ == '__main__':
    app.run(debug=True)