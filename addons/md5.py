import hashlib

def generate_md5(filepath):
    md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    return md5.hexdigest()

addon_folder = r"C:\Users\T-11-User\Desktop\repository.hacker0x00-1\addons\plugin.video.thepromise"
md5_value = generate_md5(addon_folder)
with open(f"{addon_folder}.md5", "w") as f:
    f.write(md5_value)