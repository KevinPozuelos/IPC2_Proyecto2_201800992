from tkinter import filedialog, messagebox,END
import xml.etree.ElementTree as ET
from listaSimple import listaMatriz
from matriz import matrix
lista = listaMatriz()
cotenido = []

class Funciones_:
    def __init__(self):
        self.archivo = ""

    def nuevo(self,editor):
        editor.delete(1.0, END)
        self.archivo = ""

    def abrir(self, editor):
        self.archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir="/home/")
        ruta = self.archivo
        tree = ET.parse(ruta)
        root = tree.getroot()
        f = 0
        c = 1

        for element in root:
            cadena = element[3].text
            matrice = matrix(str(element[0].text), int(element[1].text), int(element[2].text))
            for i in range(len(element[3].text)):
                if cadena[i] == '\n':
                    f += 1
                    c = 1
                elif cadena[i] == '*' or cadena[i] == '-':
                    matrice.nuevoNodo(cadena[i], f, c)
                    c += 1
            f = 0
            c = 1
            print(matrice.signo)
            lista.insert(matrice)
            matrice.listarxFila()
            cotenido.append(matrice)
            matrice.graphOriginal(matrice)


        editor.delete(1.0, END)

    def info(self):
        messagebox.showinfo(message="KEVIN RAUL POZUELOS ESTRADA\n201800992\nIPC 2 SECCION : D",title="PROYECTO 2")