'''
download video from youtube using pytube 
https://pytube.io/en/latest/user/quickstart.html#downloading-a-video

get audio from video 
'''
from pytube import YouTube, Playlist
from os.path import exists

class Audio_zen(): 
    def __init__(self, paylist_url: str) -> None:
        print("audio zen") 
        self.playlist = Playlist(paylist_url)
        self.path  = './downloaded_videos'

    def download_paylist_videos(self): 
        print(f"Downloading playlist '{self.playlist.title}' audios:")
        for url in self.playlist.video_urls:
            self.download_yt_video(url)
        print("\n")

    def download_yt_video(self,url):
        try: 
            yt = YouTube(url)
            list_of_streams = yt.streams.filter(only_audio=True)

            # abr = adaptive bitrate streaming 
            # technique for adjusting compression level
            # print(list_of_streams)
            
            #TODO: investigate features of stream call result 
            list_of_streams[0].download(self.path)

        except Exception as e: 
            print(e)