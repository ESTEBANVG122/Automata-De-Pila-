import tkinter as tk
from tkinter import filedialog, messagebox

def automata_pila(cadena):
    """Valida si una cadena tiene corchetes y llaves balanceados usando un autómata de pila."""
    pila = []
    pares = {'{': '}', '[': ']'}  # Solo se consideran corchetes y llaves
    for char in cadena:
        if char in pares.keys():  # Si es un carácter de apertura, se agrega a la pila
            pila.append(char)
        elif char in pares.values():  # Si es un carácter de cierre
            if not pila or pares[pila.pop()] != char:  # La pila no debe estar vacía y el último abierto debe coincidir
                return False
    return not pila  # Si la pila está vacía al final, está balanceado

def validar_cadenas():
    """Valida las cadenas ingresadas y muestra los resultados."""
    cadenas = entry.get().split(",")
    resultados = []
    for cadena in cadenas:
        cadena = cadena.strip()
        if automata_pila(cadena):
            resultados.append(f"[{cadena}]: Válida")
        else:
            resultados.append(f"[{cadena}]: Inválida")
    resultados_var.set("\n".join(resultados))

def cargar_archivo():
    """Permite cargar cadenas desde un archivo y mostrarlas en el campo de entrada."""
    filepath = filedialog.askopenfilename(
        filetypes=[("Archivos de texto", ".txt"), ("Todos los archivos", ".*")]
    )
    if filepath:
        try:
            with open(filepath, "r") as file:
                contenido = file.read()
                entry.delete(0, tk.END)
                entry.insert(0, contenido)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

def limpiar_resultados():
    """Limpia los resultados y el campo de entrada."""
    entry.delete(0, tk.END)
    resultados_var.set("")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Autómata de Pila - Corchetes y Llaves Balanceados")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg="#f7f7f7")

# Etiqueta de entrada
tk.Label(root, text="Ingrese cadenas separadas por comas:", font=("Arial", 12), bg="#f7f7f7").pack(pady=10)

# Campo de entrada
entry = tk.Entry(root, font=("Arial", 12), width=50)
entry.pack(pady=5)

# Botones
frame_botones = tk.Frame(root, bg="#f7f7f7")
frame_botones.pack(pady=10)

btn_validar = tk.Button(frame_botones, text="Validar Cadenas", command=validar_cadenas, bg="#4caf50", fg="white", font=("Arial", 10), width=15)
btn_validar.grid(row=0, column=0, padx=5)

btn_cargar = tk.Button(frame_botones, text="Cargar Archivo", command=cargar_archivo, bg="#2196f3", fg="white", font=("Arial", 10), width=15)
btn_cargar.grid(row=0, column=1, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_resultados, bg="#f44336", fg="white", font=("Arial", 10), width=15)
btn_limpiar.grid(row=0, column=2, padx=5)

# Resultados
resultados_var = tk.StringVar()
resultados_label = tk.Label(root, textvariable=resultados_var, font=("Courier", 10), bg="#f7f7f7", justify="left", anchor="nw")
resultados_label.pack(pady=10, fill="both", expand=True)

# Iniciar el bucle de la interfaz
root.mainloop()
