from tkinter import *
import tkinter
import os
import PyPDF2
from PIL import *
from tkinter.filedialog import askopenfile

root = tkinter.Tk()
root.title('OpenPDF')

canvas = tkinter.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#istrucctions
instructions = tkinter.Label(root, text='SELECT YOUR PDF TO GET CONTENTS')
instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    select_text.set("Loading....")
    file = askopenfile(parent=root, mode='rb', title="choose a File", filetypes=[("Pdf file", "*.pdf")])
    if file:
        #display pdf to text
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        #text box
        text_box = tkinter.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)
        
        #changing the select button back to select instead of loading
        select_text.set("SELECT")
        
#button for selecting
select_text = tkinter.StringVar()
select_btn = tkinter.Button(root, textvariable=select_text, command=lambda:open_file(), bg="green", fg="white", height=2, width=15)
select_text.set("SELECT")
select_btn.grid(columnspan=3, column=0, row=2)



canvas = tkinter.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()