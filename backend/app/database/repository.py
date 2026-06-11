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
            file_path
        )
        VALUES (?, ?, ?)
        """,
        (
            threat_type,
            severity,
            file_path
        )
    )

    conn.commit()
    conn.close()