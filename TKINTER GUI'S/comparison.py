import tkinter as tk

root = tk.Tk()
title = tk.Label(root, text="Aplicación que calcula cuál es el mayor entre dos números")
title.grid(row=0,column=0)
n1 = tk.Entry(root)
n2 = tk.Entry(root)
n1.grid(row = 1,column = 0)
n2.grid(row = 1,column = 1)

result = tk.Label(text="El mayor es: ")
def major():
    v1 = float(n1.get())
    v2 = float(n2.get())
    if v1>v2:
        result.config(text="El primer valor es mayor")
    elif v2>v1:
        result.config(text="El segundo valor es mayor")
    else:
        result.config(text="Los dos valores son iguales")
button = tk.Button(text="Encontrar el mayor", command=major)
button.grid(row=2,column=0)
result.grid(row=2,column=1)
root.mainloop()
