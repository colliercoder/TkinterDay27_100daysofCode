from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 500, height =150)

#Label
is_equal = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal.grid(column=0, row=1)
is_equal.config(padx=20, pady=20)

miles = Label(text="Miles", font=("Arial", 24, "bold"))
miles.grid(column=2, row=0)
#miles.config(padx=20, pady=20)

km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)
km.config(padx=20, pady=20)

to_km = Label(text="0", font=("Arial", 24, "bold"))
to_km.grid(column=1, row=1)
#to_km.config(padx=20, pady=20)

#Button

def convert():
    conversion = float(input.get())
    conversion *= 1.60934
    to_km.config(text=round(conversion,2))

#Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

#Entry

input = Entry(width=20)
input.grid(column=1,row=0)
input.get()


window.mainloop()
