from models import Estudiante
from shared.json_manager import cargar, guardar


class EstudianteController:

    MODELO = Estudiante

    # ==========================================
    # OBTENER ESTUDIANTES
    # ==========================================

    @staticmethod
    def obtener_estudiantes():

        datos = cargar()

        return [
            Estudiante.desde_diccionario(estudiante)
            for estudiante in datos
        ]

    # ==========================================
    # CREAR ESTUDIANTE
    # ==========================================

    @staticmethod
    def crear(datos):

        estudiantes = (
            EstudianteController.obtener_estudiantes()
        )

        try:

            id_estudiante = int(
                datos["id"]
            )

        except (ValueError, KeyError):

            return False, "El ID debe ser un número."

        for estudiante in estudiantes:

            if estudiante.id == id_estudiante:

                return (
                    False,
                    "Ya existe un estudiante con ese ID."
                )

        carnet = datos["carnet"].strip().upper()

        for estudiante in estudiantes:

            if estudiante.carnet == carnet:

                return (
                    False,
                    "Ya existe un estudiante con ese carnet."
                )

        try:

            estudiante = Estudiante(
                id_estudiante,
                datos["nombre"],
                datos["apellido"],
                datos["email"],
                datos["carnet"]
            )

        except ValueError as error:

            return False, str(error)

        estudiantes.append(estudiante)

        guardar([
            estudiante.a_diccionario()
            for estudiante in estudiantes
        ])

        return (
            True,
            "Estudiante creado correctamente."
        )

    # ==========================================
    # LISTAR ESTUDIANTES
    # ==========================================

    @staticmethod
    def listar():

        return EstudianteController.obtener_estudiantes()

    # ==========================================
    # BUSCAR ESTUDIANTE
    # ==========================================

    @staticmethod
    def buscar(termino):

        estudiantes = (
            EstudianteController.obtener_estudiantes()
        )

        termino = str(
            termino
        ).lower().strip()

        encontrados = []

        for estudiante in estudiantes:

            texto = (
                f"{estudiante.id} "
                f"{estudiante.nombre} "
                f"{estudiante.apellido} "
                f"{estudiante.email} "
                f"{estudiante.carnet}"
            ).lower()

            if termino in texto:

                encontrados.append(estudiante)

        return encontrados

    # ==========================================
    # AGREGAR NOTA
    # ==========================================

    @staticmethod
    def agregar_nota(
        id_estudiante,
        materia,
        nota
    ):

        estudiantes = (
            EstudianteController.obtener_estudiantes()
        )

        estudiante_encontrado = None

        for estudiante in estudiantes:

            if estudiante.id == id_estudiante:

                estudiante_encontrado = estudiante

                break

        if estudiante_encontrado is None:

            return (
                False,
                "No existe un estudiante con ese ID."
            )

        try:

            estudiante_encontrado.agregar_nota(
                materia,
                nota
            )

        except ValueError as error:

            return False, str(error)

        guardar([
            estudiante.a_diccionario()
            for estudiante in estudiantes
        ])

        return (
            True,
            "Nota agregada correctamente."
        )

    # ==========================================
    # ACTUALIZAR ESTUDIANTE
    # ==========================================

    @staticmethod
    def actualizar(
        id_estudiante,
        datos
    ):

        estudiantes = (
            EstudianteController.obtener_estudiantes()
        )

        estudiante_encontrado = None

        for estudiante in estudiantes:

            if estudiante.id == id_estudiante:

                estudiante_encontrado = estudiante

                break

        if estudiante_encontrado is None:

            return (
                False,
                "No existe un estudiante con ese ID."
            )

        try:

            estudiante_encontrado.nombre = (
                datos["nombre"]
            )

            estudiante_encontrado.apellido = (
                datos["apellido"]
            )

            estudiante_encontrado.email = (
                datos["email"]
            )

            estudiante_encontrado.carnet = (
                datos["carnet"]
            )

        except (ValueError, KeyError) as error:

            return False, str(error)

        guardar([
            estudiante.a_diccionario()
            for estudiante in estudiantes
        ])

        return (
            True,
            "Estudiante actualizado correctamente."
        )

    # ==========================================
    # ELIMINAR ESTUDIANTE
    # ==========================================

    @staticmethod
    def eliminar(id_estudiante):

        estudiantes = (
            EstudianteController.obtener_estudiantes()
        )

        nuevos_estudiantes = [
            estudiante
            for estudiante in estudiantes
            if estudiante.id != id_estudiante
        ]

        if len(nuevos_estudiantes) == len(estudiantes):

            return (
                False,
                "No existe un estudiante con ese ID."
            )

        guardar([
            estudiante.a_diccionario()
            for estudiante in nuevos_estudiantes
        ])

        return (
            True,
            "Estudiante eliminado correctamente."
        )