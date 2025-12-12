import tkinter as tk
from tkinter import ttk

# ===============================
# Ventana principal
# ===============================
root = tk.Tk()
root.title("HydraFlow - Control de Nivel y Flujo")
root.geometry("900x600")
root.minsize(800, 500)

# ===============================
# Estilos ttk
# ===============================
style = ttk.Style()
style.theme_use("default")

style.configure(
    "Title.TLabel",
    font=("Segoe UI", 20, "bold")
)

style.configure(
    "Panel.TFrame",
    padding=15
)

style.configure(
    "Status.TLabel",
    font=("Segoe UI", 10),
    foreground="gray"
)

# ===============================
# Contenedor principal
# ===============================
container = ttk.Frame(root)
container.pack(fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# ===============================
# Diccionario de pantallas
# ===============================
frames = {}

def show_frame(name):
    frame = frames[name]
    frame.tkraise()
    status_label.config(text=f"Vista actual: {name}")

# ===============================
# Pantalla: Inicio
# ===============================
inicio = ttk.Frame(container)
inicio.grid(row=0, column=0, sticky="nsew")

panel_inicio = ttk.Frame(inicio, style="Panel.TFrame")
panel_inicio.pack(expand=True)

ttk.Label(
    panel_inicio,
    text="Pantalla de Inicio",
    style="Title.TLabel"
).pack(pady=(0, 10))

ttk.Label(
    panel_inicio,
    text="Monitoreo general de nivel y flujo",
    font=("Segoe UI", 12)
).pack()

frames["Inicio"] = inicio

# ===============================
# Pantalla: Control
# ===============================
control = ttk.Frame(container)
control.grid(row=0, column=0, sticky="nsew")

panel_control = ttk.Frame(control, style="Panel.TFrame")
panel_control.pack(expand=True)

ttk.Label(
    panel_control,
    text="Pantalla de Control",
    style="Title.TLabel"
).pack(pady=(0, 10))

ttk.Label(
    panel_control,
    text="Operación e interrupción del sistema",
    font=("Segoe UI", 12)
).pack()

frames["Control"] = control

# ===============================
# Pantalla: Diagnóstico
# ===============================
diagnostico = ttk.Frame(container)
diagnostico.grid(row=0, column=0, sticky="nsew")

panel_diag = ttk.Frame(diagnostico, style="Panel.TFrame")
panel_diag.pack(expand=True)

ttk.Label(
    panel_diag,
    text="Monitoreo y Diagnóstico",
    style="Title.TLabel"
).pack(pady=(0, 10))

ttk.Label(
    panel_diag,
    text="Estado de conexión, errores y alarmas",
    font=("Segoe UI", 12)
).pack()

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

# ===============================
# Barra de estado inferior
# ===============================


# ===============================
# Mostrar pantalla inicial
# ===============================
show_frame("Inicio")

root.mainloop()
