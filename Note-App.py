from tkinter import *
import webbrowser

#<<<<<<< HEAD
#=======
############################################# Start of the application #####################
# Set the root of the application
# root = Tk()

# root.title('Note-App')
# root.geometry("500x69")
# root.config(background="#D9D9D9")

############################################# Setting up the variables and files we need #####################
#>>>>>>> d66094b9ae4c8ef8197af921d3b3a4a217284c43
# Fonts and color scheme
inter_bold = 'Inter-Bold'
inter_regular = 'Inter-Regular'
figma_white = '#D9D9D9'

# Sets the root of the application
root = Tk()

#<<<<<<< HEAD
# Configures the title, resoultion, icon image and background color
root.title("Note-App")
root.geometry("500x500")
root.iconbitmap("Images\Icon.ico")
root.config(background="#D9D9D9")
#>>>>>>> d66094b9ae4c8ef8197af921d3b3a4a217284c43

# Sets the menubar to the root window
menubar = Menu(root)
root.config(menu=menubar)

# Creates the file menu on the menubar
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Settings")
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


# Creates the add image menu
imageMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Image", menu=imageMenu)
imageMenu.add_command(label="Add Image")

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

# End of the application
root.mainloop() # !!IMPORTANT
