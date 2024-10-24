from tkinter import *
from tkinter import ttk

<<<<<<< Updated upstream
def mostrar_resultados_ecuaciones():
=======
def mostrar_resultados_ecuaciones(matriz, x, y, z, tipo):
    # Crear la ventana Toplevel
>>>>>>> Stashed changes
    ventana_ecuaciones = Toplevel()
    ventana_ecuaciones.title("Resultados de Ecuaciones")
    ventana_ecuaciones.geometry("1366x768")
    
<<<<<<< Updated upstream
=======
    # Frame para los resultados
>>>>>>> Stashed changes
    frame_resultados = Frame(ventana_ecuaciones, width=500, height=768, bg="#274357")
    frame_resultados.place(x=0, y=0)

    label_resultados = Label(frame_resultados, text="Resultados", font=("Arial", 18), bg="#274357", fg="white")
<<<<<<< Updated upstream
    label_resultados.place(relx=0.5, y=20, anchor='center')
    label_matriz = Label(frame_resultados, text="Matriz original", font=("Arial", 16), bg="#274357", fg="white")
    label_matriz.place(relx=0.5, y=50, anchor='center')
    label_solucion = Label(frame_resultados, text="Solución:", font=("Arial", 16), bg="#274357", fg="white")
    label_solucion.place(relx=0.5, y=385, anchor='center')
    label_sistema = Label(frame_resultados, text="Tipo de sistema:", font=("Arial", 16), bg="#274357", fg="white")
    label_sistema.place(relx=0.5, y=535, anchor='center')


=======
    label_resultados.place(relx=0.3, y=20, anchor='center')
    label_matriz = Label(frame_resultados, text="Matriz original", font=("Arial", 16), bg="#274357", fg="white")
    label_matriz.place(relx=0.3, y=50, anchor='center')
    label_solucion = Label(frame_resultados, text="Solución:", font=("Arial", 16), bg="#274357", fg="white")
    label_solucion.place(relx=0.3, y=385, anchor='center')
    label_sistema = Label(frame_resultados, text="Tipo de sistema:", font=("Arial", 16), bg="#274357", fg="white")
    label_sistema.place(relx=0.3, y=535, anchor='center')

    # Etiquetas para variables
>>>>>>> Stashed changes
    label_x = Label(ventana_ecuaciones, text="X", font=("Arial", 24), fg="white", bg="#1F6680")
    label_x.place(x=291, y=144)
    label_y = Label(ventana_ecuaciones, text="Y", font=("Arial", 24), fg="white", bg="#1F6680")
    label_y.place(x=287, y=144)
    label_z = Label(ventana_ecuaciones, text="Z", font=("Arial", 24), fg="white", bg="#1F6680")
    label_z.place(x=355, y=144)
    label_i = Label(ventana_ecuaciones, text="I", font=("Arial", 24), fg="white", bg="#1F6680")
    label_i.place(x=447, y=144)

<<<<<<< Updated upstream
    #Entrys
    entry_x1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x1.place(x=204, y=172,width=70)
    entry_x2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x2.place(x=204, y=243,width=70)
    entry_x3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x3.place(x=204, y=314,width=70)

    entry_y1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y1.place(x=272, y=172,width=70)
    entry_y2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y2.place(x=272, y=243,width=70)
    entry_y3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y3.place(x=272, y=314,width=70)

    entry_z1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z1.place(x=340, y=172,width=70)
    entry_z2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z2.place(x=340, y=243,width=70)
    entry_z3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z3.place(x=340, y=314,width=70)

    entry_i1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i1.place(x=428, y=172,width=70)
    entry_i2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i2.place(x=428, y=243,width=70)
    entry_i3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i3.place(x=428, y=314,width=70)

    entry_solucion_x = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_x.place(x=248, y=455,width=70)
    entry_solucion_y = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_y.place(x=316, y=455,width=70)
    entry_solucion_z = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_z.place(x=384, y=455,width=70)

    entry_tipo_sistema = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_tipo_sistema.place(x=222, y=576,width=250)

    boton_salir = Button(frame_resultados, text="Salir", width=22, fg="White", font=("Arial", 14), bg="#274357", command=ventana_ecuaciones.destroy)
    boton_salir.place(relx=0.5, y=700, anchor='center')

    def mostrar_resultados_ecuaciones(matriz, x, y, z, tipo):
        # Código existente para crear la ventana
        # Asegúrate de actualizar las entradas para mostrar la matriz y las soluciones
        entry_x1.insert(0, str(matriz[0][0]))
        entry_y1.insert(0, str(matriz[0][1]))
        entry_z1.insert(0, str(matriz[0][2]))
        entry_i1.insert(0, str(matriz[0][3]))
        # Repite para las otras filas de la matriz
        # Inserta x, y, z en sus respectivas entradas
        if x is not None:
            entry_solucion_x.insert(0, str(x))
        if y is not None:
            entry_solucion_y.insert(0, str(y))
        if z is not None:
            entry_solucion_z.insert(0, str(z))
        entry_tipo_sistema.insert(0, tipo)
    ventana_ecuaciones.mainloop()
=======
    # Entradas para la matriz aumentada
    entry_x1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x1.place(x=204, y=172, width=70)
    entry_x2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x2.place(x=204, y=243, width=70)
    entry_x3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_x3.place(x=204, y=314, width=70)

    entry_y1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y1.place(x=272, y=172, width=70)
    entry_y2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y2.place(x=272, y=243, width=70)
    entry_y3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_y3.place(x=272, y=314, width=70)

    entry_z1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z1.place(x=340, y=172, width=70)
    entry_z2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z2.place(x=340, y=243, width=70)
    entry_z3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_z3.place(x=340, y=314, width=70)

    entry_i1 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i1.place(x=428, y=172, width=70)
    entry_i2 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i2.place(x=428, y=243, width=70)
    entry_i3 = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_i3.place(x=428, y=314, width=70)

    # Entradas para las soluciones
    entry_solucion_x = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_x.place(x=248, y=455, width=70)
    entry_solucion_y = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_y.place(x=316, y=455, width=70)
    entry_solucion_z = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_solucion_z.place(x=384, y=455, width=70)

    entry_tipo_sistema = Entry(ventana_ecuaciones, font=("Arial", 18))
    entry_tipo_sistema.place(x=222, y=576, width=250)

    # Botón para salir
    boton_salir = Button(frame_resultados, text="Salir", width=22, fg="White", font=("Arial", 14), bg="#274357", command=ventana_ecuaciones.destroy)
    boton_salir.place(relx=0.5, y=700, anchor='center')

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

>>>>>>> Stashed changes
