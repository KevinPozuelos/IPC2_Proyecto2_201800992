from tkinter import *
from tkinter import ttk,scrolledtext,Frame,Scrollbar,Canvas,Menu,Tk,VERTICAL
from matriz import *
from listaSimple import *
from funcion import Funciones_
class interface:

    def __init__(self, ventana):
        #########################__contenedor principal__################################
        self.root = ventana
        self.crearventana()

    def crearventana(self):
        function = Funciones_()
        contenedor = self.root
        contenedor.title("PROYECTO 2 -> 201800992")

        #########################__ScrollBar de ventanas__#######################
        contenedorPrincipal = Frame(contenedor, bg="OliveDrab1")
        estilos = Canvas(contenedorPrincipal, bg="OliveDrab1")
        scrolBar = Scrollbar(contenedorPrincipal, orient=VERTICAL, command=estilos.yview)
        scrol = Frame(estilos, bg="OliveDrab1")

        #########################__Configuracion de scrollBar en ventanas__#######################
        scrol.bind("<Configure>", lambda e: estilos.configure(scrollregion=estilos.bbox("all")))
        estilos.create_window((0, 0), window=scrol, anchor="nw")
        estilos.configure(yscrollcommand=scrolBar.set, width=1572, height=635)

        ttk.Label(scrol, text="MATRIZ", font=("Arial", 17), background='OliveDrab1', foreground="gray").grid(column=0, row=0)
        ttk.Label(scrol, text="ORIGINAL", font=("Arial", 17), background='OliveDrab1', foreground="gray").grid(column=0,row=1)
        ttk.Label(scrol, text="RESULTADO", font=("Arial", 17), background='OliveDrab1', foreground="gray").grid(column=1, row=0)
        ttk.Label(scrol, text="OPERACOIN", font=("Arial", 17), background='OliveDrab1', foreground="gray").grid(column=1,row=1)

        editor = scrolledtext.ScrolledText(scrol, undo=True, width=80, height=28, font=("Arial", 12),background="mint cream", foreground="black")
        editor.grid(column=0, row=2, pady=25, padx=25)

        consola = scrolledtext.ScrolledText(scrol, undo=True, width=80, height=28, font=("Arial", 12),background="black", foreground="white")
        consola.grid(column=1, row=2, pady=25, padx=25)

        #########################__Barra de herramientas__#######################
        barraHerramientas = Menu(contenedor)
        contenedor.config(menu=barraHerramientas, width=1572, height=635)
        ######################__abrir archivo y guardar matricez__#################
        opcionArchivo = Menu(barraHerramientas, tearoff=0)
        opcionArchivo.add_command(label="CARGAR XML", command=lambda: function.abrir(editor))
        #####################__OPERACIONES CON MATRICES__###########################
        opcionReporte = Menu(barraHerramientas, tearoff=0)
        opcionReporte.add_command(label="OPERACIONES", command=lambda: function.abrir(editor))
        ####################__informacion__##########################################
        informacion = Menu(barraHerramientas, tearoff=0)
        informacion.add_command(label="Informacion del estudiante", command=lambda: function.info())
        informacion.add_command(label="Documentacion", command=lambda: function.info())

        barraHerramientas.add_cascade(label="Archivo", menu=opcionArchivo)
        barraHerramientas.add_cascade(label="Operaciones", menu=opcionReporte)
        barraHerramientas.add_cascade(label="Reportes", menu=opcionReporte)
        barraHerramientas.add_cascade(label="Ayuda", menu=informacion)
        contenedorPrincipal.grid(sticky="news")
        estilos.grid(row=0, column=1)
        scrolBar.grid(row=0, column=2, sticky="ns")
        editor.focus()