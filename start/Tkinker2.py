from tkinter import *
window = Tk()
window.title("Игра-джекпот")
window.geometry('400x250')
lbl = Label(window, width = "40", height = "20")
lbl = Label(text="Джекпот=",font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop() 
