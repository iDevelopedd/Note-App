# Imports the modules needed
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

# Sets the fonts and color scheme we'll need
inter_bold = 'Inter-Bold'
inter_regular = 'Inter-Regular'
figma_white = '#D9D9D9'

# Sets the root level of the application
root = Tk()

# Configures the title, resoultion, icon image and background color
root.title("Note-App")
root.geometry("500x500")
root.iconbitmap("Images\Icon.ico")
root.config(background="#303030")

# Opens a filedialog so that the user can select 
# an image then it opens it in another window
def addImage():
    global image
    root.filename = filedialog.askopenfilename(title="Select Image", 
    filetype=[(" ", "*.png"), ("Any File", "*.*")])

    if root.filename:
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

# This will open the filedialog so that the user can select a file
# it will than delete anything that is in the text editor and insert the new content
def openButton():
    root.filepath = filedialog.askopenfilename(filetype=(("Text", "*.txt"), ("Any File", "*.*")))
    
    if root.filepath:
        user_text.delete("1.0", END)
        filepath = open(root.filepath, 'r')
        content = filepath.read()
        user_text.insert(END, content)
        filepath.close()
        
# Saves a file as a specific name
def saveAsButton():
    filename=filedialog.asksaveasfile(defaultextension=".txt", mode='w', filetypes=([("Text File", "*.txt"), ("Any File", "*.*")]))
    if filename:
        savedText = user_text.get("1.0", END)
        filename.write(savedText)
        filename.close

# Adds a text editor to the root with the text label "Text Editor"
text_label = Label(root, text="Text Editor", bg="#303030", fg=figma_white, font=(inter_bold, 15))
text_label.pack(padx=5, pady=10)
user_text = Text(root, bg="#595959", fg=figma_white, font=(inter_regular), relief="flat", height=15, width=90).pack()

# Adds the textbox to the root giving it the name "URL" and sets a placeholder for the urls
user_url_label = Label(root, text="URL", bg="#303030", fg=figma_white, font=(inter_bold, 15))
user_url_label.pack(padx=0, pady=10)
user_url = Text(root, bg="#595959", fg=figma_white, font=(inter_regular), relief="flat", height=1, width=50)
user_url.pack()
user_url.insert("1.0", "http://")

# Saves a file that has been opened
def saveText():
    user_text.delete("1.0", END)
    filepath = filedialog.askopenfilename(filetype=(("Text", "*.txt"), ("Any File", "*.*")))
    if filepath:
        content = user_text.get(1.0, END)
        filepath.write(content)
        filepath.close()

# This will clear the text of the text editor 
def clearText():
    user_text.delete("1.0", END)

# This will save a link as .txt file
def saveLink():
    filename=filedialog.asksaveasfile(defaultextension=".txt", mode='w', filetypes=([("Text File", "*.txt"), ("Any File", "*.*")]))
    savedURL = user_url.get("1.0", END)
    filename.write(savedURL)
    filename.close

def gotoLink():
    pass

# Sets the menubar to the root window
menubar = Menu(root)
root.config(menu=menubar)

# Creates the file menu on the menubar and the items within that menu
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openButton)
fileMenu.add_command(label="Save As", command=saveAsButton)
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=root.quit)

<<<<<<< HEAD
# Creates the textMenu and adds the text item
textMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Text", menu=textMenu)
textMenu.add_command(label="Save Text", command=saveText)
textMenu.add_command(label="Clear Text", command=clearText)
=======
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


>>>>>>> c035fd9ac4ccd8b8a77f8cc95a6e45a03e6de554

# Creates the imageMenu then add image items
imageMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Image", menu=imageMenu)
imageMenu.add_command(label="Add Image", command=addImage)

<<<<<<< HEAD
# Creates the linkMenu then adds link items 
linkMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Link", menu=linkMenu)
linkMenu.add_command(label="Save Link", command=saveLink)
linkMenu.add_command(label="Go to Link", command=gotoLink)

# Ends the application
root.mainloop() # !!IMPORTANT If its not include the application will not run


# Resources we've used: Codemy.com and Bro Code on youtube
=======
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


>>>>>>> c035fd9ac4ccd8b8a77f8cc95a6e45a03e6de554
