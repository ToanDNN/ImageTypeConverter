from PIL import Image
import glob
import sys
from tkinter import *
from pytube import YouTube

print(sys.version)

def pngTojpg():
    print(glob.glob("*.png"))
    for file in glob.glob('*.png'):
        im = Image.open(file)
        rgb_img = im.convert('RGB')
        rgb_img.save(file.replace("png", "jpg"), quality=95)

def jpgTopng():
    print(glob.glob("*.jpg"))
    for file in glob.glob('*.jpg'):
        im = Image.open(file)
        rgb_img = im.convert('RGBA')
        rgb_img.save(file.replace("jpg", "png"), quality=95)

def on_complete(stream, filepath):
    print('download is done!')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
    print(progress_string)

#print("Enter:\n\t\"png\" -> png to jpg\n\t\"jpg\" -> jpg to png\n\t\"yt\" -> to download youtube video")
#usr_input = input("What do you want to convert?:")



url = input('YouTube Link: ')
dir = input('Enter directory to save to: ')
video_obj = YouTube(url, on_complete_callback=on_complete, on_progress_callback= on_progress)

print(f'title:\t{video_obj.title}')
print(f'length:\t{round(video_obj.length / 60,2)} minutes')
print(f'author:\t{video_obj.author}')

print('download: (b)est | (a)udio | (e)xit')
choice = input('choice: ')

match choice:
    case 'b':
        video_obj.streams.get_highest_resolution().download(dir)
    case 'a':
        video_obj.streams.get_audio_only().download(dir)
    case 'e':
        exit()
'''
if usr_input.lower() == "png":
    print("PNG")
    pngTojpg()
elif usr_input.lower() == "jpg":
    print("JPG")
    jpgTopng()
else:
    print("[Error unknown/unsupported file type]")
    exit()
'''