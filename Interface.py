from tkinter import *
#Creacion de la raiz para realizar la interfaz grafica.
root = Tk()
root.title("Principal")

#Configuracion basica de la interfaz grafica.



#Creacion del Frame
frame = Frame(root, width="1000", height="500")
frame.pack()
frame.config(bg="grey")
frame.config(bd="25")
frame.config(relief="sunken")
frame.config(cursor="hand2")

#bottons
btnCargar = Button(frame, text="Cargar archivo")
btnCargar.grid(row="1", column="0", padx="10", pady="10")
btnOperaciones = Button(frame, text="Operaciones")
btnOperaciones.grid(row="1", column="1",  padx="10", pady="10")
btnReporte = Button(frame, text="Reporte")
btnReporte.grid(row="1", column="2",  padx="10", pady="10")
btnAyuda = Button(frame, text="Ayuda")
btnAyuda.grid(row="1", column="3",  padx="10", pady="10")

#Se ejecuta la interfaz.
root.mainloop()
