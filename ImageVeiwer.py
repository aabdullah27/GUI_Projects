
from tkinter import *
from PIL import ImageTk, Image

# Function to update the image
def update_image(index):
    global Label_1
    Label_1.place_forget()  # Remove the current image
    Label_1 = Label(image=img_list[index])
    img_width = img_list[index].width()
    img_height = img_list[index].height()
    x = (root.winfo_width() - img_width) // 2
    y = (root.winfo_height() - img_height) // 2
    Label_1.place(x=x, y=y)

# Functions for the buttons
def forward():
    global img_index
    img_index = (img_index + 1) % len(img_list)
    update_image(img_index)

def backward():
    global img_index
    img_index = (img_index - 1) % len(img_list)
    update_image(img_index)

# Making the main window
root = Tk()
root.title('Image Viewer')
root.state('zoomed')

# Using images and assigning them variables
my_image1 = ImageTk.PhotoImage(Image.open('Images/1.jpg'))
my_image2 = ImageTk.PhotoImage(Image.open('Images/2.jpg'))
my_image3 = ImageTk.PhotoImage(Image.open('Images/3.jpg'))

# Making a list so that we can iterate through images in the image viewer
img_list = [my_image1, my_image2, my_image3]
img_index = 0

# Making buttons
forward_button = Button(root, padx=20, pady=20, text='>', font='bold', command=forward, bg = 'black', fg= 'white')
backward_button = Button(root, padx=20, pady=20, text='<', font='bold', command=backward, bg = 'black', fg= 'white')
exit_button = Button(root, width=6, fg='white', bg='red', font='bold', text='EXIT', command=root.quit)

# Making Labels
Label_1 = Label(image=img_list[img_index])
update_image(img_index)

# Placing the buttons
backward_button.place(x=0, y=350)
forward_button.place(x=1379, y=350)
exit_button.place(x=1375, y=842)

if __name__ == '__main__':
    root.mainloop()
