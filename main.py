import tkinter as tk
import pyautogui as py
from time import sleep
from Funções.add_remove import adicionar_item, remover_item
from Funções.inputs_show import Inputs

def Executar(x=0):
    time = time_comand.get()
    if time:
        while x < int(time):
            x += 1
            try:
                for indice in range(list_comand.size()):
                    eval(list_comand.get(indice))
            except Exception as e:
                py.alert(text='Algo está Errado no Comando!') 
                break
    else:
        try:
            for indice in range(list_comand.size()):
                eval(list_comand.get(indice))
        except Exception as e:
            py.alert(text='Algo está Errado no Comando!')

#Janela
janela = tk.Tk()
janela.geometry('630x300')
janela.resizable(False, False)
janela.title('Macro')

comandos = ["sleep(x)", "py.moveTo(x,y)", "py.rightClick()", "py.leftClick()", "py.press(x)", "py.typewrite(x)", 
            "py.keyDown(x)"]

#FRAME 1
frame_1 = tk.Frame(janela)
frame_1.grid(row=0, column=0, sticky="w", padx=(10,20))

#BOTÃO DE OPÇÕES
opcao = tk.StringVar(janela)
opcao.set("Comandos")
opcao.trace_add("write", lambda *args: Inputs(opcao,label_x,entrada_x,label_y,entrada_y))

menu_opcoes = tk.OptionMenu(frame_1, opcao, *comandos)
menu_opcoes.grid(row=0, column=0, padx=(0,10))

#INPUTS
#X
label_x = tk.Label(frame_1)
label_x.grid(row=0, column=2, padx=5, pady=5, sticky="w")
label_x.grid_remove() 

entrada_x = tk.Entry(frame_1)
entrada_x.grid(row=0, column=3, padx=(10,0), pady=(20,0), sticky="w")
entrada_x.grid_remove()

#Y
label_y = tk.Label(frame_1, text="Y:")
label_y.grid(row=0, column=2, padx=5, pady=5, sticky="w")
label_y.grid_remove() 

entrada_y = tk.Entry(frame_1, width=5)
entrada_y.grid(row=0, column=4, padx=(10,0), pady=(20,0), sticky="w")
entrada_y.grid_remove()

#BOTÃO DE ADICIONAR ITENS DA LISTA
botao_adicionar = tk.Button(frame_1 ,text="Adicionar", command=lambda: adicionar_item(opcao, entrada_x, entrada_y, list_comand), bg="blue", fg="white")
botao_adicionar.grid(row=0, column=7, padx=(0,30))

#TEXTO DA LISTA
frame_2 = tk.Frame(janela)
frame_2.grid(row=1, column=0, sticky="w", padx=(10,20))

text = tk.Label(frame_2,text="Lista de Comandos:")
text.grid(row=1, column=0, sticky="w", padx=0, pady=(20,0))

text = tk.Label(frame_2,text="Quantas Vezes:")
text.grid(row=1, column=1, sticky="w", padx=(40,0), pady=(20,0))

time_comand = tk.Entry(frame_2, width=5)
time_comand.grid(row=1, column=2, sticky="w", padx=0, pady=(20,0))

#LISTA DE COMANDOS
list_comand = tk.Listbox(janela, width=87, font=("Arial", 10))
list_comand.grid(row=2, column=0, sticky="w", padx=(10, 0), pady=10)

#FRAME 2
frame_3 = tk.Frame(janela)
frame_3.grid(row=3, column=0, sticky="w", padx=(10,20))


#BOTÃO DE REMOVER ITENS DA LISTA
botao_remover = tk.Button(frame_3,text="Remover", command=lambda: remover_item(list_comand), bg="red", fg="white")
botao_remover.grid(row=0, column=0, sticky="w", padx=0)

botao_executar = tk.Button(frame_3,text="Iniciar Programa", command=Executar, bg="green", fg="white")
botao_executar.grid(row=0, column=1, sticky="w", padx=(10,20))

janela.mainloop()