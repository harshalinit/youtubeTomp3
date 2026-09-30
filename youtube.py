import os
import yt_dlp


DOWNLOAD_FOLDER = "D:\youtubeTomp3"


def download(url):
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
        "restrictfilenames": True,
        "windowsfilenames": True,
        "noplaylist": True,
        "writethumbnail": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {
                "key": "FFmpegMetadata",
            },
            {
                "key": "EmbedThumbnail",
            },
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()

    if not url:
        print("URL cannot be empty.")
    else:
        download(url)
        print("Download complete.")