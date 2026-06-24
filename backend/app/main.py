from app.database.database import initialize_database
from backend.app.monitor.file_monitor import start_monitoring
from api.server import app

if __name__ == "__main__":

    initialize_database()

    start_monitoring()