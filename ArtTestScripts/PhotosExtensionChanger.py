import os

folder_path = "D:\Recyculd"  # Update this with the path to your folder
extension = ".jpg"

for count, filename in enumerate(os.listdir(folder_path)):
    new_name = f"newname{count + 1}{extension}"
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
