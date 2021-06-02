import os
import shutil

images = ['jpg', 'png', 'jpeg', 'gif', 'webp', 'tiff', 'svg']
audio = ['mp3', 'wav', 'fxp', 'alp', ]
docs = ['doc', 'docx', 'txt', 'rtf', 'ait']
damages = ['dmg', 'zip', 'iso', 'exe']
videos = ['mp4', 'avi', 'webm']
pdf = ['pdf']

files = os.listdir('./')

while True:
    for file in files:
        if os.path.isfile(file) and file != 'Organize.py':
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

# Process 38890
