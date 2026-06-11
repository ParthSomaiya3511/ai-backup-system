import shutil

def recover_latest_version(
    backup_file,
    restore_path
):

    shutil.copy2(
        backup_file,
        restore_path
    )

    return True