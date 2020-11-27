from tkinter import *

ventana = Tk()
ventana.title("@akalautaro")
ventana.geometry("540x480")
ventana.config(bg = "black")

def pruebas(nombre, pais):
    return f"Hola {nombre}, veo que eres de {pais}"

texto = Label(ventana, text = "Bienvenido a mi programa")   # Parametros de palabra clave, keyword parameters
texto.config(                                               # Paso parametros
            fg="green", 
            bg="black",
            padx = 5,
            pady = 5,
            font = ("Consolas", 15))                                     # Tambien se pueden pasar los valores en hexadecimal
texto.pack()                                                # Empaqueto y muestro texto

texto = Label(ventana, text = "Soy Lautaro Celli, también conocido como @akalautaro :D")
texto.config(
            fg="green", 
            bg="black", 
            padx = 5,
            font = ("Consolas", 12),
            cursor = "spider")
texto.pack(anchor = W) 

texto = Label(ventana, text = "Estoy aprendiendo a hacer interfaces gráficas")
texto.config(
            fg="green", 
            bg="black", 
            padx = 5,
            font = ("Consolas", 10),
            cursor = "spider")
texto.pack(anchor = W) 

texto = Label(ventana, text = pruebas(nombre = "Victor", pais = "Espanya")) # Rellenar parametro permite cambiar el orden de los parametros como yo quiera
texto.config(
            height = 2,
            fg="green", 
            bg="black", 
            padx = 5,
            font = ("Consolas", 10),
            cursor = "spider")
texto.pack(anchor = W)

ventana.mainloop()
