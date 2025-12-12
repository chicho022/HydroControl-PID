import tkinter as tk
from tkinter import ttk

# Ventana principal

root = tk.Tk()
root.title("HydraFlow - Control de Nivel y Flujo")
root.geometry("900x600")
root.minsize(800, 500)
container = ttk.Frame(root)
container.pack(fill="both", expand=True)

# Diccionario de pantallas

frames = {}
def show_frame(name):
    """Muestra la pantalla seleccionada"""
    frame = frames[name]
    frame.tkraise()

# Pantalla: Inicio
inicio = ttk.Frame(container)
inicio.grid(row=0, column=0, sticky="nsew")

lbl_inicio = ttk.Label(
    inicio,
    text="Pantalla de Inicio",
    font=("Segoe UI", 20),
)
lbl_inicio.pack(expand=True)

frames["Inicio"] = inicio

# ===============================
# Pantalla: Control
# ===============================
control = ttk.Frame(container)
control.grid(row=0, column=0, sticky="nsew")

lbl_control = ttk.Label(
    control,
    text="Pantalla de Control\nOperación del Sistema",
    font=("Segoe UI", 18)
)
lbl_control.pack(expand=True)

frames["Control"] = control

# ===============================
# Pantalla: Diagnóstico
# ===============================
diagnostico = ttk.Frame(container)
diagnostico.grid(row=0, column=0, sticky="nsew")

lbl_diag = ttk.Label(
    diagnostico,
    text="Monitoreo y Diagnóstico\nEstado del Sistema",
    font=("Segoe UI", 18)
)
lbl_diag.pack(expand=True)

frames["Diagnóstico"] = diagnostico

# ===============================
# Menú superior
# ===============================
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_vistas = tk.Menu(menu_bar, tearoff=0)
menu_vistas.add_command(label="Inicio", command=lambda: show_frame("Inicio"))
menu_vistas.add_command(label="Control", command=lambda: show_frame("Control"))
menu_vistas.add_command(label="Diagnóstico", command=lambda: show_frame("Diagnóstico"))
menu_bar.add_cascade(label="Vistas", menu=menu_vistas)

menu_bar.add_command(label="Salir", command=root.quit)

# Mostrar pantalla inicial

show_frame("Inicio")

root.mainloop()
