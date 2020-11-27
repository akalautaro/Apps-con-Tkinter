from tkinter import *

ventana = Tk()
ventana.title("@akalautaro")
ventana.geometry("540x480")

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
            height = 3,
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

texto = Label(ventana, text = "GitHub: @akalautaro")
texto.config(
            height = 1,
            fg="orange", 
            bg="black", 
            padx = 5,
            font = ("Consolas", 10),
            cursor = "spider")
texto.pack(side= LEFT, fill = X, expand=YES) 

texto = Label(ventana, text = "LinkedIn: Lautaro Celli")
texto.config(
            fg="blue", 
            bg="black", 
            padx = 5,
            font = ("Consolas", 10),
            cursor = "spider")
texto.pack(side= LEFT, fill = X, expand=YES) 

texto = Label(ventana, text = "Twitter: @akalautaro")
texto.config(
            height = 1,
            fg="lightblue", 
            bg="black", 
            padx = 5,
            font = ("Consolas", 10),
            cursor = "spider")
texto.pack(side= LEFT, fill = X, expand=YES) 

ventana.mainloop()