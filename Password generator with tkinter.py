from tkinter import *
import random
import string

root = Tk()
#Naming the window
root.title('Password Generator')
#Setting the size of the window
root.geometry("500x500")



def new_pass():
    #get the length of the password from entryBox
    lengthOfPassword = int(entryBox.get())
    the_password = ''
    #Get the characters
    upper = string.ascii_uppercase
    num = string.digits
    lower = string.ascii_lowercase
    hexdigits = string.hexdigits
    #concatenate characters together
    password = upper + num + lower + hexdigits 
    temp = random.sample(password,lengthOfPassword)
    #Join the password with empty string
    password = the_password.join(temp)
    #Output password to screen
    passwordBox.insert(0,password)
#Copy created password to clipboard
def clipboard():
    root.clipboard_clear()
    root.clipboard_append(passwordBox.get())


#create frame for input box
labelFrame = LabelFrame(root, text  = 'How Many Characters')
labelFrame.pack(pady=20)

entryBox = Entry(labelFrame, font = ("Helvetica", 24))
entryBox.pack(pady=20,padx=20)

#create the frame for the password box
passwordBoxFrame = LabelFrame(root, text = 'Generated Password')
passwordBoxFrame.pack(pady=20, padx=20)
#create the box where the password appears
passwordBox = Entry(passwordBoxFrame, font = ("Helvetica", 24))
passwordBox.pack(pady=20, padx=20)


#Create a frame for the buttons
buttonFrame = Frame(root)
buttonFrame.pack(pady=20)


#create the buttons
passwordButton = Button(buttonFrame, text = "Create Password", command = new_pass)
passwordButton.grid(row=0,column=0,padx=10)

clipboardButton = Button(buttonFrame, text = "Copy to Clipboard", command = clipboard)
clipboardButton.grid(row=0, column=1,padx=10)






root.mainloop()
