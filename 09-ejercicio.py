""" Calculadora:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("400x400")
ventana.config(bd=50)
ventana.title("Calculadora | @akalautaro")

# Funciones

def cFloat(numero):
    try:
        resultado = float(numero)
    except:
        resultado=0 # Puede estar o no
        MessageBox.showerror("Error","Introduce bien los datos")
    return resultado

def sumar():
    resultado.set(cFloat(numero1.get())+cFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    MessageBox.showinfo("Resultado", f"El resultado es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

def restar():
    resultado.set(cFloat(numero1.get())-cFloat(numero2.get()))
    mostrarResultado()

def multipicar():
    resultado.set(cFloat(numero1.get())*cFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(cFloat(numero1.get())/cFloat(numero2.get()))
    mostrarResultado()


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(
    bd=5,
    relief="ridge",
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer número: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(ventana, text="").pack() # Separador

Button(marco, text="Sumar (+)", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar (-)", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar (*)", command=multipicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir (/)", command=dividir).pack(side="left", fill=X, expand=YES)


ventana.mainloop()