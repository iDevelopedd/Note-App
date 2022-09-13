# Imports the modules needed
from tkinter import *
from tkinter import filedialog
import webbrowser
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
root.config(background="#19191a")

# Sets the variable for an opened file
global opened_file
opened_file = False

# Adds a text editor to the root with the text label "Text Editor"
text_label = Label(root, text="Text Editor", bg="#303030", fg=figma_white, font=(inter_bold, 14))
text_label.pack(padx=5, pady=10)
user_text = Text(root, bg="#ffffff", fg="black", font=(inter_regular), relief="flat", height=15, width=90)
user_text.pack()

# Adds the textbox to the root giving it the name "URL" and sets a placeholder for the urls
user_url_label = Label(root, text="URL", bg="#303030", fg=figma_white, font=(inter_bold, 14))
user_url_label.pack(padx=0, pady=10)
user_url = Text(root, bg="#ffffff", fg="black", font=(inter_regular), relief="flat", height=1, width=50)
user_url.pack()
user_url.insert("1.0", "http://www.")

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
    root.filename = filedialog.askopenfilename(filetype=([("Text", "*.txt"), ("Any File", "*.*")]))

    if root.filename:
        global opened_file
        opened_file = root.filename
        user_text.delete("1.0", END)
        filename = open(root.filename, 'r')
        content = filename.read()
        user_text.insert(END, content)
        filename.close()

    # Checks if it is a url link
    if root.filename:
        # global opened_file
        opened_url_file = root.filename
        # user_url.delete("1.0", END)
        filename = open(opened_url_file, 'r')
        content = filename.read()
        user_url.insert(END, content)
        filename.close()
        
# Saves a file as a specific name
def saveAsButton():
    filename = filedialog.asksaveasfile(defaultextension=".txt", mode="w",filetype=(("Text", "*.txt"), ("Any File", "*.*")))
    if filename:
        content = user_text.get("1.0", END)
        filename.write(content)
        filename.close()

# Saves the current file
def saveText():
    global opened_file
    if opened_file:
        filename = open(opened_file, "w")
        filename.write(user_text.get("1.0", END))
        filename.close()
    else:
        saveAsButton()

# This will clear the text of the text editor 
def clearText():
    user_text.delete("1.0", END)

# This will save the current file
def saveLink():
    global opened_file
    if opened_file:
        filename = open(opened_file, "w")
        filename.write(user_url.get("1.0", END))
        filename.close()
    else:
        saveAsLink()

# This will save a specific link as a .txt
def saveAsLink():
    filename = filedialog.asksaveasfile(defaultextension=".txt", mode='w', filetypes=([("Text File", "*.txt"), ("Any File", "*.*")]))
    if filename:
        savedURL = user_url.get("1.0", END)
        filename.write(savedURL)
        filename.close

# This function will open a web browser and 
# search the url from the textbox
def gotoLink():
    getURL = user_url.get("1.0", END)
    webbrowser.open(getURL)

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

# Creates the textMenu and adds the text item
textMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Text", menu=textMenu)
textMenu.add_command(label="Save Text", command=saveText)
textMenu.add_command(label="Clear Text", command=clearText)

# Creates the imageMenu then add image items
imageMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Image", menu=imageMenu)
imageMenu.add_command(label="Add Image", command=addImage)

# Creates the linkMenu then adds link items 
linkMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Link", menu=linkMenu)
linkMenu.add_command(label="Save", command=saveLink)
linkMenu.add_command(label="Save As", command=saveAsLink)
linkMenu.add_command(label="Go to Link", command=gotoLink)

# Ends the application
root.mainloop() # !!IMPORTANT If its not include the application will not run

# Resources we've used: Codemy.com and Bro Code on youtube