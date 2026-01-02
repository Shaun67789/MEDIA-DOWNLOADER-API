from yt_dlp import YoutubeDL
from config import DOWNLOAD_FOLDER, BASE_URL
from utils import ensure_dir, format_size
import os

ensure_dir(DOWNLOAD_FOLDER)

def execute(payload: dict):
    url = payload["url"]

    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "format": payload.get("quality","best"),
        "writesubtitles": payload.get("subtitles",False),
        "writethumbnail": payload.get("thumbnail",False),
        "noplaylist": not payload.get("playlist",False)
    }

    if payload.get("mp3"):
        ydl_opts["format"] = "bestaudio"
        ydl_opts["postprocessors"] = [{
            "key":"FFmpegExtractAudio",
            "preferredcodec":"mp3",
            "preferredquality":"320"
        }]

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    file = ydl.prepare_filename(info)
    name = os.path.basename(file)

    return {
        "platform": info.get("extractor_key"),
        "title": info.get("title"),
        "uploader": info.get("uploader"),
        "duration": info.get("duration"),
        "filesize": format_size(info.get("filesize") or 0),
        "available_formats": [f.get("format_note") for f in info.get("formats",[]) if f.get("format_note")],
        "download_url": f"{BASE_URL}/file/{name}"
    }