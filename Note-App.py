from tkinter import *

# Fonts and color scheme
inter_bold = 'Inter-Bold'
inter_regular = 'Inter-Regular'
figma_white = '#D9D9D9'

# Sets the root of the application
root = Tk()

# Configures the title, resoultion, icon image and background color
root.title("Note-App")
root.geometry("500x500")
root.iconbitmap("Images\Icon.ico")
root.config(background="#D9D9D9")

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
textMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Text", menu=textMenu)
textMenu.add_command(label="Add Text")

# Creates the add image menu
imageMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Image", menu=imageMenu)
imageMenu.add_command(label="Add Image")

# Creates the add link 
linkMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Link", menu=linkMenu)
linkMenu.add_command(label="Add Link")

# End of the application
root.mainloop() # !!IMPORTANT
