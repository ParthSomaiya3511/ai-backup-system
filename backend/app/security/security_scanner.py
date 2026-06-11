import os

from security.threat_engine import (
    analyze_file
)

def scan_directory(path):

    threats = []

    for root, dirs, files in os.walk(path):

        for file in files:

            full_path = os.path.join(

                root,

                file

            )

            result = analyze_file(

                full_path

            )

            if result["type"] != "SAFE":

                threats.append({

                    "file":
                    full_path,

                    "result":
                    result

                })

    return threats