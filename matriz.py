import os

from cabecera import *
from Nodo import nodoOrtogonal, nodoDoble
class matrix:

    def __init__(self, signo, fila, columna):

        self.signo = signo
        self.fila = fila
        self.columna = columna
        self.lista_horizontal = cabezera()
        self.lista_vertical = cabezera()

    def nuevoNodo(self, signo, x, y):
        nuevo = nodoOrtogonal(signo, x, y)
        fila = self.lista_horizontal.search(x)
        if fila is None:
            fila = nodoDoble(x)
            fila.access = nuevo
            self.lista_horizontal.crearCabezera(fila)
        else:
            if nuevo.y < fila.access.y:
                nuevo.derecho = fila.access
                fila.access.izquierdo = nuevo
                fila.acess = nuevo

            else:
                temp = fila.access
                while temp.derecho is not None:
                    if nuevo.y < temp.derecho.y:
                        nuevo.derecho = temp.derecho
                        temp.derecho.izquierdo = temp
                        temp.derecho = nuevo
                        return
                    temp = temp.derecho

                if temp.derecho is None:
                    temp.derecho = nuevo
                    nuevo.izquierdo = temp

        columna = self.lista_vertical.search(y)
        if columna is None:
            columna = nodoDoble(y)
            self.lista_vertical.crearCabezera(columna)
            columna.access = nuevo

        else:

            temp = columna.access
            while temp.abajo is not None:
                if nuevo.x < temp.abajo.x:
                    nuevo.abajo = temp.abajo
                    temp.abajo.arriba = nuevo
                    nuevo.arriba = temp
                    temp.abajo = nuevo
                    return
                temp = temp.abajo

            if temp.abajo is None:
                temp.abajo = nuevo
                nuevo.arriba = temp



    def listarxFila(self):
        fila = self.lista_horizontal.head
        print("FILAS")
        while fila is not None:
            print('fila' + str(fila.valor))
            aux = fila.access
            while aux is not None:
                print(aux.contenido + '  ' + str(aux.x) +' , '+str(aux.y))
                aux = aux.derecho

            fila = fila.sig

    def graphMatrizGirovertical(self):
        grafo = "digraph"
        grafo += "{\nnode[shape=record];\n"
        grafo += str("graph[pencolor=transparent];\n")
        grafo += str("node [style=filled];\n")
        filas = self.lista_horizontal.head
        while filas is not None:
            aux = filas.access
            while aux is not None:
                grafo += str("p"+str(aux.x)+str(aux.y)+"[label=\"{<data>"+str(aux.y)+","+str(aux.x)+"|<next>"+str(aux.contenido)+"}\" pos=\""+str(aux.x)+","+str(aux.y)+"!\"];\n")
                aux = aux.derecho
            filas = filas.sig
        grafo += str("}\n")
        f = open("ejemplo.dot", "w+")
        f.write(grafo)
        f.close()
        os.system("fdp -Tpng -o graph-g.png ejemplo.dot")

    def graphMatrizGirohorizonal(self):
        grafo = "digraph"
        grafo += "{\nnode[shape=record];\n"
        grafo += str("graph[pencolor=transparent];\n")
        grafo += str("node [style=filled];\n")
        filas = self.lista_horizontal.head
        while filas is not None:
            aux = filas.access
            while aux is not None:
                grafo += str("p"+str(aux.x)+str(aux.y)+"[label=\"{<data>"+str(aux.x)+","+str(aux.y)+"|<next>"+str(aux.contenido)+"}\" pos=\""+str(aux.x)+","+str(aux.y)+"!\"];\n")
                aux = aux.derecho
            filas = filas.sig
        grafo += str("}\n")
        f = open("ejemplo.dot", "w+")
        f.write(grafo)
        f.close()
        os.system("fdp -Tpng -o graph-g.png ejemplo.dot")

    def graphOriginal(self, matrice):
        f = self.fila
        c = self.columna
        n = self.signo
        grafo = "digraph"
        grafo += "{\nnode[shape=record];\n"
        grafo += str("graph[pencolor=transparent];\n")
        grafo += str("node [style=filled];\n")

        for y in range(1, c + 1):
            for x in range(1, f + 1):
                grafo += str("p" + str(x) + str(y) + "[label=\"{<data>" + str(x) + "," + str(
                    y) + "|<next>" + str(matrice.busquedaPorCoordenada(y, x)) + "}\" pos=\"" + str(x) + "," + str(
                    self.columna - y) + "!\"];\n")
        try:
            grafo += "Inicio[label=\"" + n + "\"]\n"
            grafo += str("}\n")
            dot = str(n + ".dot")
            f = open(dot, "w")
            f.write(grafo)
            f.close()
            os.system("fdp -Tpng " + dot + " -o " + n + ".png")
        except Exception:
            print("error")



    def busquedaPorCoordenada(self, fila, columna):
        cabeceraF = self.lista_horizontal.head
        while cabeceraF is not None:
            aux = cabeceraF.access
            while aux is not None:
                if aux.x == fila and aux.y == columna:
                    return aux.contenido
                aux = aux.derecho
            cabeceraF = cabeceraF.sig

