'''
download video from youtube using pytube 
https://pytube.io/en/latest/user/quickstart.html#downloading-a-video

get audio from video 
'''
from pytube import YouTube
from os.path import exists

class Audio_zen(): 
    def __init__(self, urls: list) -> None:
        print("audio zen") 
        self.urls = urls
        self.path  = './downloaded_videos'
    def download_yt_video(self):

        for url in self.urls:
            try: 
                yt = YouTube(url)
                yt.download(self.path)
            except Exception as e: 
                print(e)