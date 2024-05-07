import tkinter as tk

def remover_item(list_comand):
    if list_comand.curselection():
        indice = list_comand.curselection()[0]
        list_comand.delete(indice)

def adicionar_item(opcao, entrada_x, entrada_y, list_comand):
    item_selecionado = opcao.get()
    if item_selecionado != 'Comandos':
        if item_selecionado == "py.press(x)":
            x = str(entrada_x.get())
            list_comand.insert(tk.END, f"py.press({x})")
        elif item_selecionado == "py.moveTo(x,y)":
            x = int(entrada_x.get())
            y = int(entrada_y.get())
            list_comand.insert(tk.END, f"py.moveTo({x},{y})")
        elif item_selecionado == "sleep(x)":
            x = int(entrada_x.get())
            list_comand.insert(tk.END, f"sleep({x})")
        elif opcao.get() == "py.typewrite(x)":
            x = entrada_x.get()
            if "\\" in x:
                list_comand.insert(tk.END, f"py.typewrite(r'{x}')")
            else:
                list_comand.insert(tk.END, f"py.typewrite('{x}')")
        elif opcao.get() == "py.keyDown(x)":
            x = str(entrada_x.get())
            list_comand.insert(tk.END, f"py.keyDown({x})")
            
        else:
            list_comand.insert(tk.END, item_selecionado)
