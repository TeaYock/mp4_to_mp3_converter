# __ONLINE MEDIA📹 CONVERTER TO MP3🎵__
This online converter turns a downloaded MP4 file or a link from YouTube into MP3, which you can download to your device.

---------------------

# What does it consist of?🏗️
## app directory 🧰 : 
The app directory contains the internal structure of the program and its API. Namely:

**mp4_to_mp3.py** - contains functions for converting MP4 and a link from YouTube to MP3, creating folders for temporary storage of files and deleting them with subsequent conversion into a byte stream for sending.

**main.py** - the main file that launches the API.

### Directory api 📡 :
**api_get_mp4_from_youtube.py** - API on Flask, accepting mp4 files or a link from YouTube and validating it, after which it returns the mp3 to the user.

**swagger.py** - swagger documentation that contains examples of possible errors and the ability to test some functions.

### Directory website 📃 :
**test_page_mp4_to_mp3.html** - web page for user interaction with the program.

## docker directory 🐳 :
Contains **Dockerfile** and **docker-compose.yml** for creating an image and container, as well as a configuration file (**values.yaml**) and a meta file (**Chart.yaml**) for Helm.
# templates directory ☸️ : 
Contains the **deployment.yaml** manifest file for Kubernetes, which launches a cluster with an application.

## tests directory 🔧:
Contains a set of unit tests for the application. **test_convertation.py** - tests of conversion functions **test_api.py** - api tests

--------------------
# Libraries 📚:
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) was used for api
- [moviepy](https://pypi.org/project/moviepy/) was used for conversion
- [pytube](https://github.com/pytube/pytube) and [yt-dlp](https://github.com/yt-dlp) were used to download mp4/mp3 from youtube. Pytube stopped working after update of YouTube Java Script, and the developer does not make update, therefore the version of the library from community with a fix is ​​used (https://github.com/pytube/pytube.git@e7a074e9e4eb3715a0ea05904dcb5f3d55c9fe9f). Yt-dlp requires pre-installed [ffmpeg](https://www.ffmpeg.org/) for its work.
- [pytest](https://docs.pytest.org/en/stable/) was used for tests
----------------------------------
# Launch in the cloud ☁️:
This project was launched on a cluster of nodes in GCP:
+ the site itself: http://34.116.208.74:5000/
+ swagger documentation: http://34.116.208.74:5000/swagger/

--------------------------------------
About Creator (TeaYock🍵): 
+ instagram: https://www.instagram.com/_._tea_._tea_._tea_._/
+ telegram: TEA5566
+ discord: tea_tea_tea_tea