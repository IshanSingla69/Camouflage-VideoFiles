# Camouflage-VideoFiles
# Random Folder and Video Generator 📁🎥

This is a Python script that creates a random folder structure with blank video files in it. It can be used for testing purposes or just for fun.

## What it does 🤔

The script does the following steps:

- It creates a root folder named `root` if it doesn't exist.
- It creates a folder structure recursively inside the root folder, with 10 subfolders in each level. The number of levels can be changed by modifying the `levels` parameter in the `create_folder_structure` function call.
- It finds the deepest folders in the folder structure, i.e., the ones that have no subfolders in them.
- It randomly chooses one of the deepest folders to be empty, and prints its name and directory.
- It creates blank video files with `.mp4` extension in the other deepest folders, with random names. The number of video files in each folder can vary from 49 to 50.
- It prints a message when the video files are added successfully.

## How to run it 🚀

To run the script, you need to have Python installed on your system.

Then, you can simply run the script from the command line or any IDE of your choice.

For example, if you are using Windows, you can open a command prompt window and type:

```bash
python PlayWithFolders.py
```

You should see something like this:

```bash
Empty Folder Name: xLZqkWmQlI
Directory: C:\Users\user\Desktop\root\XwYjLrQaZs\yfJtXgZpQo\XwYjLrQaZs\xLZqkWmQlI
Video files added to folders successfully.
```

You can then explore the folder structure and the video files that were created.

## Disclaimer ⚠️

This script is for educational and entertainment purposes only. It does not intend to harm any system or data. However, use it at your own risk. The author is not responsible for any damages or losses caused by this script.
