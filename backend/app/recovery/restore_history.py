from app.database.database import get_connection

def save_restore_history(
    file_name,
    version
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO restore_history
        (
            file_name,
            version
        )
        VALUES (?, ?)
        """,
        (
            file_name,
            version
        )
    )

    conn.commit()
    conn.close()