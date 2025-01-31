# youtube_downloader
A youtube downloader web app using Django and yt_dlp.

# Useful commands / setup
Download [yt_dlp](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#installation), which is an alternative to the pytube module.

`pip install yt_dlp`

Install django (windows):

`py -m pip install Django`

Your project may not work properly until you apply the migrations for app(s):

`python manage.py migrate`

Install ffmpeg with choco for video processing:

`choco install ffmpeg`

Run app locally:

`python manage.py runserver`

### Helpful information / tutorials:
[Download YouTube videos using yt_dlp module](https://www.geeksforgeeks.org/python-download-youtube-videos-using-youtube_dl-module/) 
