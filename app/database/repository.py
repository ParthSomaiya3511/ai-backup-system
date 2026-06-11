conn = get_connection()

cursor = conn.cursor()

cursor.execute(

    """
    INSERT INTO file_events
    (event_type, file_path)
    VALUES (?, ?)
    """,

    (event_type, file_path)

)

conn.commit()

conn.close()