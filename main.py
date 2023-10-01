from pytube import YouTube

SAVE_PATH = "Your path"

def on_progress(video_stream, total_size, bytes_remaining):
    total_size = video_stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')


link = input("Paste the link of the video you want to download: ")
yt = YouTube(link, use_oauth=False, allow_oauth_cache=True, on_progress_callback=on_progress)
stream = yt.streams.get_by_itag(22) # Example itag for 720p MP4, you can change it to your desired format.
confirm = input(f"Are you sure you want to download {yt.title}? (y/n) ")


if confirm.lower() == "y":
    print(f"Downloading {yt.title}...")
    stream.download(output_path=SAVE_PATH)
    print(f"Video downloaded succesfully to {SAVE_PATH}")
if confirm.lower() == "n":
    exit()

