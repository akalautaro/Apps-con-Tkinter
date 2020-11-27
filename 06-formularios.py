from tkinter import *

ventana = Tk()
ventana.geometry("540x480")
ventana.title("Formularios | @akalautaro")
ventana.resizable(0,0)

# Texto encabezado
encabezado = Label(ventana, text = "Formularios con Tkinter | akalautaro")
encabezado.config(
    fg = "white",
    bg = "darkgray",
    font = ("Consolas", 18),
    pady = 5,
    padx = 50
)
encabezado.grid(row = 0, column = 0, columnspan = 100, sticky = N)

# Label para el campo (nombre)
label = Label(ventana, text = "Nombre: ")
label.grid(row = 1, column = 0, pady = 5, padx = 5, sticky = W)

# Campo de texto (nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column = 1, pady = 5, padx = 5, sticky = W)
campo_texto.config(justify = "left", state = "normal") # State puede ser normal o disabled, dis no deja escribir

# Label para el campo (apellido)
label = Label(ventana, text = "Apellido: ")
label.grid(row = 2, column = 0, pady = 5, padx = 5, sticky = W)

# Campo de texto (apellido)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column = 1, pady = 5, padx = 5, sticky = W)
campo_texto.config(justify = "left", state = "normal")

# Label para el campo (descripcion)
label = Label(ventana, text = "Descripcion: ")
label.grid(row = 3, column = 0, pady = 5, padx = 5, sticky = NW)

# Campo de texto grande (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row = 3, column = 1, pady = 5, padx = 5)
campo_grande.config(
    width = 30,
    height = 5,
    font = ("Consolas", 10)
)

# Botones
Label(ventana).grid(row=4, column=1) # Separación

boton = Button(ventana, text = "Enviar")
boton.grid(row = 5, column = 1, sticky = W)
boton.config(
    pady= 5,
    padx = 5,
    bg = "green",
    fg = "white"
)


ventana.mainloop()