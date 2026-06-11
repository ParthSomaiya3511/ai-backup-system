import time
from watchdog.observers import Observer

from backend.app.monitor.event_handler import BackupEventHandler
from backend.app.config.settings import WATCH_PATHS

def start_monitoring():

    observer = Observer()

    handler = BackupEventHandler()

    for path in WATCH_PATHS:
        observer.schedule(
            handler,
            path,
            recursive=True
        )

    observer.start()

    print("Monitoring Started")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()