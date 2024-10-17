import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from tkinter import *
from tkinter import messagebox

# Función para verificar si el número es negativo (para mostrarlo con paréntesis)
def negativo(variable):
    if variable < 0:
        return f"({variable})"
    return variable 

# Función cuadrática
def funcion_cuadratica(a, b, c, x):
    return a * x**2 + b * x + c

# Evaluar función cuadrática para la integración
def evaluar_funcion_cuadratica(x):
    return funcion_cuadratica(a, b, c, x)

# Función para graficar desde la interfaz
def graficar():
    try:
        # Obtener valores desde los campos de entrada
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())
        cant_rectangulos = int(entry_rectangulos.get())

        if x1 >= x2:
            messagebox.showerror("Error", "El límite izquierdo debe ser menor que el derecho")
            return

        # Graficar la función cuadrática
        x_values = np.linspace(x1 - 1, x2 + 1, 400)
        y_values = funcion_cuadratica(a, b, c, x_values)

        plt.plot(x_values, y_values, label=f'f(x) = {negativo(a)}x² + {negativo(b)}x + {negativo(c)}', color='blue')

        # Área con rectángulos
        intervalo_rectangulo = (x2 - x1) / cant_rectangulos
        intervalo_inicial = x1
        area_inferior = 0
        area_superior = 0

        for i in range(1, cant_rectangulos + 1):
            intervalo_final = intervalo_inicial + intervalo_rectangulo

            # Valores para el área
            y_inferior = funcion_cuadratica(a, b, c, intervalo_inicial)
            y_superior = funcion_cuadratica(a, b, c, intervalo_final)

            # Rellenar el área inferior en rojo
            plt.fill_between([intervalo_inicial, intervalo_final], 0, y_inferior, color='red', alpha=1)

            # Rellenar el área superior en azul
            plt.fill_between([intervalo_inicial, intervalo_final], y_superior, 0, color='blue', alpha=0.7)

            # Cálculo de áreas
            area_inferior += (intervalo_final - intervalo_inicial) * y_inferior
            area_superior += (intervalo_final - intervalo_inicial) * y_superior
            intervalo_inicial = intervalo_final

        # Calcular el área real usando integración numérica
        area_real, error_integral = quad(lambda x: funcion_cuadratica(a, b, c, x), x1, x2)

        # Calcular los errores
        error_inferior = area_real - area_inferior
        error_superior = area_real - area_superior

        # Mostrar resultados de áreas y errores
        messagebox.showinfo("Resultado", 
                            f"El área de la región está entre: {area_inferior:.2f} y {area_superior:.2f}\n"
                            f"El área real bajo la curva es: {area_real:.2f}\n"
                            f"Error con el área inferior: {error_inferior:.2f}\n"
                            f"Error con el área superior: {error_superior:.2f}")

        # Configurar gráficos
        plt.title('Gráfico de la Función Cuadrática')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.axhline(0, color='darkgray', lw=1.5)  # Eje X
        plt.axvline(0, color='darkgray', lw=1.5)  # Eje Y
        plt.grid()
        plt.legend()
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# INTERFAZ GRÁFICA

ventana = Tk()
ventana.title("Calculadora de Función Cuadrática")
ventana.configure(bg="#3B8B9E")

# Etiquetas y campos de entrada
Label(ventana, text="Ingrese el valor de a:", font=("Arial", 18), bg="#3B8B9E").grid(row=0, column=0, padx=20, pady=20, sticky=E)
entry_a = Entry(ventana, font=("Arial", 18))
entry_a.grid(row=0, column=1, padx=20, pady=20)

Label(ventana, text="Ingrese el valor de b:", font=("Arial", 18), bg="#3B8B9E").grid(row=1, column=0, padx=20, pady=20, sticky=E)
entry_b = Entry(ventana, font=("Arial", 18))
entry_b.grid(row=1, column=1, padx=20, pady=20)

Label(ventana, text="Ingrese el valor de c:", font=("Arial", 18), bg="#3B8B9E").grid(row=2, column=0, padx=20, pady=20, sticky=E)
entry_c = Entry(ventana, font=("Arial", 18))
entry_c.grid(row=2, column=1, padx=20, pady=20)

Label(ventana, text="Límite izquierdo:", font=("Arial", 18), bg="#3B8B9E").grid(row=3, column=0, padx=20, pady=20, sticky=E)
entry_x1 = Entry(ventana, font=("Arial", 18))
entry_x1.grid(row=3, column=1, padx=20, pady=20)

Label(ventana, text="Límite derecho:", font=("Arial", 18), bg="#3B8B9E").grid(row=4, column=0, padx=20, pady=20, sticky=E)
entry_x2 = Entry(ventana, font=("Arial", 18))
entry_x2.grid(row=4, column=1, padx=20, pady=20)

Label(ventana, text="Cantidad de rectángulos:", font=("Arial", 18), bg="#3B8B9E").grid(row=5, column=0, padx=20, pady=20, sticky=E)
entry_rectangulos = Entry(ventana, font=("Arial", 18))
entry_rectangulos.grid(row=5, column=1, padx=20, pady=20)

# Botón para graficar la función
Button(ventana, text="Graficar Función", font=("Arial", 18), command=graficar, bg="#66B2C4").grid(row=6, columnspan=2, pady=40)

ventana.mainloop()
