from recovery.restore_manager import (
    restore_version
)

def trigger_restore(

    file_name,
    version
):

    return restore_version(
        file_name,
        version
    )