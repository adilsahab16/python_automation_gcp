import papermill as pm

pm.execute_notebook(
    'hello_world.ipynb',
    'hello_world_out.ipynb'  # output log of execution
)