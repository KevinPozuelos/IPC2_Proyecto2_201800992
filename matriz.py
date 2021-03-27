from Nodo import *
class Matriz:
    def __init__(self, matriz):
        # Aca inicializamos la cabecera y le agregamos el nombre de la matriz
        self.cabecera = Nodo()
        self.valor = matriz

    def insertarNodo(self, valor, row, column):
        # Aca inicializamos los nodos para filas, columnas y el cuerpo
        fila = Nodo()
        columna = Nodo()
        cuerpo = Nodo()

        # ------------------------- Creamos datos de usuario -------------------

        cuerpo.valor = valor
        # ---------------------- Buscamos fila y columna --------------------
        columna = self.buscarColumna(column, self.cabecera)
        fila = self.buscarFila(row, self.cabecera)
        # -------------------- Creamos los deptos y empresas --------------------
        if columna == None:
            columna = self.insertarColumna(column)
        if fila == None:
            fila = self.insertarFila(row)

        # ---------------- Creamos los nodos de las columnas---------------
        # ------------- Creamos al inicio de columnas ------------------------

        if columna.abajo == None:
                columna.abajo = cuerpo
                cuerpo.arriba = columna

        elif fila.abajo == None:
            auxiliar = columna.abajo
            while auxiliar.abajo != None:
                auxiliar = auxiliar.abajo

            auxiliar.abajo = cuerpo
            cuerpo.arriba = auxiliar
        else:
            auxiliar = columna
            condicionB = True

            while condicionB:
                auxiliar = auxiliar.abajo
                auxiliarFila = auxiliar
                while auxiliarFila.anterior != None:
                    auxiliarFila = auxiliarFila.anterior

                while auxiliarFila.arriba != None:
                    if auxiliarFila.fila == row:
                        cuerpo.abajo = auxiliar
                        cuerpo.arriba = auxiliar.arriba
                        auxiliar.arriba.abajo = cuerpo
                        auxiliar.arriba = cuerpo
                        break
                    auxiliarFila = auxiliarFila.arriba

                if auxiliar.abajo != None and cuerpo.arriba == None:
                    condicionB = False

            if cuerpo.arriba == None:
                auxiliar.abajo = cuerpo
                auxiliar.arriba = auxiliar

                # ---------------- Creamos los nodos de las filas--------------------
                # ------------- Creamos al inicio de filas ---------------------------

                if fila.siguiente == None:
                    fila.siguiente = cuerpo
                    cuerpo.anterior = fila

                    # ------------- Creamos al final de filas ----------------------------
                elif columna.siguiente == None:
                    auxiliar = fila.siguiente
                    while auxiliar.siguiente != None:
                        auxiliar = auxiliar.siguiente

                    auxiliar.siguiente = cuerpo
                    cuerpo.anterior = auxiliar

                    # ------------------ Creamos enmedio de filas ----------------------
                else:
                    auxiliar = fila
                    condicionB = True


                    while condicionB:
                        auxiliar = auxiliar.siguiente
                        auxiliarColumna = auxiliar

                        while auxiliarColumna.arriba != None:
                            auxiliarColumna = auxiliarColumna.arriba

                        while auxiliarColumna.anterior != None:
                            if column == auxiliarColumna.columna:
                                cuerpo.siguiente = auxiliar
                                cuerpo.anterior = auxiliar.anterior
                                auxiliar.anterior.siguiente = cuerpo
                                auxiliar.anterior = cuerpo
                                break
                            auxiliarColumna = auxiliarColumna.anterior

                        if (auxiliar.siguiente != None) and (cuerpo.anterior == None):
                            condicionB = False

                    if cuerpo.anterior == None:
                        auxiliar.siguiente = cuerpo
                        cuerpo.anterior = auxiliar

            # /************************** Cabecera Filas ***********************************/

    def insertarFila(self, fila):
        filaAux = Nodo()
        filaAux.fila = fila

        auxiliar = self.cabecera

        while auxiliar.abajo != None:
            auxiliar = auxiliar.abajo

        auxiliar.abajo = filaAux
        filaAux.arriba = auxiliar

        return filaAux


    def insertarColumna(self, columna):
        columnaAux = Nodo()
        columnaAux.columna = columna

        auxiliar = self.cabecera

        while auxiliar.siguiente != None:
            auxiliar = auxiliar.siguiente

        auxiliar.siguiente = columnaAux
        columnaAux.anterior = auxiliar

        return columnaAux


    # /************************** Buscar fila ************************************/
    def buscarFila(self, fila, ini):
        auxiliar = ini
        while auxiliar != None:
            if auxiliar.fila == fila:
                return auxiliar
            else:
                auxiliar = auxiliar.abajo
        return None

        # /************************** Buscar columna *************************************/
    def buscarColumna(self, columna, ini):
        auxiliar = ini
        while auxiliar != None:
            if auxiliar.columna == columna:
                return auxiliar
            else:
                auxiliar = auxiliar.siguiente
        return None