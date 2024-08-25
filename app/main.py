import sys
import os
from multiprocessing import Process, set_start_method
from api import api_app, swagger_app

# Set the start method for multiprocessing to 'spawn'
set_start_method('spawn', force=True)

# Add the current directory to the system path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Run the main API app
def run_api():
    api_app.run(debug=True, port=5000, use_reloader=False)

# Run the Swagger documentation app
def run_swagger():
    swagger_app.run(debug=True, port=5001, use_reloader=False)

if __name__ == '__main__':
    # Create separate processes for the API app and the Swagger app
    api_process = Process(target=run_api)
    swagger_process = Process(target=run_swagger)

    api_process.start()
    swagger_process.start()

    api_process.join()
    swagger_process.join()