from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

def Miles_to_Km():
    miles = float(miles_input.get())
    km = miles *1.609
    kilometer_result_label.config(text=f'{km}')
  
#entry
miles_input = Entry(width=7)
miles_input.grid(column=2, row=0)

#label
lable_miles = Label(text="Miles")
lable_miles.grid(column=3,row=0)

kilometer_result_label = Label(text=0)
kilometer_result_label.grid(column=2,row =2)

Km = Label(text="km")
Km.grid(column=3,row=2)

equal = Label(text="is equal to ")
equal.grid(column=1,row=2)

#button
button = Button(text ="Calculate",command=Miles_to_Km)
button.grid(column=2,row=3)

window.mainloop()
