from fractions import Fraction
import sympy as sp
from tkinter import *
from tkinter import messagebox
from resultados_ecuaciones import mostrar_resultados_ecuaciones


def abrir_ecuaciones():
    # INTERFAZ GRÁFICA
    ventana = Toplevel()
    ventana.geometry("800x600")
    ventana.title("Calculadora de ecuaciones lineales")
    ventana.configure(bg="#1F6680")

    label_titulo = Label(ventana, text="Sistemas de ecuaciones\nlineales", font=("Arial", 24), bg="#1F6680", fg="white")
    label_titulo.place(relx=0.5, y=50, anchor='center')

    # frame con label matriz
    frame_matriz = Frame(ventana, bg="#274357")
    frame_matriz.place(x=0, y=90, width=800, height=48)
    label_matriz = Label(frame_matriz, text="Determine la matriz 3x3 a trabajar", font=("Arial", 18), bg="#274357", fg="white")
    label_matriz.place(relx=0.5, rely=0.5, anchor='center')

    label_ecuacion1 = Label(ventana, text="Primera ecuación:", font=("Arial", 18), fg="white", bg="#1F6680")
    label_ecuacion1.place(x=137, y=238)
    label_ecuacion2 = Label(ventana, text="Segunda ecuación:", font=("Arial", 18), fg="white", bg="#1F6680")
    label_ecuacion2.place(x=137, y=309)
    label_ecuacion3 = Label(ventana, text="Tercera ecuación:", font=("Arial", 18), fg="white", bg="#1F6680")
    label_ecuacion3.place(x=137, y=380)

    label_x = Label(ventana, text="X", font=("Arial", 24), fg="white", bg="#1F6680")
    label_x.place(x=410, y=200)
    label_y = Label(ventana, text="Y", font=("Arial", 24), fg="white", bg="#1F6680")
    label_y.place(x=478, y=200)
    label_z = Label(ventana, text="Z", font=("Arial", 24), fg="white", bg="#1F6680")
    label_z.place(x=546, y=200)
    label_i = Label(ventana, text="I", font=("Arial", 24), fg="white", bg="#1F6680")
    label_i.place(x=634, y=200)

    # Entradas para coeficientes y términos independientes
    entry_x1 = Entry(ventana, font=("Arial", 18))
    entry_x1.place(x=390, y=238, width=70)
    entry_x2 = Entry(ventana, font=("Arial", 18))
    entry_x2.place(x=390, y=309, width=70)
    entry_x3 = Entry(ventana, font=("Arial", 18))
    entry_x3.place(x=390, y=380, width=70)

    entry_y1 = Entry(ventana, font=("Arial", 18))
    entry_y1.place(x=458, y=238, width=70)
    entry_y2 = Entry(ventana, font=("Arial", 18))
    entry_y2.place(x=458, y=309, width=70)
    entry_y3 = Entry(ventana, font=("Arial", 18))
    entry_y3.place(x=458, y=380, width=70)

    entry_z1 = Entry(ventana, font=("Arial", 18))
    entry_z1.place(x=526, y=238, width=70)
    entry_z2 = Entry(ventana, font=("Arial", 18))
    entry_z2.place(x=526, y=309, width=70)
    entry_z3 = Entry(ventana, font=("Arial", 18))
    entry_z3.place(x=526, y=380, width=70)

    entry_i1 = Entry(ventana, font=("Arial", 18))
    entry_i1.place(x=614, y=238, width=70)
    entry_i2 = Entry(ventana, font=("Arial", 18))
    entry_i2.place(x=614, y=309, width=70)
    entry_i3 = Entry(ventana, font=("Arial", 18))
    entry_i3.place(x=614, y=380, width=70)

    # Frame separando la I
    frame_separador = Frame(ventana, bg="#274357")
    frame_separador.place(x=600, y=228, width=5, height=192)

    # Función para resolver las ecuaciones
    def resolver_ecuaciones():
        # Inicialización de la matriz aumentada
        matriz_aumentada = [[0 for _ in range(4)] for _ in range(3)]

        # Obtener los valores de los Entry y convertirlos a Fracción
        try:
            matriz_aumentada[0][0] = Fraction(entry_x1.get())
            matriz_aumentada[0][1] = Fraction(entry_y1.get())
            matriz_aumentada[0][2] = Fraction(entry_z1.get())
            matriz_aumentada[0][3] = Fraction(entry_i1.get())

            matriz_aumentada[1][0] = Fraction(entry_x2.get())
            matriz_aumentada[1][1] = Fraction(entry_y2.get())
            matriz_aumentada[1][2] = Fraction(entry_z2.get())
            matriz_aumentada[1][3] = Fraction(entry_i2.get())

            matriz_aumentada[2][0] = Fraction(entry_x3.get())
            matriz_aumentada[2][1] = Fraction(entry_y3.get())
            matriz_aumentada[2][2] = Fraction(entry_z3.get())
            matriz_aumentada[2][3] = Fraction(entry_i3.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese solo números válidos.")
            return

        # Mostrar la matriz ingresada
        mostrar_matriz(matriz_aumentada)

        # Llamada al método de Gauss-Jordan
        solucion = gauss_jordan(matriz_aumentada)

        # Mostrar la matriz en forma escalonada reducida
        print("\nMatriz en forma escalonada reducida:")
        mostrar_matriz(solucion)

        # Determinar el tipo de sistema
        tipo = tipo_de_sistema(solucion)

        # Mostrar resultados
        if tipo == "Compatible indeterminado":
            x, y, t = solucionar_sistema_indeterminado(solucion)
            mostrar_resultados_ecuaciones(solucion, x, y, t, tipo)
        elif tipo == "Compatible determinado":
            x, y, z = solucion[0][3], solucion[1][3], solucion[2][3]
            mostrar_resultados_ecuaciones(solucion, x, y, z, tipo)
        else:
            mostrar_resultados_ecuaciones(solucion, None, None, None, tipo)

    # Botones
    Boton_resolver = Button(ventana, text="Resolver", font=("Arial", 14), bg="White", width=10, command=resolver_ecuaciones)
    Boton_resolver.place(x=528, y=538)
    boton_limpiar = Button(ventana, text="Limpiar", font=("Arial", 14), bg="White", width=10)
    boton_limpiar.place(x=388, y=538)
    boton_salir = Button(ventana, text="Salir", font=("Arial", 14), bg="White", command=ventana.destroy, width=10)
    boton_salir.place(x=669, y=538)

# Funciones auxiliares
def mostrar_matriz(matriz):
    print("")
    for fila in matriz:
        print(f"{str(fila[0]):>10} {str(fila[1]):>10} {str(fila[2]):>10} | {str(fila[3]):>10}")

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
        # Paso 1: Verificar si el pivote es cero
        if matriz[i][i] == 0:
            for j in range(i + 1, filas):
                if matriz[j][i] != 0:
                    intercambiar_filas(matriz, i, j)
                    break

        # Después del intercambio, verifica nuevamente el pivote
        if matriz[i][i] == 0:
            # Si no se puede encontrar un pivote, el sistema es incompatible
            continue  # O podrías lanzar un mensaje de error aquí

        # Paso 2: Normalizar el pivote
        pivote = matriz[i][i]
        matriz = multiplicar_fila(matriz, i, Fraction(1, pivote))

        # Paso 3: Eliminar las filas debajo del pivote
        for j in range(i + 1, filas):
            matriz = sumar_multiplo_fila(matriz, j, i, -matriz[j][i])

    # Paso 4: Volver a la matriz en forma escalonada reducida
    for i in range(filas - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            matriz = sumar_multiplo_fila(matriz, j, i, -matriz[j][i])

    return matriz


def tipo_de_sistema(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    # Contar el número de filas no nulas
    filas_no_nulas = sum(1 for fila in matriz if any(x != 0 for x in fila[:-1]))

    # Determinar el tipo de sistema
    if filas_no_nulas == columnas - 1:
        return "Compatible determinado"
    elif filas_no_nulas < columnas - 1:
        return "Compatible indeterminado"
    else:
        return "Incompatible"

def solucionar_sistema_indeterminado(matriz):
    # Obtener la solución del sistema indeterminado
    # Esto es un ejemplo, puede que necesites una solución específica
    x = sp.symbols('x')
    y = sp.symbols('y')
    return x, y, sp.Symbol('t')


