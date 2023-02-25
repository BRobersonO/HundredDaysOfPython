from tkinter import *

def button_clicked():
    text = input.get()
    result = float(text) * 1.609344
    km_num.config(text=result)
    pass

window = Tk()
window.title("Mile to Kilometers Converter")
window.minsize(width=250, height=100)
window.config(padx=20,pady=20)

# Entry
input = Entry()
input.grid(column=1, row=0)

# Label 1
miles = Label(text="Miles")
miles.grid(column=2,row=0)

# Label 2
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

# Label 3
km_num = Label(text=0)
km_num.grid(column=1,row=1)

# Label 4
km = Label(text="Km")
km.grid(column=2,row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()