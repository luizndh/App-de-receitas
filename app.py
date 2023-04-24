from tkinter import *
from tkinter import ttk
import json
import random

root = Tk()
root.title("Gerador de Receitas")
root.geometry('1200x800')

with open("receitas.JSON", "r") as arq:
        receitas = json.load(arq)


def gerar_receita():
    # Pegando uma receita aleatoria
    id_receita = str(random.randint(1, len(receitas)))
    
    # Definindo o que será mostrado na janela
    texto = f"{formatar_itens(receitas[id_receita])}"
    
    # Limpa o conteúdo da receita anterior e insere o novo
    texto_receita.delete("1.0", END)
    texto_receita.insert(END, texto)
    
    
def formatar_itens(itens):
    return "\n\n".join([f"- {item}: {itens[item]}" for item in itens])

# Cria o widget que exibirá a receita
texto_receita = Text(root, wrap=WORD, height=40, font=("Arial", 12))
texto_receita.pack(padx=10, pady=10)


# Cria o botão para gerar uma nova receita
botao_gera = ttk.Button(root, text="Gerar Receita", command=gerar_receita)
botao_gera.pack(pady=10)

# Inicia o loop de eventos
root.mainloop()
