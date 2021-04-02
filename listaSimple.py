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
