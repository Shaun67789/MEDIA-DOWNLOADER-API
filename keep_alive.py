import threading, time, requests

def keep_alive(url):
    while True:
        try: requests.get(url)
        except: pass
        time.sleep(480)

def start_keep_alive(url):
    threading.Thread(target=keep_alive, args=(url,), daemon=True).start()