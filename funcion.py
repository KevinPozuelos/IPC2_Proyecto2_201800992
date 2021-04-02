from tkinter import filedialog, messagebox,END, INSERT
import xml.etree.ElementTree as ET
from listaSimple import listaMatriz
from matriz import matrix
lista = listaMatriz()


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
        for element in root:
            matrice = matrix(element[0].text, element[1].text, element[3].text)





        editor.delete(1.0, END)

    def info(self):
        messagebox.showinfo(message="KEVIN RAUL POZUELOS ESTRADA\n201800992\nIPC 2 SECCION : D",title="PROYECTO 2")