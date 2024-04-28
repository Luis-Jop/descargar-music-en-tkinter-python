from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from pathlib import Path
from pytube import YouTube 
import os

import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()
window = Tk()
window.title("youtube dowloand")
window.geometry('736x414')
window.resizable(False, False)
window.config(bg="gray")

# CODIGO PARA COLOCAR EL FONDO 
image3 = Image.open("image.jpg")
img3 = ImageTk.PhotoImage(image3)
img=tkinter.Label(window,image=img3)
img.place(relwidth=1,relheight=1,anchor="nw")



Label(window, text=' youtube download', font='arial 20  ', bg="#282928",fg="#Fff").place(x=130,y=10) 
Label(window, text='INGRESE EL LINK DEL VIDEO ', font='arial 10  ', bg="#282928",fg="#Fff" ).place(x=160,y=130)


#BARRA DE ENTRADA DE LINK
link = StringVar()
linkenter= Entry(window, textvariable=link, width=50,  ).place(x=105,y=200)


  # DESCARGAR VIDEO DE YOUTUBE MP4
def download():
     path   = "Downloads"
 #Downloads, Documentos, Videos
     folder = "videoYT"
 #Directorio para almacenar las descargas
     url_Descargas = str(Path.home() / path)
     print(url_Descargas) #C:\Users\urian\Documentos
     print(Path.home()) #C:\Users\uria
  #download video 
     yt = YouTube(str(link.get()))
     yt.streams.get_highest_resolution().download(output_path=os.path.join(url_Descargas, folder))
     link.set("")
     messagebox.showinfo( "Video descargado correctamente",yt.title)

def audio():
     
        path   = "Downloads"
 #Downloads, Documentos, Videos
        folder = "MusicasYT"
 #Directorio para almacenar las descargas
        url_Descargas = str(Path.home() / path)
        print(url_Descargas) #C:\Users\urian\Documentos
        print(Path.home()) #C:\Users\uria

#Download mp3
        yt = YouTube(str(link.get()))
        audio_file = yt.streams.filter(only_audio=True).first().download(output_path=os.path.join(url_Descargas, folder))
        base, ext = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        os.rename(audio_file, new_file)
        link.set("")
        titulo=yt.title
        print(f"Titulo .........: {yt.title}")
        messagebox.showinfo("audio descargado correctamente",titulo)
        
    
         
Button(window,text='VIDEO DOWNLOAD', font='arial 13 bold italic', command=download, bg="#282928",fg="#Fff").place(x=50,y=300)
Button(window, text='AUDIO DOWNLOAD', font='arial 13 bold italic', command=audio, bg="#282928",fg="#Fff").place(x=300,y=300)
   



window.mainloop()