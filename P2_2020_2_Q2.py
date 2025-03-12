#Q2

from tkinter import *
import P2_2020_2_Q1 as Q1


def bt_click():
    comprimento = texto.get()
    lista_random = Q1.sorter.randomList(int(comprimento))

    lista_random.sort()
    lista_ordenada["text"] = lista_random


janela = Tk()
janela.title("P2 2020.2 - Questao 2")

comp_lista = Label(janela, text="Comprimento da lista: ")
txt = Label(janela, text="Lista ordenada: ")
lista_ordenada = Label(janela, text="", bg="lightblue")
texto = Entry(janela)
botao = Button(janela, text="Confirmar", command=bt_click)

comp_lista.grid(row=0, column=0, sticky=W+E)
texto.grid(row=0, column=1, sticky=W+E)
botao.grid(row=0, column=2, sticky=W+E)
txt.grid(row=3, column=0, sticky=W+E, columnspan=3)
lista_ordenada.grid(row=4, column=0, sticky=W+E, columnspan=500)

janela.geometry("400x150+100+100")
janela.mainloop()