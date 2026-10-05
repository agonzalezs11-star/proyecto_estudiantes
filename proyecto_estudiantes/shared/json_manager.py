import json
import os


RUTA_ARCHIVO = "data/estudiantes.json"


def asegurar_archivo():

    carpeta = os.path.dirname(
        RUTA_ARCHIVO
    )

    if not os.path.exists(carpeta):

        os.makedirs(carpeta)

    if not os.path.exists(
        RUTA_ARCHIVO
    ):

        with open(
            RUTA_ARCHIVO,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                [],
                archivo,
                indent=4,
                ensure_ascii=False
            )


def cargar():

    asegurar_archivo()

    try:

        with open(
            RUTA_ARCHIVO,
            "r",
            encoding="utf-8"
        ) as archivo:

            return json.load(
                archivo
            )

    except json.JSONDecodeError:

        return []


def guardar(datos):

    asegurar_archivo()

    with open(
        RUTA_ARCHIVO,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )