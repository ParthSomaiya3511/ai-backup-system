from app.database.database import get_connection


def save_event(event_data):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO file_events (
            file_path,
            event_type,
            event_time
        )
        VALUES (?, ?, ?)
        """,
        (
            event_data["file_path"],
            event_data["event_type"],
            event_data["event_time"]
        )
    )

    conn.commit()
    conn.close()