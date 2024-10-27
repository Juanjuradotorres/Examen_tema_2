# main.py

import tkinter as tk
from GetRecord import GetRecord
from ShowRecord import ShowRecord

if __name__ == "__main__":
    url = "https://671be4232c842d92c381a595.mockapi.io/test"

    get_record = GetRecord(url)
    ventana = tk.Tk()
    ventana.attributes("-fullscreen", True)  # Activar pantalla completa
    ventana.resizable(False, False)  # Desactivar la capacidad de redimensionar

    show_record = ShowRecord(ventana, get_record)

    ventana.mainloop()
