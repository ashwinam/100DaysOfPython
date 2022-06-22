import tkinter

window = tkinter.Tk()
window.config(width=350, height=200, padx=20, pady=20)
window.title("Miles to KM converter")


def miles_to_km():
    mile = float(inputs.get())
    kms = round(mile * 1.609)
    zero.config(text=f"{kms}")


# Entry
inputs = tkinter.Entry()
inputs.config(width=10)
inputs.grid(column=1, row=0)

# label
miles = tkinter.Label()
miles.config(text="Miles", padx=5, pady=5, font=15)
miles.grid(column=2, row=0)

# second label
is_equal_to = tkinter.Label()
is_equal_to.config(text="is equal to", font=15)
is_equal_to.grid(column=0, row=1)

# third label
zero = tkinter.Label()
zero.config(text=0, font=15)
zero.grid(column=1, row=1)

# fourth label
km = tkinter.Label()
km.config(text="KM", font=15)
km.grid(column=2, row=1)

# Button
calculate = tkinter.Button()
calculate.config(text="calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
