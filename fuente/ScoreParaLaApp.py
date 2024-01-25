from tkinter import *

class ScoreApp:
    def __init__(self, root, puntuacion_final):
        self.root = root
        self.root.title("Pantalla de Score")

        self.label_puntuacion_final = Label(root, text=f"Puntuación Final: {puntuacion_final}", font=("Arial", 18))
        self.label_puntuacion_final.pack(pady=20)

class MiApp:
    def __init__(self, root):
        self.root = root
        # (reemplazar la lógica con la real)
        self.puntuacion_final = 0

        self.mostrar_pantalla_score()

    def mostrar_pantalla_score(self):
        root_score = Toplevel(self.root)
        root_score.title("Pantalla de Score")
        root_score.geometry("400x300")

        app_score = ScoreApp(root_score, self.puntuacion_final)

root = Tk()
app = MiApp(root)
root.withdraw()
root.mainloop()
