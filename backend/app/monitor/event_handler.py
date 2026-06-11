from watchdog.events import FileSystemEventHandler
from backend.app.services.event_service import process_event

class BackupEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        process_event("CREATED", event)

    def on_modified(self, event):
        process_event("MODIFIED", event)

    def on_deleted(self, event):
        process_event("DELETED", event)

    def on_moved(self, event):
        process_event("MOVED", event)