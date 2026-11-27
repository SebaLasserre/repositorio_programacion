import tkinter as tk
from tkinter import ttk

def saludo():
    nombre= entrada.get()
    etiqueta_saludo.config(text=f"Que tocas capo {nombre}!")

ventana = tk.Tk()
ventana.title("La ventanita del amor")
ventana.geometry("1200x800")

etiqueta=ttk.Label(ventana, text="Ingresa tu nombre").grid(padx=10)

entrada = tk.Entry (ventana)
etiqueta_saludo=tk.Label(ventana, text="")
boton= tk.Button(ventana, text="no apretes aca", command=saludo)



# entrada.pack()
# etiqueta_saludo.pack()
# boton.pack()
ventana.mainloop()