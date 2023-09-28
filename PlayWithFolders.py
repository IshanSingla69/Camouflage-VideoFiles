import os
import random
import string
import shutil

# Function to generate a random folder name
def random_folder_name():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

# Function to create a folder structure recursively
def create_folder_structure(path, levels):
    if levels == 0:
        return
    for _ in range(10):
        folder_name = random_folder_name()
        folder_path = os.path.join(path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            create_folder_structure(folder_path, levels - 1)

# Function to create blank video files
def create_video_files(path):
    for _ in range(random.randint(49, 50)):
        video_name = ''.join(random.choice(string.ascii_letters) for _ in range(10)) + '.mp4'
        video_path = os.path.join(path, video_name)
        open(video_path, 'w').close()

# Create the root folder if it doesn't exist
root_folder = 'root'
if not os.path.exists(root_folder):
    os.makedirs(root_folder)

# Create the folder structure
create_folder_structure(root_folder, 4)

# Find the deepest folders
deepest_folders = []
for root, _, _ in os.walk(root_folder):
    if not os.listdir(root):
        deepest_folders.append(root)

# Randomly choose one of the deepest folders to be empty
if deepest_folders:
    empty_folder = random.choice(deepest_folders)
    print("Empty Folder Name:", os.path.basename(empty_folder))
    print("Directory:", os.path.abspath(empty_folder))

# Add blank video files to random folders in the deepest level
for folder in deepest_folders:
    if folder != empty_folder:
        create_video_files(folder)

print("Video files added to folders successfully.")
