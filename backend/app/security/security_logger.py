from database.database import get_connection

def log_security_event(

    event_type,

    severity,

    description

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO security_events
        (
            event_type,
            severity,
            description
        )
        VALUES (?, ?, ?)
        """,
        (
            event_type,
            severity,
            description
        )
    )

    conn.commit()

    conn.close()