import papermill as pm
import time
pm.execute_notebook(
    'hello_world.ipynb',
    'hello_world_out.ipynb'  # output log of execution
)
# Keep container alive for Cloud Run health checks
time.sleep(300)
