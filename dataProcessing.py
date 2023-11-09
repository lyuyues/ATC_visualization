
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import which

AudioSegment.converter = which("ffmpeg")

file_name = "2023-11-05-17-14-32"
audio_file_path = "data/" + file_name + ".mp3"
source = AudioSegment.from_mp3(audio_file_path)
# play(source)

segment_duration = 20 * 60 * 1000

# Calculate the number of segments
num_segments = len(source) // segment_duration

# Loop over the number of segments and export each as a separate file
for i in range(num_segments):
    start_time = i * segment_duration
    end_time = start_time + segment_duration
    segment = source[start_time:end_time]
    segment.export(f"data/{file_name}/segment_{i}/{num_segments}.mp3", format="mp3")

# If there is any remaining audio that is less than the segment duration, export it as a final segment
if len(source) % segment_duration != 0:
    start_time = num_segments * segment_duration
    segment = source[start_time:]
    segment.export(f"data/{file_name}/segment_{num_segments}.mp3", format="mp3")