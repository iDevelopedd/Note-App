# Imports the modules needed
from fileinput import filename
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

# Fonts and color scheme
inter_bold = 'Inter-Bold'
inter_regular = 'Inter-Regular'
figma_white = '#D9D9D9'

# Sets the root level of the application
root = Tk()

# Configures the title, resoultion, icon image and background color
root.title("Note-App")
root.geometry("500x500")
root.iconbitmap("Images\Icon.ico")
root.config(background="#D9D9D9")

# Sets the menubar to the root window
menubar = Menu(root)
root.config(menu=menubar)

# Opens a file
def openButton():

    filepath = filedialog.askopenfilename()
    file = open(filepath,'r')
    textcontent = file.read()

    if filepath == filedialog.askopenfilename(filetype=[("any", "*.txt")]):
        print("Txt file detected")

    # user_text.insert(END, textfile)
    file.close()

# Saves the content of the current file
def saveButton():
    filepath = filedialog.askopenfilename()
    textFile = open(filepath, 'w')
    # textFile.write(user_text.get(1.0, END))

# Opens the setings window
# def settingsButton():
#     print("Settings window opened")

# Creates the file menu on the menubar and the items within that menu
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openButton)
fileMenu.add_command(label="Save", command=saveButton)
# fileMenu.add_command(label="Settings", command=settingsButton)
fileMenu.add_command(label="Quit", command=root.quit)

# Creates the add text

def textButton():

    top = Toplevel()
    top.resizable(False, False)
    top.title("Text")
    top.iconbitmap("Image\Icon.ico")

    text = Text(top, height=15, width=90)
    text.pack()

    top.mainloop()
    


textMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Text", menu=textMenu)
textMenu.add_command(label="Add Text", command = textButton)



# Opens a filedialog so that the user can select which one to import
def imageButton():
    global image
    root.filename = filedialog.askopenfilename(title="Select Image", 
    filetype=[(" ", "*.png"), ("any", "*.*")])

    top = Toplevel()
    top.title("Image")
    top.geometry("300x300")
    top.iconbitmap("Images\Icon.ico")

    canvas=Canvas(top)
    image = Image.open(root.filename)
    image = image.resize((900, 700), resample=1)
    image = ImageTk.PhotoImage(image)
    canvas.create_image(0,0,image=image)
    canvas.pack()

    top.mainloop()
    
    
# Creates the imageMenu the add image item
imageMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Image", menu=imageMenu)
imageMenu.add_command(label="Add Image", command=imageButton)

# Creates the add link 

def linkButton():
    top = Toplevel()
    top.resizable(False, False)
    top.title("Link")
    top.iconbitmap("Image\Icon.ico")

    text = Text(top, height=15, width=90)
    text.pack(pady=20)

    top.mainloop()

linkMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Link", menu=linkMenu)
linkMenu.add_command(label="Add Link", command = linkButton)

root.mainloop()


