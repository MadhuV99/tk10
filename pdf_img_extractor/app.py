# Create a GUI app with Tkinter - Step by Step Tutorial by Python Simplified (YouTube)
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import display_logo, display_textbox, display_icon, display_images, extract_images, copy_text, save_all, save_image

#global parameters, updating dynamically
all_content = []
all_images = []
img_idx = [0]
displayed_img = []

root = Tk()
root.geometry('+%d+%d'%(350,10)) #place GUI at x=350, y=10

#ARROW BUTTONS FUNCTIONALITY
#right arrow
def right_arrow(all_images, selected_img, what_text):
    pass


#left arrow
def left_arrow(all_images, selected_img, what_text):
    pass


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        #page_content = page_content.encode('cp1252')
        page_content = page_content.replace('\u2122', "'")

        #BEGIN EXTRACTING
        #extract text
        all_content.append(page_content)
        #extract images
        images = extract_images(page)
        for img in images:
            all_images.append(img)

        #BEGIN DISPLAYING
        #display the first image that was detected
        selected_image = display_images(images[img_idx[-1]])
        displayed_img.append(selected_image)

        #show text box on row 4 col 0
        display_textbox(page_content, 4, 0, root)

        #reset the button text back to Browse
        browse_text.set("Browse")

        #BEGIN MENUES AND MENU WIDGETS
        #1.image menu on row 2
        img_menu = Frame(root, width=800, height=60)
        img_menu.grid(columnspan=3, rowspan=1, row=2)

        what_text = StringVar()
        what_img = Label(root, textvariable=what_text, font=("shanti", 10))
        what_text.set("image " + str(img_idx[-1] + 1) + " out of " + str(len(all_images)))
        what_img.grid(row=2, column=1)

        #arrow buttons
        display_icon('arrow_l.png', 2, 0, E, lambda:left_arrow(all_images, selected_image, what_text), root)
        display_icon('arrow_r.png', 2, 2, W, lambda:right_arrow(all_images, selected_image, what_text), root)


        #create action buttons
        copyText_btn = Button(root, text="copy text",command=lambda:copy_text(all_content, root), font=("shanti", 10), height=1, width=15)
        saveAll_btn = Button(root, text="save all images", command=lambda:save_all(all_images), font=("shanti", 10), height=1, width=15)
        save_btn = Button(root, text="save image", command=lambda:save_image(all_images[img_idx[-1]]), font=("shanti", 10), height=1, width=15)

        #place buttons on grid
        copyText_btn.grid(row=3,column=0)
        saveAll_btn.grid(row=3,column=1)
        save_btn.grid(row=3,column=2)

#header area - logo & browse button
header = Frame(root, width=800, height=175, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

#main content area - text and image extraction
main_content = Frame(root, width=800, height=250, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=4)


#BEGIN INITIAL APP COMPONENTS
display_logo('logo.png', 0, 0, root)

#instructions
instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

#browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda:open_file(), font=("Raleway",12), bg="#20bebe", fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)


root.mainloop()