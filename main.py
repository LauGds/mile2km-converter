from tkinter import *
NUM = 1.609

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=120)

is_equal = Label(text="is equal to", font=("Arial", 15, "bold"))
is_equal.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 15, "bold"))
miles.grid(column=2, row=0)

km = Label(text="Km", font=("Arial", 15, "bold"))
km.grid(column=2, row=1)

convert = Label(text="0", font=("Arial", 15, "bold"))
convert.grid(column=1, row=1)


def calculate():
    calc = input.get()
    total = float(calc) * float(NUM)
    print(convert.config(text=total))


button = Button(text="Calculate", command=calculate, font=20)
button.grid(column=1, row=2)


input = Entry(width=8)
input.get()
input.grid(column=1, row=0)

window.mainloop()
