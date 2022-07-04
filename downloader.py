from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
import tkinter as tk
from moviepy.editor import * 
#import os
#import webbrowser
#import webview
#from threading import Thread
#check = False 
root = tk.Tk()
root.geometry("550x400")
root.resizable(True, True)
root.title("YouTube Downloader")
root.config(background="black")

def Widgets():

 
    head_label = Label(root, text="YouTube Downloader",
                       padx=15,
                       pady=15,
                       font="SegoeUI 14",
                       bg="black",
                       fg="white")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)
 
    link_label = Label(root,
                       text="YouTube link :",
                       bg="black",
                       fg="white",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)
 
    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)
 
 
    destination_label = Label(root,
                              text="Speicherort :",
                              bg="black",
                              fg="white",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)
 
 
    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)
 
 
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)
 
    Download_B = Button(root,
                        text="Download",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)      

def Browse():
    
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")
    download_Path.set(download_Directory)
 
def Download():
 
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    yt = YouTube(Youtube_link)
   # videoStream = getVideo.streams.first()
    #yt.streams.filter(file_extension='mp4')
    yt.streams.get_highest_resolution().download(download_Folder) 
    messagebox.showinfo("SUCCESSFULLY",
                       "DOWNLOADED AND SAVED IN\n"
                       + download_Folder)


video_Link = StringVar()
download_Path = StringVar()

Widgets()


root.mainloop()
