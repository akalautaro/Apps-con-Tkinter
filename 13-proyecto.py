"""
Crear un programa que tenga:
Done - Ventana
Done - Tamaño fijo
Done - No resizable
Done - Un menu (Inicio, Añadir, Info, Salir)
Done - Diferentes pantallas
Done - Formulario de añadir productos
DONE - Guardar datos temporalmente
DONE - Mostrar datos listados en la pantalla principal
Done - Opcion de salir
"""

from tkinter import *
from tkinter import ttk

# Creo entana
ventana = Tk()
# ventana.geometry("540x480")
ventana.minsize(540, 480)
ventana.title("Proyecto MeP | @akalautaro")
ventana.resizable(0,0)

# Pantallas
def limpiar():
    contenido = ventana.grid_slaves()
    for c in contenido:
        c.grid_remove()

def home():
    # Ocultar otras pantallas
    limpiar()

    home_label = Label(ventana, text="Inicio")
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=230,
        pady=20
    )
    home_label.grid(row=0, column=0, columnspan=10)

    products_box.grid(row=2)

    # Listar productos

    # Label(ventana, text="Listado de productos").grid(row=2, sticky=W)

    # for product in products:
    #     if len(product)==3:
    #         product.append("Added")
    #         Label(products_box, text=product[0]).grid(column=0, sticky=NW)
    #         Label(products_box, text=product[1]).grid(sticky=W)
    #         Label(products_box, text=product[2]).grid(sticky=W)
    #         Label(products_box, text="---------------------------------").grid(sticky=W)

    for product in products:
        if len(product)==3:
            product.append("Added")
            products_box.insert('', END, text=product[0], values=(product[1], product[2]))

def add():
    limpiar()

    add_label = Label(ventana, text="Añadir producto")
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=175,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Campos del formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Arial", 10),
        padx=5,
        pady=5
    )
    
    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=W)
    boton.config(
        padx=6, 
        pady=5,
        bg="green",
        fg="white"
    )

def info():
    limpiar()

    info_label = Label(ventana, text="Información")
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=200,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label = Label(ventana, text="Creado por @akalautaro - 2020")
    data_label.grid(row=1, column=0)

def ayuda():
    limpiar()
    
    ayuda_label = Label(ventana, text="Ayuda")
    ayuda_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=230,
        pady=20
    )
    ayuda_label.grid(row=0, column=0)

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()

# Variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantallas
home_label = add_label = info_label = data_label = ayuda_label = None

home_label = Label(ventana, text="Inicio")
# products_box = Frame(ventana, width=250)

Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=("#1","#2"))
products_box.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
products_box.heading("#0", text='Producto', anchor=W)
products_box.heading("#1", text='Precio', anchor=W)
products_box.heading("#2", text='Descripción', anchor=W)

add_label = Label(ventana, text="Añadir")

# Formulario
add_frame= Frame(ventana)

add_name_label = Label(ventana, text="Nombre del producto:")
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text="Precio:")
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text="Descripción:")
add_description_entry = Text(ventana)

add_separator = Label(ventana)

boton = Button(ventana, text="Guardar", command=add_product)

info_label = Label(ventana, text="Info")

ayuda_label = Label(ventana, text="Help")

data_label = Label(ventana, text="Creado por @akalautaro - 2020")

# Cargo pantalla de inicio
home()

# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Info", command=info)
menu_superior.add_command(label="Ayuda", command=ayuda)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menu
ventana.config(menu=menu_superior)

ventana.mainloop()