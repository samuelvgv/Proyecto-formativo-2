from tkinter import *
window = Tk()
window.geometry('300x200')
window.title("bienvenidos")
lbl=Label(window, text="hola", font=("Arial Bold",50))
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked!!")
btn=Button(window, text="haz click", bg="green", fg="white")
btn.grid(column=1, row=0)

window.mainloop()