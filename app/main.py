import sys
import os
from multiprocessing import Process, set_start_method

# Установка метода старта для процессов
set_start_method('spawn', force=True)

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from api import api_app, swagger_app

def run_api():
    api_app.run(debug=True, port=5000, use_reloader=False)

def run_swagger():
    swagger_app.run(debug=True, port=5001, use_reloader=False)

if __name__ == '__main__':
    api_process = Process(target=run_api)
    swagger_process = Process(target=run_swagger)

    api_process.start()
    swagger_process.start()

    api_process.join()
    swagger_process.join()