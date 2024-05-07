import tkinter as tk
import pyautogui as py

def Inputs(opcao,label_x,entrada_x,label_y,entrada_y):
    if opcao.get() == "sleep(x)":
        label_x.configure(text="Time:")
        entrada_x.config(width=5)
        label_x.grid(row=0, column=2, padx=0, pady=0, sticky="w")
        entrada_x.grid(row=0, column=3, padx=(0,15), pady=0, sticky="w")

        entrada_x.delete(0, tk.END)  

        label_y.grid_remove()
        entrada_y.grid_remove()

    elif opcao.get() == "py.moveTo(x,y)":
        label_x.configure(text="X:")
        entrada_x.config(width=5)
        label_x.grid(row=0, column=2, padx=0, pady=0, sticky="w")
        entrada_x.grid(row=0, column=3, padx=(0,15), pady=0, sticky="w")
        label_y.grid(row=0, column=4, padx=0, pady=0, sticky="w")
        entrada_y.grid(row=0, column=5, padx=(0,15), pady=0, sticky="w")

        entrada_x.delete(0, tk.END)  
        entrada_y.delete(0, tk.END)

    elif opcao.get() == "py.press(x)":
        label_x.configure(text="Tecla:")
        entrada_x.config(width=5)
        label_x.grid(row=0, column=2, padx=0, pady=0, sticky="w")
        entrada_x.grid(row=0, column=3, padx=(0,15), pady=0, sticky="w")
        
        entrada_x.delete(0, tk.END) 

        label_y.grid_remove()
        entrada_y.grid_remove()
    
    elif opcao.get() == "py.typewrite(x)":
        label_x.configure(text="Frase:")
        entrada_x.config(width=60)
        label_x.grid(row=0, column=2, padx=0, pady=0, sticky="w")
        entrada_x.grid(row=0, column=3, padx=(0,15), pady=0, sticky="w")

        entrada_x.delete(0, tk.END)  

        label_y.grid_remove()
        entrada_y.grid_remove()
        pass
    elif opcao.get() == "py.keyDown(x)":
        label_x.configure(text="Tecla Segurada:")
        entrada_x.config(width=5)
        label_x.grid(row=0, column=2, padx=0, pady=0, sticky="w")
        entrada_x.grid(row=0, column=3, padx=(0,15), pady=0, sticky="w")

        entrada_x.delete(0, tk.END)  

        label_y.grid_remove()
        entrada_y.grid_remove()

    else:
        label_x.grid_remove()
        entrada_x.grid_remove()
        label_y.grid_remove()
        entrada_y.grid_remove()