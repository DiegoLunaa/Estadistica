import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from tkinter import *
from tkinter import messagebox
from resultados import mostrar_resultados

# INTERFAZ GRÁFICA
def abrir_area():
    ventana = Toplevel()
    ventana.geometry("800x600")
    ventana.title("Calculadora de Función Cuadrática")
    ventana.configure(bg="#1F6680")

    label_titulo = Label(ventana, text="Cálculo de áreas de\nregiones curvas", font=("Arial", 24), bg="#1F6680", fg="white")
    label_titulo.place(relx=0.5, y=50, anchor='center')

    #frame con label funcion
    frame_funcion = Frame(ventana, bg="#274357")
    frame_funcion.place(x=0, y=90, width=800, height=48)
    label_funcion = Label(frame_funcion, text="Teniendo en cuenta la siguiente función: f(x)= ax² + bx + c .", font=("Arial", 18), bg="#274357", fg="white")
    label_funcion.place(relx=0.5,rely=0.5, anchor='center')

    # Etiquetas y campos de entrada
    label_a = Label(ventana, text="Ingrese el valor del término cuadrático (a):", font=("Arial", 18), fg="white", bg="#1F6680")
    label_a.place(x=5, y=163)
    entry_a = Entry(ventana, font=("Arial", 18))
    entry_a.place(x=536, y=163,width=200)

    label_b = Label(ventana, text="Ingrese el valor del término lineal (b):", font=("Arial", 18),fg="white", bg="#1F6680")
    label_b.place(x=5, y=227)
    entry_b = Entry(ventana, font=("Arial", 18))
    entry_b.place(x=536, y=227,width=200)

    label_c = Label(ventana, text="Ingrese el valor del término constante (c):", font=("Arial", 18),fg="white", bg="#1F6680")
    label_c.place(x=5, y=291)
    entry_c = Entry(ventana, font=("Arial", 18))
    entry_c.place(x=536, y=291,width=200)

    label_x1 = Label(ventana, text="Límite izquierdo:", font=("Arial", 18),fg="white", bg="#1F6680")
    label_x1.place(x=5, y=355)
    entry_x1 = Entry(ventana, font=("Arial", 18))
    entry_x1.place(x=536, y=355,width=200)

    label_x2 = Label(ventana, text="Límite derecho:", font=("Arial", 18),fg="white", bg="#1F6680")
    label_x2.place(x=5, y=419)
    entry_x2 = Entry(ventana, font=("Arial", 18))
    entry_x2.place(x=536, y=419,width=200)

    label_rectangulos = Label(ventana, text="Cantidad de rectángulos:", font=("Arial", 18),fg="white", bg="#1F6680")
    label_rectangulos.place(x=5, y=483)
    entry_rectangulos = Entry(ventana, font=("Arial", 18))
    entry_rectangulos.place(x=536, y=483,width=200)

    # NO INTERFAZ
    # Función para verificar si el número es negativo (para mostrarlo con paréntesis)
    def negativo(variable):
        if variable < 0:
            return f"({variable})"
        return variable 

    # Función cuadrática
    def funcion_cuadratica(a, b, c, x):
        return a * x**2 + b * x + c

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
            fig, ax = plt.subplots(figsize=(7, 6), dpi=100)
            x_values = np.linspace(x1 - 4, x2 + 4, 400)
            y_values = funcion_cuadratica(a, b, c, x_values)
            ax.plot(x_values, y_values, label=f'f(x) = {a}x² + {b}x + {c}', color='blue')
            

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
                plt.fill_between([intervalo_inicial, intervalo_final], y_inferior, y_superior, color='green', alpha=1)
                
                print(f"El rectángulo número {i} empieza en {intervalo_inicial:.4f} y finaliza en {intervalo_final:.4f} con área inferior: {y_inferior:.4f} y área superior: {y_superior:.4f}")

                # Cálculo de áreas
                area_inferior += (intervalo_final - intervalo_inicial) * y_inferior
                area_superior += (intervalo_final - intervalo_inicial) * y_superior
                intervalo_inicial = intervalo_final

            # Calcular el área real usando integración numérica
            area_real, _ = quad(lambda x: funcion_cuadratica(a, b, c, x), x1, x2)

            # Calcular los errores
            error_inferior = abs(area_real - area_inferior)
            error_superior = abs(area_real - area_superior)

            # Configurar gráficos
            plt.title('Gráfico de la Función Cuadrática')
            plt.xlabel('Eje x')
            plt.ylabel('Eje y', rotation=0, labelpad=20)
            plt.axhline(0, color='darkgray', lw=1.5)  # Eje X
            plt.axvline(0, color='darkgray', lw=1.5)  # Eje Y
            plt.grid()
            #plt.legend()
        
            resultados = f"Área real: {area_real}\nÁrea inferior: {area_inferior}\nÁrea superior: {area_superior}\nÁrea real: {area_real}\nError inferior: {error_inferior}\nError superior: {error_superior}\n"
            mostrar_resultados(resultados, fig)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")


    def limpiar_campos():
        entry_a.delete(0, END)  
        entry_b.delete(0, END)  
        entry_c.delete(0, END)  
        entry_x1.delete(0, END)  
        entry_x2.delete(0, END)  
        entry_rectangulos.delete(0, END)

    #INTERFAZ
    # Botones para graficar la función y limpiar los campos
    
    Boton_graficar = Button(ventana, text="Resolver", font=("Arial", 14), command=graficar, bg="White",width=10)
    Boton_graficar.place(x=528, y=538)
    boton_limpiar = Button(ventana, text="Limpiar", font=("Arial", 14), bg="White", command=limpiar_campos,width=10)
    boton_limpiar.place(x=388, y=538)
    boton_salir = Button(ventana, text="Salir", font=("Arial", 14), bg="White", command=ventana.destroy,width=10)
    boton_salir.place(x=669, y=538)

    ventana.mainloop()
