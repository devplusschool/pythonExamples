import tkinter as tk

root = tk.Tk()
#Etiqueta de título de la aplicación
title = tk.Label(root,text="Bienvenido a la aplicación de grado décimo")
title.grid(row=0,column=0)
#Intrfaz que calcula la densidad de alguna sustancia teniendo en cuenta dos valores
#Entradas de valores:
masa = tk.Entry(root)
vol = tk.Entry(root)
masa.grid(row=1,column=0)
vol.grid(row=1,column=1)

def density():
    m = float(masa.get())
    v = float(vol.get())
    d = m/v
    result.config(text=f"La densidad calculada es: {d}")

bt = tk.Button(root, text="Calcular densidad", command=density)
bt.grid(row=2, column=0)
result = tk.Label(root, text="Resultado: 0")
result.grid(row=2, column=1)



root.mainloop()
