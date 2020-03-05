from tkinter import *
import pygame
 
root = Tk()
root.title("emdr_audio")
root.geometry("208x50")
root.resizable(False, False)

###

b2 = Button(text="140", width=5, height=2)
 
def change():
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load('140.wav')
        pygame.mixer.music.play()
 
b2.config(command=change)
 
b2.pack()

b2.place(x=1, y=1)

###

b1 = Button(text="280", width=5, height=2)
 
def change():
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load('280.wav')
        pygame.mixer.music.play()
 
b1.config(command=change)
 
b1.pack()

b1.place(x=70, y=1)

###

b0 = Button(text="560", width=5, height=2)
 
def change():
    while True:
        pygame.mixer.init()
        pygame.mixer.music.load("560.wav")
        pygame.mixer.music.play()
 
b0.config(command=change)
 
b0.pack()

b0.place(x=139, y=1)
 
root.mainloop()

