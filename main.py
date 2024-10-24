import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from calculo_de_area import abrir_area
<<<<<<< Updated upstream
from v3 import abrir_ecuaciones
=======
from sistemas_ecuaciones import abrir_ecuaciones
>>>>>>> Stashed changes
import sys

ventana = tk.Tk()
ventana.title("PROGRAMA DE ESTADÍSTICA Y PROBABILIDAD")
ventana.geometry(f"800x600")
ventana.configure(bg="#1F6680")

# Logo Isaui
imagen = Image.open("C:/Users/benja/OneDrive/Desktop/Estadistica/isaui.png")
imagen_redimensionada = imagen.resize((500, 350))  # Tamaño ajustado
imagen_logo = ImageTk.PhotoImage(imagen_redimensionada)
label_imagen = tk.Label(ventana, image=imagen_logo, bg="#1F6680")
label_imagen.place(relx=0.5, y=100,anchor='center')  # Ajuste de posición

#Labels
label_estadistica = tk.Label(ventana, text="ESTADÍSTICA Y PROBABILIDAD\nAPLICADA", font=("Arial", 24), bg="#1F6680", fg="white")
label_estadistica.place(relx=0.5, y=220, anchor='center')

label_pregunta = tk.Label(ventana, text="¿Qué operación desea realizar?" , font=("Arial", 24), bg="#1F6680", fg="white")
label_pregunta.place(relx=0.5, y=300, anchor='center')

#BOTONES
boton_area = tk.Button(ventana, text="CÁLCULO DE ÁREA", width=22, fg="White", font=("Arial", 14), bg="#274357",command=abrir_area)
boton_area.place(relx=0.5, y=370, anchor='center') 

boton_ecuacion = tk.Button(ventana, text="ECUACIONES LINEALES", width=22, fg="White", font=("Arial", 14), bg="#274357", command=abrir_ecuaciones)
boton_ecuacion.place(relx=0.5, y=440, anchor='center') 

boton_salir = tk.Button(ventana, text="SALIR", width=22, fg="White", font=("Arial", 14), bg="#274357", command=sys.exit)
boton_salir.place(relx=0.5, y=510, anchor='center') 


ventana.mainloop()
