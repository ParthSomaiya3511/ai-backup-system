from database.database import get_connection

def register_device(

    device_id,
    hostname,
    ip_address,
    os_name

):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO devices
        (
            device_id,
            hostname,
            ip_address,
            operating_system,
            status
        )
        VALUES
        (?, ?, ?, ?, ?)
        """,
        (
            device_id,
            hostname,
            ip_address,
            os_name,
            "ONLINE"
        )
    )

    conn.commit()

    conn.close()