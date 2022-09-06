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
settings_button = PhotoImage(file = r"Images\Settings.png")
exit_button = PhotoImage(file = r"Images\ExitButton.png")
minimize_button = PhotoImage(file = r"Images\Minimize.png")
# maximize_button = PhotoImage(file= r"Images\Maximize.png") !!NOT SURE IF WE WANT TO ADD YET

# Resizes the images
settings_button_image = settings_button.subsample(2, 2)
exit_button_image = exit_button.subsample(2, 2)
minimize_button_image = minimize_button.subsample(2, 2)
# maximize_button_image = maximize_button.subsample(2, 2) !!NOT SURE IF WE WANT TO ADD YET

###################################### Removing and creating a custom app ################################################

# Remove title bar
root.overrideredirect(True)

# Function for quitting the app
def quit_app(e):
    root.quit()

# Title bar
title_bar = Frame(root, bg=figma_white, relief="flat")
title_bar.pack(fill=X, pady=5)

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

    # Function for the app window to the mouse pointer
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
title_label = Label(title_bar, text="Note-App", background=figma_white, font=(inter_bold, 16), fg="black")
title_label.grid(row=0, column=1, columnspan=3, sticky=SW)

############################################# Feature Buttons ###########################################################

# Settings Button
title_setting = Button(title_bar, image = settings_button_image, background=figma_white, relief="flat")
title_setting.grid(row=0, column=0, rowspan=3, padx=20)

# Text Button
title_text = Button(title_bar, text="Text", background=figma_white, font=(inter_regular, 10), fg="black", relief="flat")
title_text.grid(row=1, column=1, sticky=NW)

# Audio Button
title_audio = Button(title_bar, text="Audio", background=figma_white, font=(inter_regular, 10), fg="black", relief="flat")
title_audio.grid(row=1, column=2)

# Image Button
title_image = Button(title_bar, text="Image", background=figma_white, font=(inter_regular, 10), fg="black", relief="flat")
title_image.grid(row=1, column=3)

# Link Button
title_link = Button(title_bar, text="Link", background=figma_white, font=(inter_regular, 10), fg="black", relief="flat")
title_link.grid(row=1, column=4)

############################################## Minimize, Maximize, Exit Buttons ########################################

# Exit button
close_label = Label(title_bar, image = exit_button_image, bg=figma_white, fg="black", font=(inter_bold, 20))
close_label.grid(row=0, column=7, padx=5, sticky=SE)
close_label.bind("<Button-1>", quit_app)

# Maximize Button
# max_label = Label(title_bar, image = maximize_button_image, bg=figma_white, fg="black", font=(inter_bold, 20))
# max_label.grid(row=0, column=6, padx=5, sticky=S)
# # max_label.bind("<Button-1>", maximize_app)

# Minimize Button
min_label = Label(title_bar, image = minimize_button_image, bg=figma_white, fg="black", font=(inter_bold, 20))
min_label.grid(row=0, column=5, padx=5, sticky=S)
min_label.bind("<Button-1>", minimize_app)

############################################# End of the application #######################################
# App Loop IMPORTANT!!!
root.mainloop()
