import json
import os


class GestorJSON:
    """Lee y guarda una lista de estudiantes en formato JSON."""

    def __init__(self, ruta):
        self.__ruta = ruta  # Ruta privada del archivo estudiantes.json

        carpeta = os.path.dirname(ruta)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

    @property
    def ruta(self):
        """Devuelve la ruta del archivo (solo lectura)."""
        return self.__ruta

    def leer(self):
        """Lee la lista de estudiantes del archivo JSON."""
        if not os.path.exists(self.__ruta):
            return []

        try:
            with open(self.__ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            return datos if isinstance(datos, list) else []

        except (json.JSONDecodeError, OSError):
            return []

    def guardar(self, datos):
        """Guarda la lista de estudiantes en el archivo JSON."""
        try:
            with open(self.__ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)

            return True

        except (TypeError, OSError):
            return False