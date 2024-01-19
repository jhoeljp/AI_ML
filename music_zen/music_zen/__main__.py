
from audio_zen import Audio_zen

def run(): 
    url = "http://youtu.be/tdceTb3vsmk?list=PLHXu9v3Y_fKm78b0lWbn8jXRUpjh6rCNj"
    url2 = 'http://youtube.com/watch?v=2lAe1cqCOXo'
    obj = Audio_zen(urls = [url, url2])
    obj.download_yt_video()

if __name__ == "__main__":
    run()