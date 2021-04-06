#Nodo de la matriz ortogonal
class nodoOrtogonal:

    def __init__(self, contenido, x=None, y=None):
        self.contenido = contenido
        self.x = x
        self.y = y
        self.derecho = self.izquierdo = self.arriba = self.abajo = None
#Nodo de la lista doblemente enlazada
class nodoDoble:

    def __init__(self, valor):
        self.valor = valor
        self.sig = None
        self.ant = None
        self.access = None

#Nodo de lista simplemente enlazada
class nodoSimple:

    def __init__(self, matriz):
        self.matriz = matriz

        self.next = None