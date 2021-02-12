#Morse Code Translator
#Icon found from http://icons8.com
import tkinter
from tkinter import IntVar, END, DISABLED, NORMAL
from playsound import playsound
from PIL import ImageTk, Image

#Define window
root = tkinter.Tk()
root.title('Morse Code Translator')
root.iconbitmap('morse.ico')
root.geometry('500x350')
root.resizable(0,0)

#Define fonts colors
button_font = ('SimSun', 10)
root_color = "#778899"
frame_color = "#dcdcdc"
button_color = "#c0c0c0"
text_color = "#f8f8ff"
root.config(bg=root_color)

#Define funtions 
