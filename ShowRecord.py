# show_record.py

import tkinter as tk
from tkinter import ttk

class ShowRecord:
    def __init__(self, root, get_record_instance):
        if get_record_instance is None:
            raise ValueError("La instancia de GetRecord no debe ser None")

        self.get_record_instance = get_record_instance

        # Configuración de la ventana
        self.root = root
        self.root.title("Registros de Países")
        self.root.geometry("600x400")

        # Crear un marco para la búsqueda
        self.frame_busqueda = tk.Frame(self.root)
        self.frame_busqueda.pack(side=tk.TOP, anchor='ne', padx=10, pady=10)

        # Campo de entrada para GPS
        self.label_gps = tk.Label(self.frame_busqueda, text="Buscar por GPS:")
        self.label_gps.pack(side=tk.LEFT)

        self.entry_gps = tk.Entry(self.frame_busqueda)
        self.entry_gps.pack(side=tk.LEFT)

        self.boton_buscar = tk.Button(self.frame_busqueda, text="Buscar", command=self.buscar_gps)
        self.boton_buscar.pack(side=tk.LEFT)

        # Crear un botón para obtener todos los registros
        self.boton = tk.Button(self.root, text="Mostrar Todos los Registros", command=self.mostrar_todos_registros)
        self.boton.pack(pady=10)

        # Configuración de la tabla
        self.tabla = ttk.Treeview(self.root, columns=("País", "Fecha y Tiempo", "Calle", "GPS"), show='headings')
        self.tabla.heading("País", text="País")
        self.tabla.heading("Fecha y Tiempo", text="Fecha y Tiempo")
        self.tabla.heading("Calle", text="Calle")
        self.tabla.heading("GPS", text="GPS")
        self.tabla.pack(expand=True, fill='both')

    def buscar_gps(self):
        gps_buscado = self.entry_gps.get()
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        resultado = self.get_record_instance.get_all_records()

        if isinstance(resultado, list):
            encontrado = False
            for registro in resultado:
                if registro.get('GPS') == gps_buscado:
                    pais = registro.get('Pais', 'N/A')
                    fecha_y_tiempo = registro.get('Fecha_y_Tiempo', 'N/A')
                    calle = registro.get('Calle', 'N/A')
                    gps = registro.get('GPS', 'N/A')
                    self.tabla.insert("", "end", values=(pais, fecha_y_tiempo, calle, gps))
                    encontrado = True
                    break  # Solo mostrar un registro si se encuentra

            if not encontrado:
                self.tabla.insert("", "end", values=("N/A", "N/A", "N/A", gps_buscado))  # Imprimir N/A si no se encuentra
        else:
            self.tabla.insert("", "end", values=(resultado, "", "", ""))

    def mostrar_todos_registros(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        resultado = self.get_record_instance.get_all_records()

        if isinstance(resultado, list):
            for registro in resultado:
                pais = registro.get('Pais', 'N/A')
                fecha_y_tiempo = registro.get('Fecha_y_Tiempo', 'N/A')
                calle = registro.get('Calle', 'N/A')
                gps = registro.get('GPS', 'N/A')

                self.tabla.insert("", "end", values=(pais, fecha_y_tiempo, calle, gps))
        else:
            self.tabla.insert("", "end", values=(resultado, "", "", ""))
