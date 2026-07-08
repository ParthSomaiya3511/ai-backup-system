from datetime import datetime

from app.database.repository import save_event
from app.backup.backup_service import create_backup


def process_event(event_type, event):

    if event.is_directory:
        return

    event_data = {
        "file_path": event.src_path,
        "event_type": event_type,
        "event_time": datetime.now().isoformat()
    }

    save_event(event_data)

    if event_type in ["CREATED", "MODIFIED"]:
        create_backup(event.src_path)