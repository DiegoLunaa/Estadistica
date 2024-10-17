import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def negativo(variable):
    if variable < 0:
        return f"({variable})"
    return variable 

def funcion_cuadratica(a, b, c, x):
    return a * x**2 + b * x + c

def evaluar_funcion_cuadratica(x):
    return funcion_cuadratica(a, b, c, x)


# Entradas del usuario
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
print(f"La función cuadrática es: {negativo(a)}x² + {negativo(b)}x + {negativo(c)}")

# Graficar la función cuadrática
x_values = np.linspace(-1, 6, 400)  # Rango de valores de x
y_values = funcion_cuadratica(a, b, c, x_values)

plt.plot(x_values, y_values, label=f'f(x) = {negativo(a)}x² + {negativo(b)}x + {negativo(c)}', color='blue')

# Área con rectángulos
x1 = float(input("Ingrese el límite izquierdo: "))
x2 = float(input("Ingrese el límite derecho: "))
cant_rectangulos = int(input("Ingrese la cantidad de rectángulos: "))
intervalo_rectangulo = (x2 - x1) / cant_rectangulos

intervalo_inicial = x1
area_inferior = 0
area_superior = 0

for i in range(1, cant_rectangulos + 1):
    intervalo_final = intervalo_inicial + intervalo_rectangulo

    # Valores para el área
    y_inferior = funcion_cuadratica(a, b, c, intervalo_inicial)
    y_superior = funcion_cuadratica(a, b, c, intervalo_final)

    # Rellenar el área inferior en amarillo
    plt.fill_between([intervalo_inicial, intervalo_final], 0, y_inferior, color='red', alpha=1)

    # Rellenar el área superior en rojo
    plt.fill_between([intervalo_inicial, intervalo_final], y_superior, 0, color='blue', alpha=0.7)

    print("El rectángulo número", i, "empieza en", intervalo_inicial, "y finaliza en", intervalo_final)
    
    # Cálculo de áreas
    area_inferior += (intervalo_final - intervalo_inicial) * y_inferior
    area_superior += (intervalo_final - intervalo_inicial) * y_superior
    intervalo_inicial = intervalo_final


area_real, error_integral = quad(evaluar_funcion_cuadratica, x1, x2)

# Calcular los errores
error_inferior = area_real - area_inferior
error_superior = area_real - area_superior

print("El área de la región de dicha función se encuentra entre:", area_inferior, "y", area_superior)
print(f"El área real bajo la curva en el intervalo [{x1}, {x2}] es: {area_real}")
print(f"El error de cálculo con el área inferior es: {error_inferior}")
print(f"El error de cálculo con el área superior es: {error_superior}")

# Configuraciones finales del gráfico
plt.title('Gráfico de la Función Cuadrática')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Ejes con líneas más oscuras
plt.axhline(0, color='darkgray', lw=1.5)  # Eje X más oscuro
plt.axvline(0, color='darkgray', lw=1.5)  # Eje Y más oscuro

plt.grid()
plt.legend()
plt.show()



