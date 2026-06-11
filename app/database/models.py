CREATE_TABLE_QUERY = '''

    CREATE TABLE IF NOT EXISTS file_events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    event_type TEXT,

    file_path TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

)
'''


CREATE_TABLE_QUERY = '''
 
    CREATE TABLE IF NOT EXISTS restore_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    file_name TEXT,

    version TEXT,

    restored_at DATETIME DEFAULT CURRENT_TIMESTAMP

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