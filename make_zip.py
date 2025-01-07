import os
import zipfile
import time
from datetime import datetime
import shutil

source_folder = r"C:\Users\user1\Desktop\source"  
destination_folder = r"C:\Users\user1\Desktop\destination"  
processed_files = set()


def zip_new_files():
    # 'dd_mm_yyyy'
    today_date = datetime.now().strftime("%d_%m_%Y")
    current_date_folder = os.path.join(source_folder, today_date)

    if not os.path.exists(current_date_folder):
        print(f"No folder for today's date ({today_date}). Waiting for the next run...")
        return

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    zip_file_name = f"{timestamp}.zip"
    zip_file_path = os.path.join(destination_folder, zip_file_name)

    log_file_name = f"{timestamp}.txt"
    log_file_path = os.path.join(destination_folder, log_file_name)

    files_zipped = False

    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:

        with open(log_file_path, 'w') as logf:
            logf.write(f"Backup Log\n")
            logf.write(f"Timestamp: {timestamp}\n")
            logf.write(f"Zip File: {zip_file_name}\n")
            logf.write(f"Source Folder: {current_date_folder}\n")
            logf.write(f"Destination Folder: {zip_file_path}\n")
            logf.write("Files Included:\n")

            for root, dirs, files in os.walk(current_date_folder):
                for file in files:
                    file_path = os.path.join(root, file)

                    if file_path not in processed_files:
                        zipf.write(file_path, os.path.relpath(file_path, source_folder))
                        logf.write(f"  - {os.path.relpath(file_path, source_folder)}\n")
                        processed_files.add(file_path)  
                        files_zipped = True

            if files_zipped:
                for root, dirs, files in os.walk(current_date_folder, topdown=False):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if file_path in processed_files:
                            os.remove(file_path)

                    for dir in dirs:
                        dir_path = os.path.join(root, dir)
                        if not os.listdir(dir_path):
                            os.rmdir(dir_path)

            if not files_zipped:
                logf.write("No new files found to zip.\n")

    if files_zipped:
        print(f"Zipped new files into: {zip_file_name}, Log saved as: {log_file_name}")
    else:
        print("No new files to zip. Waiting for the next run...")


def main():
    while True:
        zip_new_files()
        print("Waiting for 2 hours before checking again...")
        time.sleep(7200)


if __name__ == "__main__":
    main()
