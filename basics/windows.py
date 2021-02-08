# windows basics
import tkinter

#Define window
root = tkinter.Tk()
root.title('Windows Basics!')
root.iconbitmap('thinking.ico') # from www.iconarchive.com
root.geometry('300x700')
root.resizable(0, 0)
root.config(bg='blue')


#Second window
top = tkinter.Toplevel()
top.title('Second Window')
top.geometry('275x350+500+50')
top.config(bg='#123456')

#Run root window's main loop
root.mainloop()
