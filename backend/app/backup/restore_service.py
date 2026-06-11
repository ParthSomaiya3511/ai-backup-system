import shutil

def restore_file(
    backup_file,
    original_path
):

    shutil.copy2(
        backup_file,
        original_path
    )