from tkinter import *

ventana = Tk()
ventana.title("Marcos | @akalautaro")
ventana.geometry("540x480")

marco = Frame(ventana, width = 100, height = 50)
marco.config(
    bg = "green",
    bd = 5,
    relief = "ridge"
)
marco.pack(side = RIGHT, anchor = SE)

marco.pack_propagate(False) # Con esto evito que se contraiga
texto = Label(marco, text = "Siguiente") # Contrae el marco "padre"
texto.config(
    bg = "green",
    fg = "black",
    font = ("Arial", 10),
    # height = 10,
    # width = 10,
    # bd = 1,
    anchor = CENTER
)
texto.pack(fill = Y, expand = YES) # Si pongo el fill, puedo obviar las propiedades hw y bd, también puedo sacar el anchor del config y colocarlo en el pack

marco = Frame(ventana, width = 100, height = 50)
marco.config(
    bg = "red",
    bd = 5,
    relief = "ridge"
)
marco.pack(side = RIGHT, anchor = SE)

marco.pack_propagate(False)
texto = Label(marco, text = "Cancelar")
texto.config(
    bg = "red",
    fg = "black",
    font = ("Arial", 10),
    anchor = CENTER
)
texto.pack(fill = Y, expand = YES)


marco = Frame(ventana, width = 100, height = 50)
marco.config(
    bg = "red",
    bd = 5,
    relief = "ridge"
)
marco.pack(side = LEFT, anchor = SE)

marco.pack_propagate(False)
texto = Label(marco, text = "Salir")
texto.config(
    bg = "red",
    fg = "black",
    font = ("Arial", 10),
    anchor = CENTER
)
texto.pack(fill = Y, expand = YES)

ventana.mainloop()