import tkinter

window = tkinter.Tk()  # Window initialization
window.title("GUI Program")  # setting the title of the window
window.minsize(width=300, height=300)  # setting the size of the window

# inorder to show something on the window we will use a Label
first_lable = tkinter.Label(text='This is a lable', font=('Arial', 12, 'bold'))
first_lable.pack()  # suppose to show is ? yeap it did

first_lable["text"] = "This is a new Text"
first_lable.config(text="This is another way to write new text")


# *args is a way of a function get input as much it needs - will be shown in playground.py

def button_clicked():
    print('Ouch ! Stop clicking me so HARD ~')


# Buttons
new_button = tkinter.Button(text="You should probably click me", command=button_clicked) # no need the parenthesis at the end cause clicking on the button is calling the function and not us
new_button.pack() # Dont forget the pack
# instead of run in a while loop tkinter can listen always
# while True:


window.mainloop()  # This will be at the end
