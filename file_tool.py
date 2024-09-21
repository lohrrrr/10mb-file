import os

debug = True
from PIL import Image
import os
import ffmpeg
from ffmpeg import probe

def image_type(image_path, size_out, output_path):
    # The most parts of this code parsed from stak overflow and i rly dont have any idea would it work or just make IMG bd qlty. This code is suck. I am so sorry
    # FileCompressor sucks - keep in mind...
    if debug:
        print("[DEBUG]:IMAGE MODULE STARTED")
    #---------------------------------------#
    target_size_bytes = size_out * 1024 * 1024
    img = Image.open(image_path)
    # IDK WHAT DOING THIS PART! THIS PART WRITEN BY AI
    quality = 90

    # Save the image with the initial quality
    img.save(output_path, quality=quality, optimize=True)

    # Loop until the image size is within the target size
    while os.path.getsize(output_path) > target_size_bytes:
        # Re-open the saved image to get its size
        img = Image.open(output_path)

        # If the size is still larger than the target, decrease the quality
        if os.path.getsize(output_path) > target_size_bytes:
            quality -= 10
            if quality < 0:
                print("Cannot compress image to the desired size.")
                break
            # Save the image with the new quality
            img.save(output_path, quality=quality, optimize=True)

    # Print the compressed image size
    print(f"Compressed image size: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")
    #---------------------------------------#
    #AYO NO WAY WORKING CODE!



#def video_type(video_path, tagret_size, output_path):
#    # I'll try, maybe...
#    import moviepy.editor as moviepy
#    clip = moviepy.VideoFileClip(video_path)
#    #---------------------------------------#
    
def compress_video(video_full_path, output_file_name, target_size):
    # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000

    probe = ffmpeg.probe(video_full_path)
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    # Audio bitrate, in bps.
    audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
    # Target total bitrate, in bps.
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Target audio bitrate, in bps
    if 10 * audio_bitrate > target_total_bitrate:
        audio_bitrate = target_total_bitrate / 10
        if audio_bitrate < min_audio_bitrate < target_total_bitrate:
            audio_bitrate = min_audio_bitrate
        elif audio_bitrate > max_audio_bitrate:
            audio_bitrate = max_audio_bitrate
    # Target video bitrate, in bps.
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, os.devnull,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                  ).overwrite_output().run()
    ffmpeg.output(i, output_file_name,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                  ).overwrite_output().run()
