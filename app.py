import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("HydraFlow - Control de Nivel y Flujo")
root.geometry("900x600")
root.minsize(800, 500)

root.configure(bg="#ffffff")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_archivo = tk.Menu(menu_bar, tearoff=0)
menu_archivo.add_command(label="Salir", command=root.quit)
menu_bar.add_cascade(label="Archivo", menu=menu_archivo)

menu_control = tk.Menu(menu_bar, tearoff=0)
menu_control.add_command(label="Iniciar sistema")
menu_control.add_command(label="Detener sistema")
menu_bar.add_cascade(label="Control", menu=menu_control)

menu_config = tk.Menu(menu_bar, tearoff=0)
menu_config.add_command(label="Parámetros PID")
menu_bar.add_cascade(label="Configuración", menu=menu_config)

root.mainloop()
