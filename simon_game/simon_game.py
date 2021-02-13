#Simon Memory Game
import tkinter
from tkinter import StringVar, ACTIVE, NORMAL, DISABLED
import random

#Define window
root = tkinter.Tk()
root.title('Simon Memory Game')
root.iconbitmap('simon.ico')
root.geometry('400x400')
root.resizable(0,0)

#Define fonts and colors
game_font1 = ('Arial', 12)
game_font2 = ('Arial', 8)
white = "#c6cbcd"
white_light = "#fbfcfc"
magenta = "#90189e"
magenta_light = "#f802f9"
cyan = "#078384"
cyan_light = "#00fafa"
yellow = "#9ba00f"
yellow_light = "#f7f801"
root_color = "#2eb4c6"
game_color = "#f6f7f8"
root.config(bg=root_color)
