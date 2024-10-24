from fractions import Fraction
import sympy as sp
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from resultados_ecuaciones import mostrar_resultados_ecuaciones

#INTERFAZ GRÁFICA
def abrir_ecuaciones():
    ventana = Toplevel()
    ventana.geometry("800x600")
    ventana.title("Calculadora de ecuaciones lineales")
    ventana.configure(bg="#1F6680")

    label_titulo = Label(ventana, text="Sistemas de ecuaciones\nlineales", font=("Arial", 24), bg="#1F6680", fg="white")
    label_titulo.place(relx=0.5, y=50, anchor='center')

    #frame con label matriz
    frame_matriz = Frame(ventana, bg="#274357")
    frame_matriz.place(x=0, y=90, width=800, height=48)
    label_matriz = Label(frame_matriz, text="Determine la matriz 3x3 a trabajar", font=("Arial", 18), bg="#274357", fg="white")
    label_matriz.place(relx=0.5,rely=0.5, anchor='center')

    label_ecuacion1 = Label(ventana, text="Primera ecuación:", font=("Arial", 18), fg="white", bg="#1F6680")
    label_ecuacion1.place(x=137, y=238)
    label_ecuacion2 = Label(ventana, text="Segunda ecuación:", font=("Arial", 18), fg="white", bg="#1F6680")
    label_ecuacion2.place(x=137, y=309)
    label_ecuacion3 = Label(ventana, text="Tercera ecuación:", font=("Arial", 18), fg="white", bg="#1F6680")
    label_ecuacion3.place(x=137, y=380)

    label_x = Label(ventana, text="x", font=("Arial", 24), fg="white", bg="#1F6680")
    label_x.place(x=410, y=200)
    label_y = Label(ventana, text="y", font=("Arial", 24), fg="white", bg="#1F6680")
    label_y.place(x=478, y=200)
    label_z = Label(ventana, text="z", font=("Arial", 24), fg="white", bg="#1F6680")
    label_z.place(x=546, y=200)
    label_i = Label(ventana, text="i", font=("Arial", 24), fg="white", bg="#1F6680")
    label_i.place(x=634, y=200)

    #Entrys
    entry_x1 = Entry(ventana, font=("Arial", 18))
    entry_x1.place(x=390, y=238,width=70)
    entry_y1 = Entry(ventana, font=("Arial", 18))
    entry_y1.place(x=458, y=238,width=70)
    entry_z1 = Entry(ventana, font=("Arial", 18))
    entry_z1.place(x=526, y=238,width=70)
    entry_i1 = Entry(ventana, font=("Arial", 18))
    entry_i1.place(x=614, y=238,width=70)

    entry_x2 = Entry(ventana, font=("Arial", 18))
    entry_x2.place(x=390, y=309,width=70)
    entry_y2 = Entry(ventana, font=("Arial", 18))
    entry_y2.place(x=458, y=309,width=70)
    entry_z2 = Entry(ventana, font=("Arial", 18))
    entry_z2.place(x=526, y=309,width=70)
    entry_i2 = Entry(ventana, font=("Arial", 18))
    entry_i2.place(x=614, y=309,width=70)

    entry_x3 = Entry(ventana, font=("Arial", 18))
    entry_x3.place(x=390, y=380,width=70)
    entry_y3 = Entry(ventana, font=("Arial", 18))
    entry_y3.place(x=458, y=380,width=70)
    entry_z3 = Entry(ventana, font=("Arial", 18))
    entry_z3.place(x=526, y=380,width=70)
    entry_i3 = Entry(ventana, font=("Arial", 18))
    entry_i3.place(x=614, y=380,width=70)
    
    #frame separando la I
    frame_separador = Frame(ventana, bg="#274357")
    frame_separador.place(x=600, y=228, width=5, height=192)

    def resolver_sistema():
        # Inicialización de la matriz aumentada
        matriz_aumentada = [[0 for _ in range(4)] for _ in range(3)]

        # Obtener valores de las entradas para la primera ecuación
        x1 = solicitar_entrada(entry_x1)
        y1 = solicitar_entrada(entry_y1)
        z1 = solicitar_entrada(entry_z1)
        i1 = solicitar_entrada(entry_i1)

        # Obtener valores de las entradas para la segunda ecuación
        x2 = solicitar_entrada(entry_x2)
        y2 = solicitar_entrada(entry_y2)
        z2 = solicitar_entrada(entry_z2)
        i2 = solicitar_entrada(entry_i2)

        # Obtener valores de las entradas para la tercera ecuación
        x3 = solicitar_entrada(entry_x3)
        y3 = solicitar_entrada(entry_y3)
        z3 = solicitar_entrada(entry_z3)
        i3 = solicitar_entrada(entry_i3)

        # Comprobar que no haya entradas inválidas
        if None in (x1, y1, z1, i1, x2, y2, z2, i2, x3, y3, z3, i3):
            return  # Si hay un error en la entrada, se detiene la ejecución

        # Asignar los valores a la matriz aumentada
        matriz_aumentada[0] = [x1, y1, z1, i1]
        matriz_aumentada[1] = [x2, y2, z2, i2]
        matriz_aumentada[2] = [x3, y3, z3, i3]
        matriz_original = [fila[:] for fila in matriz_aumentada]

        # Mostrar la matriz inicial
        print("\nMatriz original:")
        mostrar_matriz(matriz_original)

        # Llamada al método de Gauss-Jordan
        solucion = gauss_jordan(matriz_aumentada)

        # Mostrar la matriz en forma escalonada reducida
        print("\nMatriz en forma escalonada reducida:")
        mostrar_matriz(solucion)

        # Determinar el tipo de sistema
        tipo = tipo_de_sistema(solucion)

        if tipo == "Compatible indeterminado":
            print("\nSistema compatible indeterminado, con soluciones infinitas.")
            x, y, z = solucionar_sistema_indeterminado(solucion)
            print("Soluciones:")
            print(f"x = {x}")
            print(f"y = {y}")
            print(f"z = {z}")

        elif tipo == "Compatible determinado":
            print("\nSistema compatible determinado")
            x = solucion[0][3]
            y = solucion[1][3]
            z = solucion[2][3]
            print("Soluciones:")
            print(f"Valor de x: {x}")
            print(f"Valor de y: {y}")
            print(f"Valor de z: {z}")

        else:
            print("\nEl sistema es incompatible. No tiene solución.")
            x, y, z = None, None, None

        mostrar_resultados_ecuaciones(matriz_original, x, y, z, tipo)

    def limpiar_campos(): 
        entry_x1.delete(0, END)
        entry_y1.delete(0, END)
        entry_z1.delete(0, END)
        entry_i1.delete(0, END)

        entry_x2.delete(0, END)
        entry_y2.delete(0, END)
        entry_z2.delete(0, END)
        entry_i2.delete(0, END)

        entry_x3.delete(0, END)
        entry_y3.delete(0, END)
        entry_z3.delete(0, END)
        entry_i3.delete(0, END)
        

    Boton_resolver = Button(ventana, text="Resolver", font=("Arial", 14), bg="White",width=10, command=resolver_sistema)
    Boton_resolver.place(x=528, y=538)
    boton_limpiar = Button(ventana, text="Limpiar", font=("Arial", 14), bg="White",width=10, command=limpiar_campos)
    boton_limpiar.place(x=388, y=538)
    boton_salir = Button(ventana, text="Salir", font=("Arial", 14), bg="White", command=ventana.destroy,width=10)
    boton_salir.place(x=669, y=538)


# Funciones auxiliares
    def mostrar_matriz(matriz):
        print("")
        for i, fila in enumerate(matriz):
            print(f"{str(fila[0]):>10} {str(fila[1]):>10} {str(fila[2]):>10} | {str(fila[3]):>10}")

    def solicitar_entrada(entry_widget):
        try:
            # Intentar convertir la entrada del widget Entry en una fracción
            valor = Fraction(entry_widget.get())
            return valor
        except ValueError:
            # Si ocurre un error, mostrar un cuadro de mensaje de error
            messagebox.showerror("Entrada inválida", "Por favor, ingrese un número válido (puede ser entero, fracción o decimal).")
            return None

    # Funciones de OEF
    def multiplicar_fila(matriz, indice_fila, k):
        for i in range(len(matriz[indice_fila])):
            matriz[indice_fila][i] *= k
        return matriz

    def intercambiar_filas(matriz, fila_1, fila_2):
        matriz[fila_1], matriz[fila_2] = matriz[fila_2], matriz[fila_1]
        return matriz

    def sumar_multiplo_fila(matriz, fila_destino, fila_fuente, k):
        for i in range(len(matriz[fila_destino])):
            matriz[fila_destino][i] += matriz[fila_fuente][i] * k
        return matriz

    # Funciones de desarrollo
    def gauss_jordan(matriz):
        filas = len(matriz)
        
        for i in range(filas):
            # Paso 1: Verificar si ya hay un 1 en la columna i
            fila_con_uno = None
            for j in range(i, filas):
                if matriz[j][i] == 1:
                    fila_con_uno = j
                    break
            
            # Si existe un 1 en la columna i, intercambiar filas para aprovecharlo
            if fila_con_uno is not None and fila_con_uno != i:
                intercambiar_filas(matriz, i, fila_con_uno)
                print(f"\nIntercambiando fila {i + 1} con fila {fila_con_uno + 1} (aprovechando el 1):")
                mostrar_matriz(matriz)
            
            # Si no hay un 1, asegurarse de no usar un 0 como pivote
            if matriz[i][i] == 0:
                # Buscar una fila con un valor no nulo en la columna i
                for j in range(i + 1, filas):
                    if matriz[j][i] != 0:
                        intercambiar_filas(matriz, i, j)
                        print(f"\nIntercambiando fila {i + 1} con fila {j + 1} (evitar pivote 0):")
                        mostrar_matriz(matriz)
                        break

            # Hacer que el pivote sea 1 si no lo es ya
            if matriz[i][i] != 1 and matriz[i][i] != 0:
                multiplicador = Fraction(1, matriz[i][i])
                multiplicar_fila(matriz, i, multiplicador)
                print(f"\nMultiplicando fila {i + 1} por {multiplicador}:")
                mostrar_matriz(matriz)

            # Paso 2: Hacer ceros en la columna i para todas las filas por encima y por debajo
            for j in range(filas):
                if j != i:
                    k = -matriz[j][i]
                    if k != 0:  # Evitar hacer operaciones si el valor ya es 0
                        sumar_multiplo_fila(matriz, j, i, k)
                        print(f"\nSumando {k} veces fila {i + 1} a fila {j + 1}:")
                        mostrar_matriz(matriz)

        return matriz

    def tipo_de_sistema(matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        
        # Contar filas no nulas
        filas_no_nulas = 0
        for i in range(filas):
            if any(matriz[i][j] != 0 for j in range(columnas - 1)):  # Ignorar la columna de igualdad
                filas_no_nulas += 1

        # Comprobar la última columna para determinar si hay contradicciones
        for i in range(filas):
            if all(matriz[i][j] == 0 for j in range(columnas - 1)) and matriz[i][columnas - 1] != 0:
                return "Incompatible"

        # Si hay filas no nulas igual a número de variables, es Compatible determinado
        if filas_no_nulas == columnas - 1:
            return "Compatible determinado"
        
        # Si hay filas no nulas menor a número de variables, es Compatible indeterminado
        return "Compatible indeterminado"

    def solucionar_sistema_indeterminado(matriz):
        # Definir la variable libre z como simbólica
        z = sp.Symbol('t')
        
        # Convertimos los elementos de la matriz a expresiones simbólicas
        y = sp.Rational(matriz[1][3]) - sp.Rational(matriz[1][2]) * z
        x = sp.Rational(matriz[0][3]) - sp.Rational(matriz[0][2]) * z - sp.Rational(matriz[0][1]) * y
        
        return x, y, z
