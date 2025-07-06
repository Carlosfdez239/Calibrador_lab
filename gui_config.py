import tkinter as tk
from tkinter import ttk
import json

def crear_menu_superior(root, modo_logger_callback):
    menu_bar = tk.Menu(root)
    sistema_menu = tk.Menu(menu_bar, tearoff=0)
    modo_var = tk.StringVar(value="Producción")

    def cambiar_modo(modo):
        modo_var.set(modo)
        modo_logger_callback(modo.lower())

    sistema_menu.add_radiobutton(label="Producción", variable=modo_var,
                                  command=lambda: cambiar_modo("Producción"))
    sistema_menu.add_radiobutton(label="Debug", variable=modo_var,
                                  command=lambda: cambiar_modo("Debug"))
    menu_bar.add_cascade(label="Sistema", menu=sistema_menu)
    root.config(menu=menu_bar)

class NoriaGUI:
    def __init__(self, root):
        self.root = root
        self.paradas = []

        tk.Label(root, text="Número de paradas:").pack()
        self.num_entry = tk.Entry(root)
        self.num_entry.pack()

        self.generate_btn = tk.Button(root, text="Generar tabla", command=self.generar_formulario)
        self.generate_btn.pack()

        self.canvas = tk.Canvas(root, width=300, height=300, bg="lightgray")
        self.canvas.pack(pady=10)

    def generar_formulario(self):
        num = int(self.num_entry.get())
        self.campos = []
        self.canvas.delete("all")
        for i in range(num):
            frame = tk.Frame(self.root)
            tk.Label(frame, text=f"Parada {i+1} (°):").pack(side="left")
            angle_entry = tk.Entry(frame, width=6)
            angle_entry.pack(side="left")

            sentido = ttk.Combobox(frame, values=["↻ horario", "↺ antihorario"], width=12)
            sentido.set("↻ horario")
            sentido.pack(side="left")

            self.campos.append((angle_entry, sentido))
            frame.pack()

        tk.Button(self.root, text="Guardar configuración", command=self.guardar_datos).pack()

    def guardar_datos(self):
        self.paradas = []
        for entry, sentido in self.campos:
            grado = round(float(entry.get()), 2)
            direccion = sentido.get()
            self.paradas.append({"angulo": grado, "sentido": direccion})

        with open("paradas.json", "w") as f:
            json.dump(self.paradas, f, indent=4)

        self.dibujar_noria(self.paradas)

    def dibujar_noria(self, paradas):
        cx, cy, r = 150, 150, 100
        self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, outline="black")

        for i, parada in enumerate(paradas):
            ang = parada["angulo"]
            sentido = parada["sentido"]
            rad = ang * 3.1416 / 180
            x = cx + r * 0.9 * -tk.sin(rad)
            y = cy + r * 0.9 * -tk.cos(rad)
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")
            self.canvas.create_text(x, y-10, text=f"{ang:.2f}°")
            flecha = "→" if sentido == "↻ horario" else "←"
            self.canvas.create_text(x, y+10, text=flecha)