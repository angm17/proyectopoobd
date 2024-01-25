from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

# Crea la ventana
ventana = Tk()
ventana.title("Ventana de puntajes")
ventana.geometry("{0}x{1}+0+0".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight()))

# Carga la imagen de fondo
ruta_imagen = "C:/Users/Family/Downloads/image 3.png"
imagen_fondo = Image.open(ruta_imagen)
imagen_fondo = imagen_fondo.resize((ventana.winfo_screenwidth(), ventana.winfo_screenheight()), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen_fondo)
# Definir la fuente personalizada
fuente = font.Font(family="MS Sans Serif", size=34, weight="bold")
fuente_boton = font.Font(family="Fixedsys", size=28, weight="bold")

# Crear el marco (frame) para el recuadro
marco = Frame(ventana, bg="#CDFFF6", width=700, height=450)
marco.pack(pady=20)

# Crear el título del recuadro
titulo = Label(text="Felicidades!!!", font=fuente, bg="#CDFFF6", fg="yellow")
titulo.place(relx=0.5, rely=0.1, anchor="center")

# Crear el texto del recuadro
texto = Label(text="Tu puntaje es: 1000\nTiempo restante: 5 segundos\nCartas acertadas: 10\nIntentos fallidos: 1", font=("Ebrima", 28), bg="#CDFFF6", fg="blue")
texto.place(relx=0.5, rely=0.4, anchor="center")

# Crear el botón "Continuar"
boton = Button(text="Continuar", font=fuente_boton, bg="#006400", fg="#FFFFFF", command=lambda: print("Botón presionado"))
boton.place(relx=0.5, rely=0.8, anchor="center")

# Función para abrir la otra ventana
def otra_ventana():
    # Crea la otra ventana aquí
    pass

# Inicia el ciclo de la ventana
ventana.mainloop()




