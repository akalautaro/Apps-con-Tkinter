""" Calculadora:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox as MessageBox

class Calculadora():

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def cFloat(self, numero):
        try:
            resultado = float(numero)
        except:
            resultado=0 # Puede estar o no
            MessageBox.showerror("Error","Introduce bien los datos")
        return resultado

    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get())+self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get())-self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def multipicar(self):
        self.resultado.set(self.cFloat(self.numero1.get())*self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get())/self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

ventana = Tk()
ventana.geometry("400x400")
ventana.config(bd=50)
ventana.title("Calculadora | @akalautaro")

calculadora = Calculadora(MessageBox)

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
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Segundo número: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(ventana, text="").pack() # Separador

Button(marco, text="Sumar (+)", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar (-)", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar (*)", command=calculadora.multipicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir (/)", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)


ventana.mainloop()