# Import the Tkinter library
from tkinter import *

############################################# Start of the application #####################
# Set the root of the application
root = Tk()

root.title('Note-App')
root.geometry("500x70")
root.config(background="#D9D9D9")

############################################# Setting up the variables and files we need #####################
# Fonts and color scheme
inter_bold = 'Inter-Bold'
inter_regular = 'Inter-Regular'
figma_white = '#D9D9D9'

# Image importer for the minimize, maximize and exit buttons
exit_button = PhotoImage(file = r"Images\ExitButton.png")
minimize_button = PhotoImage(file = r"Images\Minimize.png")
maximize_button = PhotoImage(file= r"Images\Maximize.png")

# Resizes the images
exit_button_image = exit_button.subsample(2, 2)
minimize_button_image = minimize_button.subsample(2, 2)
maximize_button_image = maximize_button.subsample(2, 2)

###################################### Removing and creating a custom app ################################################

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

# Function to get the current position of the mouse pointer on the screen
def get_pos(e):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = e.x_root
    starty = e.y_root

    ywin -= starty
    xwin -= startx

    # Function to move the app window to the mouse pointer
    def move_app(e):
        root.geometry('+{0}+{1}'.format(e.x_root + xwin, e.y_root + ywin))

    # Bind the title bar (B1 is the left mouse button <B1-Motion> and motion means that it will print the position of the moving mouse pointer)
    title_bar.bind("<B1-Motion>", move_app)
# Binds the left mouse button to the position of the window
title_bar.bind("<Button-1>", get_pos)

# Function for minimizing the app
def minimize_app(e):
    root.update_idletasks()
    root.overrideredirect(False)
    root.state('iconic')

# Function for reminizing the app
def reminimize_app(e):
    root.update_idletasks()
    root.overrideredirect(True)
    root.state('normal')

# Binds the titlebar so it reminimize the app
title_bar.bind("<Map>", reminimize_app)

# Custom title bar
title_label = Label(title_bar, text="Note-App", background="black", font=(inter_bold, 14), fg=figma_white)
title_label.pack(side=LEFT, padx=50)

############################################# Feature Buttons ###########################################################

# Text Button
title_text = Button(title_bar, text="Text", background="black", font=(inter_regular, 10), fg=figma_white, relief="flat")
title_text.pack(side=LEFT)

# Audio Button
title_audio = Button(title_bar, text="Audio", background="black", font=(inter_regular, 10), fg=figma_white, relief="flat")
title_audio.pack(side=LEFT)

# Image Button
title_image = Button(title_bar, text="Image", background="black", font=(inter_regular, 10), fg=figma_white, relief="flat")
title_image.pack(side=LEFT)

# Link Button
title_link = Button(title_bar, text="Link", background="black", font=(inter_regular, 10), fg=figma_white, relief="flat")
title_link.pack(side=LEFT)

############################################## Minimize, Maximize, Exit Buttons ########################################

# Exit button
close_label = Label(title_bar, image = exit_button_image, bg=figma_white, fg="black", font=(inter_bold, 20))
close_label.pack(side=RIGHT, ipadx=5, ipady=5)
close_label.bind("<Button-1>", quit_app)

# Maximize Button
close_label = Label(title_bar, image = maximize_button_image, bg=figma_white, fg="black", font=(inter_bold, 20))
close_label.pack(side=RIGHT, ipadx=5, ipady=5)
# close_label.bind("<Button-1>", quit_app)

# Minimize Button
close_label = Label(title_bar, image = minimize_button_image, bg=figma_white, fg="black", font=(inter_bold, 20))
close_label.pack(side=RIGHT, ipadx=5, ipady=5)
close_label.bind("<Button-1>", minimize_app)
############################################# End of the application #######################################
# App Loop IMPORTANT!!!
root.mainloop()

