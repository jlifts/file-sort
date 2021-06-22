import os
import shutil
import logging


# Logging Cron Job
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, 'Organize.log')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


def do_logging():
    logger.info("Executed")

# File Sorter Method


def sort():
    # Define file types
    images = ['jpg', 'png', 'jpeg', 'gif', 'webp', 'tiff', 'svg']
    audio = ['mp3', 'wav', 'fxp', 'alp', ]
    docs = ['doc', 'docx', 'txt', 'rtf', 'ait']
    damages = ['dmg', 'zip', 'iso', 'exe']
    videos = ['mp4', 'avi', 'webm']
    pdf = ['pdf']
    files = os.listdir('./')

    while True:
        for file in files:
            if os.path.isfile(file) and file != 'Organize.py' and file != 'Organize.log':
                ext = (file.split('.')[-1]).lower()

                if ext in images:
                    shutil.move(file, 'Images/'+file)
                elif ext in audio:
                    shutil.move(file, 'Music/'+file)
                elif ext in docs:
                    shutil.move(file, 'Documents/'+file)
                elif ext in pdf:
                    shutil.move(file, 'PDF/'+file)
                elif ext in damages:
                    shutil.move(file, 'DMGs-Zip-Iso/'+file)
                elif ext in videos:
                    shutil.move(file, 'Vidoes/'+file)
                else:
                    shutil.move(file, 'Other/'+file)


if __name__ == '__main__':
    do_logging()
    sort()
