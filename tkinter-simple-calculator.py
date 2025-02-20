import tkinter as tk
from tkinter import messagebox

def calcular(operacion):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if operacion == "+":
            resultado = a + b
        elif operacion == "-":
            resultado = a - b
        elif operacion == "*":
            resultado = a * b
        elif operacion == "/":
            if b == 0:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return
            resultado = a / b

        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingrese números válidos")

def limpiar():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_resultado.config(text="Resultado: ")

root = tk.Tk()
root.title("Calculadora con Tkinter")
root.geometry("300x300")
root.resizable(False, False)

tk.Label(root, text="Número 1:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Número 2:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="+", command=lambda: calcular("+"), width=5).grid(row=0, column=0)
tk.Button(frame_botones, text="-", command=lambda: calcular("-"), width=5).grid(row=0, column=1)
tk.Button(frame_botones, text="*", command=lambda: calcular("*"), width=5).grid(row=0, column=2)
tk.Button(frame_botones, text="/", command=lambda: calcular("/"), width=5).grid(row=0, column=3)

label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12))
label_resultado.pack(pady=10)

tk.Button(root, text="Borrar", command=limpiar, width=10, bg="red", fg="white").pack()

root.mainloop()