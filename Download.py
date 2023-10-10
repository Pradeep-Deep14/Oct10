from pytube import YouTube

def download(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("Download completed successfully.")
    except Exception as e:
        print("An error has occurred:", str(e))

link = input("Enter the YouTube video URL: ")
download(link)
