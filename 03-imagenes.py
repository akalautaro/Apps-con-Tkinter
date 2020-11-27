from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("540x480")

Label(ventana, text = "Alabado sea Itachi uwu").pack(anchor=CENTER)

imagen = Image.open('./tkinter/imagenes/229691.jpg')
render = ImageTk.PhotoImage(imagen)
Label(ventana, image = render).pack()

ventana.mainloop()