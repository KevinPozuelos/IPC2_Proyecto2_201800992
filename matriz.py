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
                print(aux.contenido + str(aux.x)+str(aux.y))
                aux = aux.derecho
            fila = fila.sig


