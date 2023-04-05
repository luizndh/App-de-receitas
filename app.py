from tkinter import *
from tkinter import ttk
import json
import random

root = Tk()
root.title("Gerador de Receitas")

lista_widgets = []

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0)

def gerar_receita():
    # Limpando os widgets da receita antiga mostrada
    if len(lista_widgets) != 0:
        for widget in lista_widgets:
            widget.grid_remove()
        lista_widgets.clear()
    
    i = 0
    with open("script/receitas.JSON", "r") as arq:
        receitas = json.load(arq)
    id_receita = str(random.randint(1, len(receitas)))
        
    label_nome_topico = ttk.Label(mainframe, text='NOME: ')
    label_descricao_topico = ttk.Label(mainframe, text='DESCRIÇÃO: ')
    label_tempo_preparo_topico = ttk.Label(mainframe, text='TEMPO DE PREPARO: ')
    label_utensilios_topico = ttk.Label(mainframe, text='UTENSÍLIOS: ')
    label_equipamento_topico = ttk.Label(mainframe, text='EQUIPAMENTOS: ')
    label_medidores_topico = ttk.Label(mainframe, text='MEDIDORES: ')
    
    label_nome_topico.grid(column=0, row=0, sticky=E)
    label_descricao_topico.grid(column=0, row=1, sticky=E)
    label_tempo_preparo_topico.grid(column=0, row=2, sticky=E)
    label_utensilios_topico.grid(column=0, row=3, sticky=E)
    label_equipamento_topico.grid(column=0, row=4, sticky=E)
    label_medidores_topico.grid(column=0, row=5, sticky=E)    
    
    for topico, conteudo in receitas[id_receita].items():
        if "Ingredientes" in topico:
            label_topico = ttk.Label(mainframe, text=f'{topico.upper()}: ')
            label_topico.grid(column=0, row=i, sticky=NE)
            lista_widgets.append(label_topico)
        
        label_conteudo = ttk.Label(mainframe, text=f'{conteudo}')
        label_conteudo.grid(column=1, row=i, sticky=NW)
        lista_widgets.append(label_conteudo)
        
        i += 1

gera = ttk.Button(mainframe, text="Gerar nova receita", command=gerar_receita)
gera.grid(column=1, row=13, sticky=S)



root.mainloop()
