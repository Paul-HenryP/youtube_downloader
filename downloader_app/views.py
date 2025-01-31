from django.shortcuts import render
import yt_dlp #Using this instead. yt_dlp is well maintained and works.
import os
import subprocess

def home(request):
    return render(request, "home.html")

def final(request):
    return render(request, "final.html")

def download(request):
    video_url = request.GET.get('inp')
    file_format = request.GET.get('format', 'mp4')  # Default to MP4.

    output_path = "C:/Users/User/Downloads/%(title)s.%(ext)s"  # Saves in the downloads folder.
    ydl_opts = {'outtmpl': output_path}

    if file_format == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio/best',
            'merge_output_format': 'mp4',
        })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        downloaded_file = ydl.prepare_filename(info_dict)

    # Converts MP4 to MOV if requested.
    if file_format == "mov":
        mov_file = downloaded_file.replace(".mp4", ".mov")
        conversion_command = [
            "ffmpeg", "-i", downloaded_file, "-f", "mov", "-q:v", "1", "-y", "C:\\Users\\User\\Downloads\\output.mov"
        ]


        try:
            subprocess.run(conversion_command, check=True)
            os.remove(downloaded_file)  # Removes MP4 after conversion.
            print(f"Converted {downloaded_file} to {mov_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting to MOV: {e}")

    print(f"Video downloaded successfully as {file_format}")
    return render(request, "final.html")


#old version.
'''
def download(request):
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(request.GET['inp']) #request.GET['inp'] = url
    print("Video downloaded successfully")
    return render(request, "final.html")
'''