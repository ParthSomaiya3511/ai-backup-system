import sqlite3

from backend.app.database.models import (
    CREATE_FILE_EVENTS_TABLE,
    CREATE_RESTORE_HISTORY_TABLE,
    CREATE_INCIDENTS_TABLE,
    CREATE_DEVICES_TABLE,
    CREATE_USERS_TABLE,
    CREATE_ORGANIZATIONS_TABLE,
    CREATE_AUDIT_TABLE,
    CREATE_SECURITY_LOGS_TABLE,
    CREATE_QUARANTINE_TABLE,
    CREATE_ALERTS_TABLE
)

DB_PATH = "../../storage/database/backup.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(CREATE_FILE_EVENTS_TABLE)

    cursor.execute(CREATE_RESTORE_HISTORY_TABLE)

    cursor.execute(CREATE_INCIDENTS_TABLE)
    
    cursor.execute(
        CREATE_DEVICES_TABLE
    )
    
    cursor.execute(
        CREATE_USERS_TABLE
    )
    
    cursor.execute(
        CREATE_ORGANIZATIONS_TABLE
    )

    cursor.execute(
        CREATE_AUDIT_TABLE
    )
    
    cursor.execute(
        CREATE_ALERTS_TABLE
    )
    
    cursor.execute(CREATE_INCIDENTS_TABLE)

    cursor.execute(CREATE_SECURITY_LOGS_TABLE)

    cursor.execute(CREATE_QUARANTINE_TABLE)

    conn.commit()

    conn.close()