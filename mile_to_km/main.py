from tkinter import *

window= Tk()
window.title("Mile to KM")
window.minsize(width=210,height=72)
#padding=window.config(padx=10)
##################Enter mile value###########################
mile=Label(text="mile")
mile.grid(column=2,row=0)

mile_value=Entry()
mile_value.grid(column=1,row=0)
##############################################################
####################show equla value##########################
equality=Label(text="is equal to")
equality.grid(column=0,row=2)

value=Label(text="0")
value.grid(column=1,row=2)

km=Label(text="KM")
km.grid(column=2, row=2)
###############################################################
################calculate######################################
def calculate():
    km_value=round(float(mile_value.get())*1.609)
    value.config(text=km_value)

button=Button(text="calculate",command=calculate)
button.grid(column=1,row=3)

window.mainloop()