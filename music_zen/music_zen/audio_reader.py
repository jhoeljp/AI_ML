'''
download video from youtube using pytube 
https://pytube.io/en/latest/user/quickstart.html#downloading-a-video

get audio from video 
'''
from pytube import YouTube, Playlist
from os.path import exists
import librosa
from os import listdir

class Audio_reader(): 
    #TODO: add check for already downloaded files 
    def __init__(self, paylist_url: str) -> None:
        print("audio zen") 
        self.playlist = Playlist(paylist_url)
        self.path  = './downloaded_videos'
        self.sample_rate = None #use native sample rate

    def download_paylist_videos(self): 
        print(f"Downloading playlist '{self.playlist.title}' audios:")
        for url in self.playlist.video_urls[:3]:
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

    def audio_preprosessing(self): 

        for filename in listdir(self.path):
            print(filename)

        #TODO: break up audio into 10min chunks 
        audio, _ = librosa.load(filename, sr=self.sample_rate, mono=True)
        audio = audio.reshape(-1, 1)
        # yield audio, filename, category_id