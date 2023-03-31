import os
from moviepy.editor import *

resolution = 1920, 1080

sourceFolder = "source folder path"
targetFolder = f"{sourceFolder}/{resolution[0]} x {resolution[1]}"

# Cache the files to avoid regenerating them on subsequent runs
files = []
for root, directories, filenames in os.walk(sourceFolder):
    for filename in filenames:
        files.append(os.path.join(root, filename))

if not os.path.exists(targetFolder):
    os.makedirs(targetFolder)

for file_path in files:
    # Get the file name
    file_name = os.path.basename(file_path)
    resized_file_path = os.path.join(targetFolder, file_name)

    if not os.path.exists(resized_file_path):
        # Load the video
        clip = VideoFileClip(file_path)

        # Resize the video
        clip_resized = clip.resize(resolution)

        # Save the resized video to a new file
        clip_resized.write_videofile(resized_file_path, codec='libx264')
