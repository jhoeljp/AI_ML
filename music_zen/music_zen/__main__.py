
from audio_zen import Audio_zen
from pytube import YouTube

def run(): 
    audio_playlist = 'https://youtube.com/playlist?list=PLHXu9v3Y_fKkS7ljYOGo_0y9FhI2fI-ZS&si=YC1WohT3QanHFRDz'
    obj = Audio_zen(paylist_url=audio_playlist)
    obj.download_paylist_videos()

if __name__ == "__main__":
    run()