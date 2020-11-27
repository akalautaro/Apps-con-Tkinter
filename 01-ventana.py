from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "@akalautaro"
        # self.icon = os.path.abspath('./TKINTER/imagenes/akalautaro.ico')
        self.icon = ('C:/Users/danie/Desktop/Lautaro/Informática/aprendiendo_python/master_python/Tkinter/imagenes/akalautaro.ico')
        self.size = "480x360"
        self.resizable = True
    
    def cargar(self):

        # Crear la ventana raíz
        ventana = Tk()
        self.ventana = ventana

        # Título de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_favicon = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_favicon):
            ruta_favicon = (self.icon)


        # Insertar favicon
        # ventana.iconbitmap('./master_python/TKINTER/imagenes/favicon.ico') La ruta es así ya que VSCode trabaja en la carpeta aprendiendo_python
        ventana.iconbitmap(ruta_favicon)

        # Mostrar texto en la ventana
        texto = Label(ventana, text = ruta_favicon)
        texto.pack()

        # Cambiar tamaño de una ventana
        ventana.geometry(self.size) # AnchoxAlto

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1,1) # 1,0 deja cambiar ancho - 0,1 deja cambiar alto - 0,0 no cambia nada
        else:
            ventana.resizable(0,0)
        
        # Arrancar y mostrar ventana hasta que se cierre, este método tiene que ser el último
        # ventana.mainloop()

    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()



# Instanciar programa mediante la clase

programa = Programa()
programa.cargar()
programa.addTexto("Hola desde VSCode :D")
programa.mostrar()
