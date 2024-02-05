
from audio_reader import Audio_reader
from pytube import YouTube

def run(): 
    audio_playlist = 'https://youtube.com/playlist?list=PLHXu9v3Y_fKkS7ljYOGo_0y9FhI2fI-ZS&si=YC1WohT3QanHFRDz'
    obj = Audio_reader(paylist_url=audio_playlist)
    # obj.download_paylist_videos()
    obj.audio_preprosessing()

if __name__ == "__main__":
    run()