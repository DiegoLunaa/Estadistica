import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Función para crear la ventana de resultados
def mostrar_resultados(resultados, fig):
    # Crear la ventana
    ventana_resultados = tk.Toplevel()
    ventana_resultados.title("Resultados y Gráfico")
    ventana_resultados.geometry("1366x768")

    # Frame para los resultados del área
    frame_resultados = tk.Frame(ventana_resultados, width=500, height=768, bg="#274357")
    frame_resultados.place(x=0, y=0)

    # Frame para el gráfico
    frame_grafico = tk.Frame(ventana_resultados, width=866, height=768,bg="#274357")
    frame_grafico.place(x=500, y=0)

    # Mostrar los resultados en el primer frame
    label_resultados = tk.Label(frame_resultados, text=resultados, font=("Arial", 18), bg="#274357", fg="white")
    label_resultados.place(relx=0.5, rely=0.5, anchor='center')

    # Mostrar el gráfico en el segundo frame
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor='center')

    boton_salir = tk.Button(frame_resultados, text="Salir", width=22, fg="White", font=("Arial", 14), bg="#274357", command=ventana_resultados.destroy)
    boton_salir.place(relx=0.5, y=700, anchor='center')
    ventana_resultados.mainloop()
    
    ventana_resultados.mainloop()

