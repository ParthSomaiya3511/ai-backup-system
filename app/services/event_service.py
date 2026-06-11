from database.repository import save_event
from backup.backup_service import create_backup

def process_event(event_type, event):

    if event.is_directory:
        return

    save_event(
        event_type,
        event.src_path
    )

    if event_type in [
        "CREATED",
        "MODIFIED"
    ]:
        create_backup(
            event.src_path
        )