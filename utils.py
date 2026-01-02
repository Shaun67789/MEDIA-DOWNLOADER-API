import os

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def format_size(n):
    for u in ["B","KB","MB","GB"]:
        if n < 1024:
            return f"{round(n,2)} {u}"
        n /= 1024