from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("250x250")
ventana.config(bd=75)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "@akalautaro") # Titulo, cuerpo

def sacarError():
    MessageBox.showerror("Error", "@akalautaro") # Titulo, cuerpo

def sacarPeligro():
    MessageBox.showwarning("Warning", "@akalautaro") # Titulo, cuerpo

def salir(nombre):
    resultado = MessageBox.askquestion("Salir","¿Quieres salir?")
    if resultado != "no":
        MessageBox.showinfo("Adiós", f"Nos vemos {nombre}")
        ventana.destroy()

Button(ventana, text="Mostrar alerta", command=sacarError).pack()

Button(ventana, text="Salir", command=lambda:salir("Lautaro")).pack()   # Lambda:salir es para pasarle el parametro a la funcion y que el programa funcione bien
                                                                        # Así la función actuará sólo cuando le dé click
ventana.mainloop()
