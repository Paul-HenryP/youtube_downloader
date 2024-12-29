from django.shortcuts import render
#from pytube import YouTube #Not working anymore: HTTP 403 forbidden error.
import yt_dlp #Using this instead. yt_dlp is well maintained and works.

def home(request):
    return render(request, "home.html")

def final(request):
    return render(request, "final.html")


def download(request):
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download(request.GET['inp']) #request.GET['inp'] = url
    print("Video downloaded successfully")
    return render(request, "final.html")
