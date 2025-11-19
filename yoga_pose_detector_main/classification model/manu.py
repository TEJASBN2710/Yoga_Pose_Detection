import os

def list_all_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(file)
    return file_list

# Example usage:
files = list_all_files(r"C:\Users\tejas\OneDrive\Desktop\yoga_pose_detector_main")
print(files)
