import subprocess
import os

# Specify the file containing the list of video files to concatenate
file_list = 'C:\\Users\\Mkarkus\Desktop\\trim_test\\fragments\\mylist.txt'

# Define the output file name
output_video = 'C:\\Users\\Mkarkus\Desktop\\trim_test\\fragments\\stitched_output_Nov7.mp4'

# FFmpeg command to concatenate the videos
ffmpeg_command = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', file_list, '-c', 'copy', output_video]

# Execute the FFmpeg command
try:
    subprocess.run(ffmpeg_command, check=True)
    print(f"Videos have been concatenated successfully into {output_video}")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while concatenating videos: {e}")
