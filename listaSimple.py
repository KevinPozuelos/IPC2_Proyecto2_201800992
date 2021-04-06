from Nodo import nodoSimple

class listaMatriz:

    def __init__(self):
        self.inicio = None


    def insert(self, matriz):
        nuevo = nodoSimple(matriz)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            temp = self.inicio
            while temp.next is not None:
                temp = temp.next
            temp.next = nuevo


    def buscar(self, patron):
        aux = self.inicio

        while aux is not None:
            if aux.matriz.signo == patron:
                return aux

            aux = aux.next
        return None