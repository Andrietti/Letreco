from tkinter import *
from webbrowser import get


janela = Tk()


caixa_palavra = Entry(janela)
caixa_palavra.grid(row=999, column=0, padx= 10, pady=10,columnspan=3)

def pegarchute():
    chute = caixa_palavra.get()
    mostrar_chute = Label(janela, text=chute).grid(row=0, column=0)


botao_enviar = Button(janela, text="chutar", command=pegarchute)
botao_enviar.grid(row=999, column=3, columnspan=2)



janela.mainloop()