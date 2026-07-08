import os


def detect_anomaly(file_path: str) -> dict:

    try:

        size = os.path.getsize(file_path)

        if size > 1024 * 1024 * 500:
            return {
                "detected": True,
                "reason": "Large File"
            }

        return {
            "detected": False
        }

    except Exception as e:

        return {
            "detected": False,
            "error": str(e)
        }