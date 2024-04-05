from tkinter import *

# Create the window itself
window = Tk()
window.title("Window With Alot of Features")
window.minsize(width=500, height=500)

# Create labels
label = Label(text="First version text")
label.grid(column=0, row=0)


# Button clicked - what we going to do when button is clicked
def clicked():
    clicked_text = text.get("1.0", END)
    print(clicked_text)


button = Button(text='Click me', command=clicked)
# button.pack()  # pack = show !!!
button.grid(column=1, row=1)
# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
# entry.pack()
entry.grid(column=2, row=2)

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Write something here. & then click the button")
# if the user write something in the box and clicking - the sentece he wrote will be printed

text.grid(column=3, row=3)


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
spinbox.grid(column=4, row=4)


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()
checkbutton.grid(column=5, row=5)
window.mainloop()
