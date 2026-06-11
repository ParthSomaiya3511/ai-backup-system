CREATE_FILE_EVENTS_TABLE = """
CREATE TABLE IF NOT EXISTS file_events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    event_type TEXT,

    file_path TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);
"""

CREATE_RESTORE_HISTORY_TABLE = """
CREATE TABLE IF NOT EXISTS restore_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    file_name TEXT,

    version TEXT,

    restored_at DATETIME DEFAULT CURRENT_TIMESTAMP

);
"""

CREATE_INCIDENTS_TABLE = """
CREATE TABLE IF NOT EXISTS incidents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    threat_type TEXT,

    severity TEXT,

    file_path TEXT,

    detected_at DATETIME DEFAULT CURRENT_TIMESTAMP

);
"""

CREATE_TABLE_QUERY = '''

CREATE TABLE file_analysis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    file_path TEXT,

    file_type TEXT,

    importance TEXT,

    analyzed_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

'''


CREATE_TABLE_QUERY = '''

CREATE TABLE file_analysis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    file_path TEXT,

    file_type TEXT,

    importance TEXT,

    analyzed_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

'''

CREATE_DEVICES_TABLE = """

CREATE TABLE IF NOT EXISTS devices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT,

    hostname TEXT,

    os TEXT,

    status TEXT,

    last_seen DATETIME

);

"""

CREATE_USERS_TABLE = """

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY,

    name TEXT,

    email TEXT,

    role TEXT,

    password TEXT

);

"""

CREATE_ORGANIZATIONS_TABLE = """

CREATE TABLE IF NOT EXISTS organizations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    plan TEXT,

    users INTEGER,

    devices INTEGER,

    storage_used TEXT

);

"""

CREATE_DEVICES_TABLE = """

CREATE TABLE IF NOT EXISTS devices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT,

    hostname TEXT,

    os TEXT,

    status TEXT,

    last_seen DATETIME

);

"""

CREATE_AUDIT_TABLE = """

CREATE TABLE IF NOT EXISTS audit_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user TEXT,

    action TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""

CREATE_INCIDENTS_TABLE = """

CREATE TABLE IF NOT EXISTS incidents (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    threat_type TEXT,

    severity TEXT,

    file_path TEXT,

    status TEXT,

    detected_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""

CREATE_SECURITY_LOGS_TABLE = """

CREATE TABLE IF NOT EXISTS security_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    event_type TEXT,

    description TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""

CREATE_QUARANTINE_TABLE = """

CREATE TABLE IF NOT EXISTS quarantine (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    file_name TEXT,

    original_path TEXT,

    quarantine_path TEXT,

    quarantined_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""

CREATE_ALERTS_TABLE = """

CREATE TABLE IF NOT EXISTS alerts (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    severity TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""

CREATE_SECURITY_EVENTS_TABLE = """

CREATE TABLE IF NOT EXISTS security_events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    event_type TEXT,

    severity TEXT,

    description TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""

CREATE_DEVICES_TABLE = """

CREATE TABLE IF NOT EXISTS devices (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT UNIQUE,

    hostname TEXT,

    ip_address TEXT,

    operating_system TEXT,

    status TEXT,

    last_seen DATETIME

);

"""

CREATE_DEVICE_COMMANDS_TABLE = """

CREATE TABLE IF NOT EXISTS device_commands (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT,

    command TEXT,

    status TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""

CREATE_DEVICE_HEALTH_TABLE = """

CREATE TABLE IF NOT EXISTS device_health (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT,

    cpu_usage REAL,

    ram_usage REAL,

    disk_usage REAL,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP

);

"""


