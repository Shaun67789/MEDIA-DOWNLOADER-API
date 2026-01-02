import os, time, threading
from config import DOWNLOAD_FOLDER

def cleaner():
    while True:
        for f in os.listdir(DOWNLOAD_FOLDER):
            p = os.path.join(DOWNLOAD_FOLDER,f)
            if time.time() - os.path.getmtime(p) > 300:
                try: os.remove(p)
                except: pass
        time.sleep(60)

def start_cleaner():
    threading.Thread(target=cleaner, daemon=True).start()