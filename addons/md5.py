import os
import hashlib

def generate_md5_for_folder(folder_path):
    md5 = hashlib.md5()
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    md5.update(chunk)
    return md5.hexdigest()

addons_folder = r"C:\Users\T-11-User\Desktop\repository.hacker0x00-1\addons"

for addon_folder in os.listdir(addons_folder):
    full_addon_folder = os.path.join(addons_folder, addon_folder)
    if os.path.isdir(full_addon_folder):
        # Exclude the MD5.py script
        if not addon_folder == "md5.py":
            md5_value = generate_md5_for_folder(full_addon_folder)
            md5_filename = os.path.basename(addon_folder) + ".md5"
            with open(os.path.join(full_addon_folder, md5_filename), "w") as f:
                f.write(md5_value)
