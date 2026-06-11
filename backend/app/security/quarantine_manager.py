import os
import shutil

QUARANTINE_DIR = (
    "../../storage/quarantine"
)

def quarantine_file(file_path):

    if not os.path.exists(file_path):

        return False

    filename = os.path.basename(file_path)

    destination = os.path.join(

        QUARANTINE_DIR,

        filename

    )

    shutil.move(
        file_path,
        destination
    )

    return destination