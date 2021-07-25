from Perceptron import Perceptron
from tkinter import *

def onButtonPress():
    avaliacao = perceptron.avalia([virus.get(), bacteria.get(), dorDeCabeca.get(), coriza.get()])

    if (avaliacao):
        print('gripe')
    else:
        print('resfriado')

baseTreino = [
    [1,0,1,1],
    [0,1,0,1],
    [1,0,1,0],
    [0,1,1,1],
    [0,0,1,1],
    [0,0,0,1]
]

perceptron = Perceptron(1, 1);

perceptron.treina(baseTreino)

master = Tk()

Label(master, text="Sintomas:").grid(row=0, sticky=W)

virus = IntVar()
Checkbutton(master, text="virus", variable=virus).grid(row=1, sticky=W)
bacteria = IntVar()
Checkbutton(master, text="bacteria", variable=bacteria).grid(row=2, sticky=W)
dorDeCabeca = IntVar()
Checkbutton(master, text="dor de cabeça", variable=dorDeCabeca).grid(row=3, sticky=W)
coriza = IntVar()
Checkbutton(master, text="coriza", variable=coriza).grid(row=4, sticky=W)


Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
Button(master, text='Show', command=onButtonPress).grid(row=6, sticky=W, pady=4)
mainloop()


