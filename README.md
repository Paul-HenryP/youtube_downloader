# youtube_downloader
A youtube downloader web app using Django and yt_dlp.

# Useful commands / setup
1. Download [yt_dlp](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#installation), which is an alternative to the pytube module.

`pip install yt_dlp`

2. Install django (windows):

`py -m pip install Django`

3. Your project may not work properly until you apply the migrations for app(s):

`python manage.py migrate`

4. Install ffmpeg with choco for video processing (Might need to run as admin):

`choco install ffmpeg`

5. Run app locally:

`python manage.py runserver`

OR just:

`pip install -r requirements.txt`

## Demo
![image](https://github.com/user-attachments/assets/9c1cba6e-7873-4270-a835-9f64e6f714c6)




### Helpful information / tutorials:
[Download YouTube videos using yt_dlp module](https://www.geeksforgeeks.org/python-download-youtube-videos-using-youtube_dl-module/) 
