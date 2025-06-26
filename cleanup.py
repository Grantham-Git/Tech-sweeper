# cleanup.py

import os
import tempfile

def clean_temp_folder():
    temp_dir = tempfile.gettempdir()
    deleted = 0
    failed = 0

    print("🗑️ Cleaning Temporary Files...")
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
                deleted += 1
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # removes empty folders only
                deleted += 1
        except Exception as e:
            failed += 1
            continue

    print(f"✅ Deleted {deleted} files/folders.")
    if failed > 0:
        print(f"⚠️ Skipped {failed} items due to access restrictions.")
