import subprocess
#note: ensure you have ffmpeg, installed. It should be included with deeplabcut
# Define the path to the input video and the name for the output fragments
input_video_path = 'C:\\Users\\Mkarkus\\Desktop\\trim_test\\input.mp4'

# Read the list of cuts from the text file
with open('C:\\Users\\Mkarkus\\Desktop\\trim_test\\cuts.txt', 'r') as file:
    intervals = file.readlines()

# Process each interval
for i, interval in enumerate(intervals):
    start_time, end_time = interval.strip().split()
    
    # Calculate the duration for each cut
    duration = int(end_time) - int(start_time)
    
    # Define the name for the output file for this specific interval
    output_video_path = f'C:\\Users\\Mkarkus\\Desktop\\trim_test\\Fragments\\output_fragment_{i+1}.mp4'
    
    # Construct the FFmpeg command to cut the video
    command = [
        'ffmpeg',
        '-ss', str(start_time),    # Start time
        '-i', input_video_path,    # Input file
        '-t', str(duration),       # Duration to cut
        '-c', 'copy',              # Use same codecs
        '-avoid_negative_ts', 'make_zero', # Avoid negative timestamps
        output_video_path          # Output file
    ]
    
    # Execute the command
    subprocess.run(command)

    print(f'Created {output_video_path}')
