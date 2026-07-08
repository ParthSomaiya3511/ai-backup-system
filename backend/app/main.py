from app.database.database import initialize_database
from app.monitor.file_monitor import start_monitoring
from app.api.server import app

initialize_database()

# Uncomment after confirming file_monitor works
# start_monitoring()