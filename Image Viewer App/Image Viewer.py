"""
Sujan Koirala, Instisute of Engineering, Pulchowk
##
This is a simple image viewer app  made using Tkinter.
"""

from tkinter import *
from PIL import ImageTk, Image

index = 3  # Default index
root = Tk()
root.title("Image viewer App")
# Back button operation
def back():
    forwardButton.config(state = ACTIVE)
    backButton.config(state = ACTIVE)
    global index 
    global myLabel
    if (index <= 1 ):
        index = index
        backButton.config(state = DISABLED) # Disabling back effect for first image
    index = index - 1
    myLabel.config(image=myImage[index])

# Forward button operation
def forward():
    forwardButton.config(state = ACTIVE)
    backButton.config(state = ACTIVE)
    global index
    global myLabel
    if (index== len(list) - 2 ):
        index = index
        forwardButton.config(state = DISABLED) # Disabling forward effect for last image
    index = index + 1
    myLabel.config(image=myImage[index])

# Image related stuff
list = ['itachi.jpg', 'naruto.jpg', 'sasuke.jpg', 'uta.jpg', 'pain.jpg', 'shanks.jpg', 'zoro.jpg', 'senku.jpg']  #Lists of images name
myImage = []
i = 0
while i < len(list):
    myImage.append(ImageTk.PhotoImage(Image.open(f"images/{list[i]}"))) # Adding element to empty list
    i += 1
myLabel = Label(image= myImage[index], anchor= CENTER)
myLabel.grid(row = 1, column = 1 )

# Defining and positioning buttons
backButton = Button(root, text= "<<", command = back)
backButton.grid(row = 1,column = 0)
forwardButton = Button(root, text= ">>", command = forward)
forwardButton.grid(row = 1,column = 2)
exitButton = Button(root, text = "Exit", command = root.quit)
exitButton.grid(row = 2, column = 1)

root.mainloop()