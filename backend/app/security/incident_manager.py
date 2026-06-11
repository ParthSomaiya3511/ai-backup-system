from database.database import get_connection

def save_incident(

    threat_type,

    severity,

    file_path

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO incidents
        (
            threat_type,
            severity,
            file_path,
            status
        )
        VALUES
        (?, ?, ?, ?)
        """,
        (
            threat_type,
            severity,
            file_path,
            "OPEN"
        )
    )

    conn.commit()

    conn.close()