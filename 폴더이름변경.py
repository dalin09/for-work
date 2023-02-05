import os

folder_path = "/Users/ksh2/Desktop/무제 폴더"
for filename in os.listdir(folder_path):
    parts = filename.split("_")
    if len(parts) == 2:
        new_filename = parts[1] + "_" + parts[0]
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))