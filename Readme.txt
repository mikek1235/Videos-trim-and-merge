You first run the trim-out code to remove the specified intervals in seconds.

The fragments to keep will be kept in the fragments folder and require stitching together through the other ffmpeg commands

ffmpeg stitch video together:
Text file saying:
file '/path/to/video1.mp4'
file '/path/to/video2.mp4'
file '/path/to/video3.mp4
then write in cmd:
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4