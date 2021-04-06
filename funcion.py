from tkinter import filedialog, messagebox,END, ttk
import xml.etree.ElementTree as ET
from listaSimple import listaMatriz
from matriz import matrix
from datetime import datetime
import os

class Funciones_:
    def __init__(self):
        self.archivo = ""
        self.cotenido = []
        self.lista = listaMatriz()
        self.listalogs = list()
        self.now = datetime.now()
    def nuevo(self,editor):
        editor.delete(1.0, END)
        self.archivo = ""

    def abrir(self, editor, combo):
        self.archivo = filedialog.askopenfilename(title="Abrir Archivo", initialdir="/home/")
        ruta = self.archivo
        tree = ET.parse(ruta)
        root = tree.getroot()
        f = 0
        c = 1
        self.espaciosLlenos = 0
        self.espaciosVacios = 0
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
            for j in range(len(element[3].text)):
                if cadena[j] == '*':
                    self.espaciosLlenos += 1
                    print(j)
                elif cadena[j] == '-':
                    self.espaciosVacios += 1
            self.listalogs.append([str(self.now), matrice.signo, self.espaciosLlenos, self.espaciosVacios])
            self.espaciosLlenos=0
            self.espaciosVacios=0
            print(matrice.signo)
            self.lista.insert(matrice)
            matrice.listarxFila()
            print(self.listalogs)
            matrice.graphOriginal(matrice)

            self.cotenido.append(matrice.signo)
            combo["values"] = self.cotenido
        editor.delete(1.0, END)




    def info(self):
        messagebox.showinfo(message="KEVIN RAUL POZUELOS ESTRADA\n201800992\nIPC 2 SECCION : D",title="PROYECTO 2")



    def reporte(self):
        contenido = ''
        htmFile = open("REPORTE" + ".html", "w")
        htmFile.write("""<!DOCTYPE HTML PUBLIC"
            <html>
            <head>
            <title>REPORTE</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>    
            </head>
            <body>
            <div class="container">
            <h2>Reporte de datos</h2>
            <p>Lista de arreglos</p>            
            <table class="table">
            <thead>
              <tr>
               <th>NOMBRE</th>
                <th>ESPACIOS LLENOS</th>
                <th>ESPACIOS VACIOS</th>
                <th>Fecha-Hora</th>
              </tr>
            </thead>

            """)
        for i in range(len(self.listalogs)):
            contenido += (" <tbody>"
                          "<td>" + str(self.listalogs[i][1]) + "</td>"
                          "<td>" + str(self.listalogs[i][2]) + "</td>"
                          "<td>" + str(self.listalogs[i][3]) + "</td>"
                          "<td>" + str(self.listalogs[i][0]) + "</td>"
                          "</tbody>")

        htmFile.write(contenido)
        htmFile.write("""</table>
                         </div>
                         </body>
                         </html>""")
        htmFile.close()
        os.startfile("REPORTE.html")
    def buscar(self, busqueda):
        e=(self.lista.buscar(busqueda))
        e.matriz.graphMatrizGirovertical