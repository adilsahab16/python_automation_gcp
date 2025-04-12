import papermill as pm
import sys
pm.execute_notebook(
    'hello_world.ipynb',
    'hello_world_out.ipynb'  # output log of execution
)
sys.exit(0)  # Graceful exit to indicate success
