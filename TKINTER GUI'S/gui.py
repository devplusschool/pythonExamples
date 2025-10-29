#GUI: Del inglés Graphic User Interface, interfaz gráfica de usuario.
import tkinter as tk

root = tk.Tk() #Contenedero inicial o raíz
root.geometry("1080x720")
title = tk.Label(root,text="Bienvenido a la aplicación que calcula densidades")
title.grid(row=0, column=0)
masa = tk.Entry(root)
vol = tk.Entry(root)
masa.grid(row=1, column=0)
vol.grid(row = 1,column =1)

resultado = tk.Label(text="El resultado es: ")
resultado.grid(row=2, column=1)

def density():
    mass = float(masa.get())
    volume = float(vol.get())
    #La función get() permite obtener el valor escrito en Entry
    d = mass/volume
    resultado.config(text=f"La densidad es: {d}")

boton = tk.Button(root, text="Calcular densidad", command=density)
boton.grid(row=2, column=0)
root.mainloop()
