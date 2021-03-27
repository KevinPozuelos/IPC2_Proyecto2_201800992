class Nodo:

    def __init__(self, valor="", fila="", columna=""):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.anteior = None
        self.arriba = None
        self.abajo = None