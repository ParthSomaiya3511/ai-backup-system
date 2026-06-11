import subprocess

def execute_script(
    path
):

    result = subprocess.run(

        ["python", path],

        capture_output=True,

        text=True

    )

    return result.stdout