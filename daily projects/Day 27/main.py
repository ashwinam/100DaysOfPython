import tkinter

window = tkinter.Tk()
window.title("This is Tkinter Window")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)  # padding around the screen

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Ariel", 24, "bold"))
my_label.grid(column=0, row=0)  # it must for label to show on window

my_label["text"] = "Hello world"
my_label.config(text="New Text")

# Button


def clicked_fn():
    my_label.config(text='Me Clicked...')
    my_label.config(text=inputs.get())  # get the item from input box


click_me = tkinter.Button(text="Click Me", command=clicked_fn)
click_me.grid(column=1, row=1)


another_butt = tkinter.Button(text="Another Button")
another_butt.grid(column=2, row=0)

# entry
inputs = tkinter.Entry()
inputs.grid(column=3, row=2)

"""
Layouts Managers pack(), place(), grid()
pack = put items in below each other
place takes a coordinates around the screen x & y
grid takes column and row

next thing is padding
just do object.config(padx=20, pady=20)
"""


window.mainloop()
