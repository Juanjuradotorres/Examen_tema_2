# get_record.py

import requests


class GetRecord:
    def __init__(self, url):
        self.url = url

    def get_all_records(self):
        try:
            respuesta = requests.get(self.url)
            respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa
            datos = respuesta.json()

            return datos if datos and isinstance(datos, list) else "No se encontraron registros."
        except requests.exceptions.RequestException as e:
            return f"Error al obtener datos: {e}"
