import tkinter as tk
from PIL import Image, ImageTk
import pygame
import pickle
import os

class Reproductor:
    SAVE_FILE = "checkpoint_player.pkl"

    def __init__(self):
        pygame.mixer.init()

        # Ventana principal
        self.root = tk.Tk()
        self.root.title("Reproductor estilo Spotify")
        self.root.geometry("400x400")
        self.root.configure(bg="black")

        # Variables de estado
        self.cancion_actual = "musica.mp3"
        self.posicion = 0
        self.reproduciendo = False
        self.pausado = False

        # Etiqueta principal (título)
        self.label = tk.Label(
            self.root, 
            text="Reproductor de Música", 
            font=("Arial", 16, "bold"), 
            fg="white", 
            bg="#1DB954", 
            padx=10, pady=5
        )
        self.label.pack(pady=10, fill="x")

        # Imagen de la portada
        if os.path.exists("portada.jpg"):
            self.portada = Image.open("portada.jpg")
            self.portada = self.portada.resize((150, 150))
            self.portada_tk = ImageTk.PhotoImage(self.portada)
            self.label_portada = tk.Label(self.root, image=self.portada_tk, bg="black")
            self.label_portada.pack(pady=10)
        else:
            self.label_portada = tk.Label(self.root, text="Sin portada", fg="white", bg="black", font=("Arial", 12))
            self.label_portada.pack(pady=10)

        # Etiqueta de tiempo
        self.tiempo_label = tk.Label(
            self.root, 
            text="Tiempo: 00:00", 
            font=("Arial", 12, "bold"), 
            fg="white", 
            bg="black", 
            padx=10, pady=5
        )
        self.tiempo_label.pack(pady=5, fill="x")

        # Botones estilo Spotify
        tk.Button(
            self.root, text="Play", width=12, command=self.play, 
            fg="white", bg="#1DB954", activebackground="#1ED760", 
            font=("Arial", 10, "bold")
        ).pack(pady=5)

        tk.Button(
            self.root, text="Pause", width=12, command=self.pause, 
            fg="white", bg="#1DB954", activebackground="#1ED760", 
            font=("Arial", 10, "bold")
        ).pack(pady=5)

        tk.Button(
            self.root, text="Stop", width=12, command=self.stop, 
            fg="white", bg="#1DB954", activebackground="#1ED760", 
            font=("Arial", 10, "bold")
        ).pack(pady=5)

        # Cargar checkpoint
        self.cargar_checkpoint()

        # Actualizar tiempo cada segundo
        self.actualizar_tiempo()

        # Evento al cerrar ventana
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar)

        self.root.mainloop()

    # Reproducir o reanudar
    def play(self):
        if not os.path.exists(self.cancion_actual):
            print("No se encontró musica.mp3")
            return

        if not self.reproduciendo:
            pygame.mixer.music.load(self.cancion_actual)
            pygame.mixer.music.play(start=self.posicion)
            self.reproduciendo = True
            self.pausado = False
        elif self.pausado:
            pygame.mixer.music.unpause()
            self.pausado = False

    # Pausar
    def pause(self):
        if self.reproduciendo and not self.pausado:
            pygame.mixer.music.pause()
            self.pausado = True

    # Detener
    def stop(self):
        pygame.mixer.music.stop()
        self.posicion = 0
        self.reproduciendo = False
        self.pausado = False
        self.tiempo_label.config(text="Tiempo: 00:00")

    # Actualizar contador de tiempo en pantalla
    def actualizar_tiempo(self):
        # Mostrar primero
        minutos = int(self.posicion // 60)
        segundos = int(self.posicion % 60)
        self.tiempo_label.config(text=f"Tiempo: {minutos:02}:{segundos:02}")

        # Sumar 1 segundo si está reproduciendo y no pausado
        if self.reproduciendo and not self.pausado:
            self.posicion += 1

        self.root.after(1000, self.actualizar_tiempo)

    # Guardar checkpoint
    def guardar_checkpoint(self):
        estado = {
            "cancion": self.cancion_actual,
            "posicion": self.posicion
        }
        with open(self.SAVE_FILE, "wb") as f:
            pickle.dump(estado, f)

    # Cargar checkpoint
    def cargar_checkpoint(self):
        if os.path.exists(self.SAVE_FILE):
            with open(self.SAVE_FILE, "rb") as f:
                estado = pickle.load(f)
                self.cancion_actual = estado["cancion"]
                self.posicion = estado["posicion"]

                minutos = int(self.posicion // 60)
                segundos = int(self.posicion % 60)
                self.tiempo_label.config(text=f"Tiempo: {minutos:02}:{segundos:02}")

    # Cerrar ventana
    def cerrar(self):
        self.guardar_checkpoint()
        self.root.destroy()


if __name__ == "__main__":
    Reproductor()
