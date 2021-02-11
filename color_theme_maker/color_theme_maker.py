#Color Theme Maker
import tkinter
from tkinter import BOTH, IntVar, DISABLED, filedialog

#Define window
root = tkinter.Tk()
root.title('Color Theme Maker')
root.iconbitmap('color_wheel.ico')
root.geometry('450x500')
root.resizable(0,0)


#Define fonts and colors
#NONE:  Using system defaults

#Define functions

#Define Layout
input_frame = tkinter.LabelFrame(root, padx=5, pady=5)
output_frame = tkinter.LabelFrame(root, padx=5, pady=5)
input_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
output_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

#Run the root window's main loop
root.mainloop()
