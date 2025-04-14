import papermill as pm
from flask import Flask
import threading

# Define a function that runs your notebook
def run_notebook():
    pm.execute_notebook(
        'hello_world.ipynb',           # Input notebook
        'hello_world_output.ipynb'     # Output notebook
    )
    print("Notebook finished running.")

# Start the notebook in a background thread (so it doesn't block Flask)
threading.Thread(target=run_notebook).start()

# Create a simple Flask app
app = Flask(__name__)

# Just a test page to return when visiting root
@app.route('/')
def index():
    return "Notebook is running in background."

# Start the Flask server so Cloud Run sees that the app is alive
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
