from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
import tkinter as tk
from moviepy.editor import * 
import os

root = tk.Tk()
root.geometry("550x400")
root.resizable(True, True)
root.title("MP4 to MP3 converter")
root.config(background="black")

def widgets():

    head_label = Label (root, text="Converter", 
    padx=15, pady=15,
    font="SegoeUI 14", 
    bg="black", fg="white")

    head_label.grid(row=1, column=3, 
                        pady=10, padx=5, columnspan=2)

    auswahl_label = Label(root, text="Titel :", 
                        bg="black", fg="white", 
                        pady=5, padx=9)
    
    auswahl_label.grid(row=2, column=0, 
                        pady=5, padx=5, 
                        columnspan=2)

    root.auswahlText=Entry(root, width=50,
                        textvariable=file, font="Arial 14")

    root.auswahlText.grid(row=2, column=3, 
                        pady=5, padx=5)

    auswahl_B = Button(root, text="Auswahl", 
                        command=Auswahl, width=10, 
                        bg="bisque", relief=GROOVE)

    auswahl_B.grid(row=2, column=5, pady=1, padx=1)

    convert_B = Button(root, text="Convert", 
                        command=Umwandlung, width=20, 
                        bg="thistle1", pady=10, padx=15, 
                        relief=GROOVE, font="Georgia, 13")

    convert_B.grid(row=4, column=3, 
                        pady=20, padx=20)

def Auswahl():
    tk.Tk().withdraw() 
    global conv_dir
    global x
    conv_dir=filedialog.askopenfilenames(title="Auswahl", initialdir='C:\\Users\\Patrik Jelic\\Music\\Python')
    file.set(conv_dir)
    
    #global file 
    #file = conv_dir 
    x = len(conv_dir)

def Umwandlung():
    for n in range(0,x):
        name = conv_dir[n]
        name2 = name.replace('/', os.sep)
        name3=os.path.splitext(name2)[0]+'.mp3'        
        mp4_file=name2
        mp3_file=name3
        video=VideoFileClip(mp4_file)
        audio=video.audio
        audio.write_audiofile(mp3_file)
        audio.close()
        video.close()
    
file=StringVar()

widgets()

root.mainloop()
