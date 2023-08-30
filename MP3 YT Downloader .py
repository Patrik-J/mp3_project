import os
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
import tkinter as tk
from moviepy.editor import *

root = tk.Tk()
root.geometry("1280x720")
root.resizable(True, True)
root.title("Smart Music")
root.config(background="lightcyan2")

def Widgets():
    ueberschrift = Label (root, text="MP3 Youtube Downloader",
                          padx=15, pady=15, font="SegoeUI 14",
                          bg="lightcyan2", fg="darkslategrey")
    ueberschrift.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

    ytvideolink = Label(root, text="Youtubelink : ", bg="lightcyan2", 
                        fg="darkslategrey", pady=5, padx=9)
    ytvideolink.grid(row=2, column=0, pady=5, padx=5)

    root.videourl = Entry(root, width=60, textvariable=video_link, font="SegoeUI 14")
    root.videourl.grid(row=2, column=1, pady=5, padx=5)    

    speicherort = Label(root, text="Speicherort :", bg="lightcyan2",
                        fg="darkslategrey", pady=5, padx=9)
    speicherort.grid(row=3, column=0, pady=5, padx=5)

    root.speicherordner = Entry(root, width=60, textvariable=download_path,
                                font="SegoeUI 14")
    root.speicherordner.grid(row=3, column=1, pady=5, padx=5)

    durchsuchen = Button(root, text="Durchsuchen", command=Browse,
                         width=10, bg="lightcyan1", relief=GROOVE)
    durchsuchen.grid(row=3, column=2, pady=1, padx=1)

    download = Button(root, text="Download", command=Download,
                      width=10, bg="lightcyan1", relief=GROOVE)
    download.grid(row=2, column=2, pady=1, padx=1)

def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH",
        title="Save Video")
    download_path.set(download_Directory)

def Download():
    YouTube_link = video_link.get()
    download_Folder = download_path.get()
    if YouTube_link == "":
        messagebox.showerror("NO URL GIVEN")
        return
    if download_Folder == "":
        messagebox.showerror("SELECT FILE DESTINATION")
        return
    yt = YouTube(YouTube_link)
    #video = yt.streams.first()
    #video.download()
    sound = yt.streams.filter(only_audio=True).first()
    out_file = sound.download(output_path=download_Folder)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    messagebox.showinfo("SUCCESSFULLY",
                       "DOWNLOADED AND SAVED IN\n"
                       + download_Folder)

download_path = StringVar()
video_link = StringVar()
Widgets()
root.mainloop()