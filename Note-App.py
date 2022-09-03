# Import the Tkinter library
from tkinter import *

# Set the root of the application
root = Tk()

root.title('Note-App')
root.geometry("500x500")
root.config(background="#D9D9D9")

# Fonts and color scheme
inter_bold =  'Inter-Bold'
inter_regular =  'Inter-Regular'
figma_white = '#D9D9D9'

# Remove title bar
root.overrideredirect(True)

# Function for quitting the app
def quit_app(e):
    root.quit()

# Title bar
title_bar = Frame(root, bg=figma_white, relief="flat")
title_bar.pack(fill=X)

# Title bar line
title_line = Frame(root, bg="black", relief="flat")
title_line.pack(expand=0, fill=X)

# Function for moving the app
def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

# Bind the title bar (B1 is the left mouse button <B1-Motion> and motion means that it will print the position of the moving mouse pointer)
title_bar.bind("<B1-Motion>", move_app)

# Custom title bar
title_label = Label(title_bar, text="Note-App", background=figma_white, font=(inter_bold, 14), fg="black", bd=1)
title_label.pack(side=LEFT, padx=50, pady=5)

# Exit button for title bar
close_label = Label(title_bar, text="X", bg=figma_white, fg="black", font=(inter_bold, 20))
close_label.pack(side=RIGHT, padx=5)
close_label.bind("<Button-1>", quit_app)

# App Loop IMPORTANT!!!
root.mainloop()

