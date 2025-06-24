import os
import hashlib
import time

# Setting the path to the folder you want to monitor
DIRECTORY_TO_MONITOR = r"E:\KHURSHEED\my_personal_file"

# Create a dictionary to store the hash of each file
file_hashes = {}

def get_file_hash(file_path):
    """Calculate the SHA256 hash of a file"""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

print("🟢 Starting file monitoring...")

# Initial scan
if os.path.exists(DIRECTORY_TO_MONITOR):
    for filename in os.listdir(DIRECTORY_TO_MONITOR):
        full_path = os.path.join(DIRECTORY_TO_MONITOR, filename)
        if os.path.isfile(full_path):
            file_hashes[filename] = get_file_hash(full_path)
else:
    print("⚠️ Folder not found:", DIRECTORY_TO_MONITOR)
    exit()

# Start watching the folder
while True:
    time.sleep(5)
    current_files = os.listdir(DIRECTORY_TO_MONITOR)
    print("\nFiles in folder right now:", current_files)

    # Check for new files
    for filename in current_files:
        full_path = os.path.join(DIRECTORY_TO_MONITOR, filename)
        if filename not in file_hashes:
            file_hashes[filename] = get_file_hash(full_path)
            #adding of file if its found in the originated file
            print(f"🟢 Added: {filename}")
        else:
            #getting files path
            current_hash = get_file_hash(full_path)
            if current_hash != file_hashes[filename]:
                file_hashes[filename] = current_hash
                print(f"🟡 Modified: {filename}")

    # Check for deleted files
    deleted_files = []
    for filename in list(file_hashes.keys()):
        if filename not in current_files:
            deleted_files.append(filename)
            del file_hashes[filename]
            print(f"🔴 Deleted: {filename}")
