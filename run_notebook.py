import papermill as pm
from flask import Flask
import threading
import logging

# Setup basic logging config — this is what Cloud Run will capture
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function that runs your notebook
def run_notebook():
    try:
        logger.info("Starting notebook execution...")
        pm.execute_notebook(
            'hello_world.ipynb',           # Input notebook
            'hello_world_output.ipynb',    # Output notebook
            #log_output=True                # Show cell outputs in logs
        )
        logger.info("Notebook execution finished successfully.")
    except Exception as e:
        logger.error(f"Error running notebook: {e}")

# Start the notebook in a background thread (so it doesn't block Flask)
threading.Thread(target=run_notebook).start()

# Create a simple Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "Notebook is running in background."

# Start the Flask server so Cloud Run sees that the app is alive
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
