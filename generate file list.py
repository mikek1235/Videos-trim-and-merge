import os
# Define the base path and the file name pattern
base_path = 'C:\\Users\\Mkarkus\Desktop\\trim_test\\Fragments'
file_name_pattern = 'output_fragment_{}.mp4'

# Generate the file list
file_list = 'C:\\Users\\Mkarkus\Desktop\\trim_test\\Fragments\\mylist.txt'
with open(file_list, 'w') as list_file:
    for i in range(1, 95):  # Start at 1, end at 94
        video_file = os.path.join(base_path, file_name_pattern.format(i))
        list_file.write(f"file '{video_file}'\n")
