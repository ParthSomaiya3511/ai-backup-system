import os
import shutil

from backend.app.backup.version_manager import get_version_name

BACKUP_ROOT = "../../storage/backups"

def create_backup(file_path):

    if not os.path.exists(file_path):
        return

    file_name = os.path.basename(file_path)

    version = get_version_name()

    backup_folder = os.path.join(
        BACKUP_ROOT,
        file_name
    )

    os.makedirs(
        backup_folder,
        exist_ok=True
    )

    extension = os.path.splitext(file_name)[1]

    destination = os.path.join(
        backup_folder,
        f"{version}{extension}"
    )

    shutil.copy2(
        file_path,
        destination
    )