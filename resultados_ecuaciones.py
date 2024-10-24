from tkinter import *
from tkinter import ttk

def mostrar_resultados_ecuaciones(matriz, x, y, z, tipo):
    # Crear la ventana Toplevel
    ventana_ecuaciones = Toplevel()
    ventana_ecuaciones.title("Resultados de Ecuaciones")
    ventana_ecuaciones.geometry("800x768")
    
    # Frame para los resultados
    frame_resultados = Frame(ventana_ecuaciones, width=800, height=768, bg="#274357")
    frame_resultados.place(x=0, y=0)

    label_resultados = Label(frame_resultados, text="Resultados", font=("Arial", 18), bg="#274357", fg="white")
    label_resultados.place(relx=0.5, y=50, anchor='center')
    label_matriz = Label(frame_resultados, text="Matriz original", font=("Arial", 16), bg="#274357", fg="white")
    label_matriz.place(relx=0.5, y=80, anchor='center')
    label_solucion = Label(frame_resultados, text="Solución:", font=("Arial", 16), bg="#274357", fg="white")
    label_solucion.place(relx=0.5, y=385, anchor='center')
    label_sistema = Label(frame_resultados, text="Tipo de sistema:", font=("Arial", 16), bg="#274357", fg="white")
    label_sistema.place(relx=0.5, y=535, anchor='center')

    label_x = Label(frame_resultados,text="X", font=("Arial", 18), bg="#274357", fg="white")
    label_x.place(x=236, y=120, width=70)
    label_y = Label(frame_resultados,text="Y", font=("Arial", 18), bg="#274357", fg="white")
    label_y.place(x=305, y=120, width=70)
    label_z = Label(frame_resultados,text="Z", font=("Arial", 18), bg="#274357", fg="white")
    label_z.place(x=373, y=120, width=70)
    label_i = Label(frame_resultados,text="I", font=("Arial", 18), bg="#274357", fg="white")
    label_i.place(x=443, y=120, width=70)

    label_xs = Label(frame_resultados,text="X", font=("Arial", 18), bg="#274357", fg="white")
    label_xs.place(x=280, y=420, width=70)
    label_ys = Label(frame_resultados,text="Y", font=("Arial", 18), bg="#274357", fg="white")
    label_ys.place(x=350, y=420, width=70)
    label_zs = Label(frame_resultados,text="Z", font=("Arial", 18), bg="#274357", fg="white")
    label_zs.place(x=420, y=420, width=70)

    # Entradas para la matriz aumentada
    entry_x1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x1.place(x=234, y=172, width=70)
    entry_x2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x2.place(x=234, y=243, width=70)
    entry_x3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x3.place(x=234, y=314, width=70)

    entry_y1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y1.place(x=302, y=172, width=70)
    entry_y2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y2.place(x=302, y=243, width=70)
    entry_y3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y3.place(x=302, y=314, width=70)

    entry_z1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z1.place(x=370, y=172, width=70)
    entry_z2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z2.place(x=370, y=243, width=70)
    entry_z3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z3.place(x=370, y=314, width=70)

    entry_i1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i1.place(x=458, y=172, width=70)
    entry_i2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i2.place(x=458, y=243, width=70)
    entry_i3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i3.place(x=458, y=314, width=70)

    # Entradas para las soluci4nes
    entry_solucion_x = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_x.place(x=274, y=455, width=70)
    entry_solucion_y = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_y.place(x=344, y=455, width=70)
    entry_solucion_z = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_z.place(x=414, y=455, width=70)

    entry_tipo_sistema = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_tipo_sistema.place(x=234, y=576, width=300)

    # Botón para salir
    boton_salir = Button(frame_resultados, text="Salir", width=22, fg="White", font=("Arial", 14), bg="#274357", command=ventana_ecuaciones.destroy)
    boton_salir.place(relx=0.5, y=680, anchor='center')

    # Llenar las entradas con la matriz y soluciones
    entry_x1.insert(0, str(matriz[0][0]))
    entry_y1.insert(0, str(matriz[0][1]))
    entry_z1.insert(0, str(matriz[0][2]))
    entry_i1.insert(0, str(matriz[0][3]))

    entry_x2.insert(0, str(matriz[1][0]))
    entry_y2.insert(0, str(matriz[1][1]))
    entry_z2.insert(0, str(matriz[1][2]))
    entry_i2.insert(0, str(matriz[1][3]))

    entry_x3.insert(0, str(matriz[2][0]))
    entry_y3.insert(0, str(matriz[2][1]))
    entry_z3.insert(0, str(matriz[2][2]))
    entry_i3.insert(0, str(matriz[2][3]))

    # Mostrar soluciones si existen
    if x is not None:
        entry_solucion_x.insert(0, str(x))
    if y is not None:
        entry_solucion_y.insert(0, str(y))
    if z is not None:
        entry_solucion_z.insert(0, str(z))

    # Insertar el tipo de sistema en su entrada correspondiente
    entry_tipo_sistema.insert(0, tipo)

    # Ejecutar el loop principal para la ventana
    ventana_ecuaciones.mainloop()
