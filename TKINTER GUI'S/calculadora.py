import tkinter as tk

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Calculadora simple")

# --- Campo de texto ---
entrada = tk.Entry(ventana, width=20, font=("Arial", 18))
entrada.grid(row=0, column=0, columnspan=4)


# --- Funciones ---
def presionar_0():
    entrada.insert(tk.END, "0")

def presionar_1():
    entrada.insert(tk.END, "1")

def presionar_2():
    entrada.insert(tk.END, "2")

def presionar_3():
    entrada.insert(tk.END, "3")

def presionar_4():
    entrada.insert(tk.END, "4")

def presionar_5():
    entrada.insert(tk.END, "5")

def presionar_6():
    entrada.insert(tk.END, "6")

def presionar_7():
    entrada.insert(tk.END, "7")

def presionar_8():
    entrada.insert(tk.END, "8")

def presionar_9():
    entrada.insert(tk.END, "9")

def presionar_punto():
    entrada.insert(tk.END, ".")

def presionar_suma():
    entrada.insert(tk.END, "+")

def presionar_resta():
    entrada.insert(tk.END, "-")

def presionar_multi():
    entrada.insert(tk.END, "*")

def presionar_div():
    entrada.insert(tk.END, "/")

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def limpiar():
    entrada.delete(0, tk.END)


# --- Creación de botones ---
botones = [
    ("7", presionar_7), ("8", presionar_8), ("9", presionar_9), ("/", presionar_div),
    ("4", presionar_4), ("5", presionar_5), ("6", presionar_6), ("*", presionar_multi),
    ("1", presionar_1), ("2", presionar_2), ("3", presionar_3), ("-", presionar_resta),
    ("0", presionar_0), (".", presionar_punto), ("+", presionar_suma), ("=", calcular)
]

fila = 1
columna = 0

for texto, funcion in botones:
    boton = tk.Button(ventana, text=texto, width=5, height=2, command=funcion)
    boton.grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# --- Botón limpiar ---
tk.Button(ventana, text="C", width=22, height=2, command=limpiar).grid(row=fila, column=0, columnspan=4)

# --- Iniciar ventana ---
ventana.mainloop()
