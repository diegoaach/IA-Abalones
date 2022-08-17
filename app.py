# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 19:13:24 2022

@author: Diego
"""
from tkinter import *
from tkinter.ttk import *
import matplotlib.pyplot as plot
import pandas as pd
import numpy as np
from scipy import stats
from functools import partial


root = Tk()

archivo = 'abalone.csv'
datos = pd.read_csv(archivo)
datos.columns=['Sex', 'Lenght','Diameter','Height','Whole weight', 'Shucked weight','Viscera weight','Shell weight', 'Rings']

def graf(datos):
    
    plot.hist(x=datos['Lenght']) #Histograma
    plot.title('Histograma de la segunda columna') #Titulo del histograma
    plot.xlabel('Valor de los datos') #Etiqueta x histograma
    plot.ylabel('Cantidad de los datos')  #Etiqueta y histograma


    plot.subplots()
    plot.boxplot(x=datos['Lenght']) #Cajas y bigotes

    fig = plot.figure()
    ax=fig.add_subplot(111)
    res = stats.probplot(datos['Lenght'], dist=stats.norm, plot=ax) #Normal

    plot.subplots()
    plot.scatter((datos['Lenght']),datos['Rings']) #Diagrama de dispersion





#printsom = partial(printsome, valcol1, valcol2, valgraph)

columns=['Sex', 'Lenght','Diameter','Height','Whole weight', 'Shucked weight','Viscera weight','Shell weight', 'Rings']

root.title('Graficadora')
root.geometry('500x500')

graphs = Combobox(state='readonly',values=['Histograma', 'Cajas y bigotes', 'Normal','Dispersion'])

colgraph= Combobox(state='readonly',values=['Sex', 'Lenght','Diameter','Height','Whole weight', 'Shucked weight','Viscera weight','Shell weight', 'Rings'] )

label = Label(root,text='Graficadora', font=('Serif',16))
    


label.grid(row=0,column=1)
graphs.grid(row=1, column=0)
colgraph.grid(row=1, column=2)


colgraph2 = Combobox(state='readonly',values=['Sex', 'Lenght','Diameter','Height','Whole weight', 'Shucked weight','Viscera weight','Shell weight', 'Rings'])
colgraph2.grid(row=2,column=2)


def histograma(columna):
    plot.hist(x=datos[columna]) #Histograma
    plot.title('Histograma') #Titulo del histograma
    plot.xlabel('Valor de los datos') #Etiqueta x histograma
    plot.ylabel('Cantidad de los datos')  #Etiqueta y histograma
    plot.show()
    
def boxplot(columna):
    plot.boxplot(x=datos[columna])
    plot.show()

def normal(columna):
    fig = plot.figure()
    ax=fig.add_subplot(111)
    res = stats.probplot(datos[columna], dist=stats.norm, plot=ax) #Normal
    plot.show()
    
def dispersion(columna1, columna2):
    plot.scatter((datos[columna1]),datos[columna2]) #Diagrama de dispersion

def graficar():
    
    if graphs.get() == '' or colgraph.get() == '':
        messagebox.showinfo(message='Debes elegir un grafico y al menos una columna')
    elif graphs.get() == 'Histograma':
        histograma(colgraph.get())
    elif graphs.get() == 'Cajas y bigotes':
        boxplot(colgraph.get())
    elif graphs.get() == 'Normal':
        normal(colgraph.get())
    elif graphs.get() == 'Dispersion' and colgraph2.get() != '':
        dispersion(colgraph.get(), colgraph2.get())
    else:
        messagebox.showinfo(message='Debes elegir 2 columnas')


        
def quartil(columna):
    removed = datos[columna]
    q25, q75 = np.percentile(removed,25), np.percentile(removed,75)
    iqr = q75-q25
    const = float(constiqr.get())
    cut = iqr*const
    lower, upper = q25-cut, q75+cut

    outliers_removed = [x for x in removed if x > lower and x < upper]
    return outliers_removed
    
def histogramaq(columna):
    plot.hist(columna) #Histograma
    plot.title('Histograma') #Titulo del histograma
    plot.xlabel('Valor de los datos') #Etiqueta x histograma
    plot.ylabel('Cantidad de los datos')  #Etiqueta y histograma
    plot.show()
    
def boxplotq(columna):
    plot.boxplot(columna)
    plot.show()

def normalq(columna):
    fig = plot.figure()
    ax=fig.add_subplot(111)
    res = stats.probplot(columna, dist=stats.norm, plot=ax) #Normal
    plot.show()
    
def dispersionq(columna1, columna2):
    plot.scatter(columna, columna2) #Diagrama de dispersion
    plot.show()

def graficarq():
    
    columna = quartil(colgraph.get())
    
    
    if graphs.get() == '' or columna == '':
        messagebox.showinfo(message='Debes elegir un grafico y al menos una columna')
    elif graphs.get() == 'Histograma':
        histogramaq(columna)
    elif graphs.get() == 'Cajas y bigotes':
        boxplotq(columna)
    elif graphs.get() == 'Normal':
        normalq(columna)
    elif graphs.get() == 'Dispersion' and colgraph2.get() != '' and columa != colgraph2.get():
        columna2 = quartil(colgraph2.get())
        dispersionq(columna, columna2)
    else:
        messagebox.showinfo(message='Debes elegir 2 columnas distintas') 
        
graficarn = partial(graficar, colgraph.get(), colgraph2.get())

graficarquart = partial(graficarq, colgraph.get(), colgraph2.get())

crear_graf = Button(root, text='Graficar', width=10, command=graficar)
crear_graf.grid(row=3, column=1)

label2 = Label(root, text='Constante IQR:', font=('Serif', 12))
label2.grid(row=9, column=0)

constiqr = Entry()
constiqr.insert(0, 1.5)
constiqr.grid(row=9, column=1)

graphIQR = Button(root, text='Graficar sin atipicos', width=25, command = graficarq)
graphIQR.grid(row=7, column=1)

modal = Label(root, text = 'Moda')
modal.grid(row=12, column=0)
medianal = Label(root, text = 'Mediana')
medianal.grid(row=13, column=0)
medial = Label(root, text = 'Media')
medial.grid(row=14, column=0)
kurtosisl = Label(root, text = 'Kurtosis')
kurtosisl.grid(row=15, column=0)
asimetrial = Label(root, text = 'Asimetria')
asimetrial.grid(row=16, column=0)

modae = Entry()
modae.grid(row=12, column=1)
medianae = Entry()
medianae.grid(row=13, column=1)
mediae = Entry()
mediae.grid(row=14, column=1)
kurtosise = Entry()
kurtosise.grid(row=15, column=1)
asimetriae = Entry()
asimetriae.grid(row=16, column=1)



def calcular(*args):
    media = np.mean(datos[colgraph.get()])
    mediana = np.median(datos[colgraph.get()])
    moda = stats.mode(datos[colgraph.get()])
    kurtosis = stats.kurtosis(datos[colgraph.get()])
    asimetria =  datos[colgraph.get()].skew()
    
    modae.insert(0, moda)
    mediae.insert(0, media)
    medianae.insert(0, mediana)
    kurtosise.insert(0, kurtosis)
    asimetriae.insert(0, asimetria)

colgraph.bind('<<ComboboxSelected>>', calcular)


root.mainloop()


#root.destroy() #destruye la ventana 