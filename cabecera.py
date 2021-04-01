from Nodo import nodoDoble
#constructor de la lista de cabezeras
class cabezera:
    def __init__(self):
        self.head = None
        self.cont = 0
#Metodo de insercion de cabezeras (AL INICIO, AL CENTRO, AL FINAL)
    def crearCabezera(self, nuevo):
        if self.head is None:
            self.head = nuevo
        else:
            if nuevo.valor < self.head.valor:
                nuevo.sig = self.head
                self.head.ant = nuevo
                self.head = nuevo

            else:
                temp = self.head

                while temp.sig is not None:

                    if nuevo.valor < temp.sig.valor:
                        nuevo.sig = temp.sig
                        temp.sig.ant = nuevo
                        nuevo.ant = temp

                        return
                    temp = temp.sig

                if temp.sig is None:

                    temp.sig = nuevo
                    nuevo.ant = temp

#Retorna el numero de cabezaras

    def search(self, pos):
        aux = self.head
        while aux is not None:
            if aux.valor is pos:
                return aux
            aux = aux.sig
        return None



