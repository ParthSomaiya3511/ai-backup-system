import os

BACKUP_ROOT = "../../storage/backups"

def get_file_versions(file_name):

    folder = os.path.join(
        BACKUP_ROOT,
        file_name
    )

    if not os.path.exists(folder):
        return []

    return sorted(
        os.listdir(folder),
        reverse=True
    )