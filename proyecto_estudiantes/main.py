from views import EstudianteController

from shared.herramientas import (
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info,
    confirmar,
    pausa
)


def menu():

    while True:

        imprimir_titulo(
            "SISTEMA DE ESTUDIANTES"
        )

        print("1. Crear estudiante")
        print("2. Ver estudiantes")
        print("3. Buscar")
        print("4. Agregar nota")
        print("5. Actualizar estudiante")
        print("6. Eliminar")
        print("0. Salir")

        opcion = input(
            "\nOpción: "
        )

        # ==================================
        # CREAR
        # ==================================

        if opcion == "1":

            imprimir_titulo(
                "CREAR ESTUDIANTE"
            )

            datos = {}

            datos["id"] = input(
                "ID: "
            )

            datos["nombre"] = input(
                "Nombre: "
            )

            datos["apellido"] = input(
                "Apellido: "
            )

            datos["email"] = input(
                "Email: "
            )

            datos["carnet"] = input(
                "Carnet: "
            )

            exito, mensaje = (
                EstudianteController.crear(
                    datos
                )
            )

            if exito:

                imprimir_exito(
                    mensaje
                )

            else:

                imprimir_error(
                    mensaje
                )

            pausa()

        # ==================================
        # LISTAR
        # ==================================

        elif opcion == "2":

            imprimir_titulo(
                "LISTA DE ESTUDIANTES"
            )

            estudiantes = (
                EstudianteController.listar()
            )

            if not estudiantes:

                imprimir_info(
                    "No hay estudiantes registrados."
                )

            else:

                for estudiante in estudiantes:

                    print(
                        estudiante
                    )

                    print(
                        f"    Email: "
                        f"{estudiante.email}"
                    )

                    materias = (
                        estudiante.materias
                    )

                    if materias:

                        print(
                            "    Materias: "
                            + ", ".join(
                                sorted(materias)
                            )
                        )

                    else:

                        print(
                            "    Materias: Ninguna"
                        )

                    print(
                        f"    Promedio: "
                        f"{estudiante.promedio}"
                    )

                    print(
                        "-" * 60
                    )

            pausa()

        # ==================================
        # BUSCAR
        # ==================================

        elif opcion == "3":

            imprimir_titulo(
                "BUSCAR ESTUDIANTE"
            )

            termino = input(
                "Buscar: "
            )

            encontrados = (
                EstudianteController.buscar(
                    termino
                )
            )

            if not encontrados:

                imprimir_info(
                    "No se encontraron coincidencias."
                )

            else:

                for estudiante in encontrados:

                    print(
                        estudiante
                    )

            pausa()

        # ==================================
        # AGREGAR NOTA
        # ==================================

        elif opcion == "4":

            imprimir_titulo(
                "AGREGAR NOTA"
            )

            try:

                id_estudiante = int(
                    input(
                        "ID del estudiante: "
                    )
                )

                materia = input(
                    "Materia: "
                )

                nota = float(
                    input(
                        "Nota: "
                    )
                )

                exito, mensaje = (
                    EstudianteController.agregar_nota(
                        id_estudiante,
                        materia,
                        nota
                    )
                )

                if exito:

                    imprimir_exito(
                        mensaje
                    )

                else:

                    imprimir_error(
                        mensaje
                    )

            except ValueError:

                imprimir_error(
                    "El ID y la nota deben ser números."
                )

            pausa()

        # ==================================
        # ACTUALIZAR
        # ==================================

        elif opcion == "5":

            imprimir_titulo(
                "ACTUALIZAR ESTUDIANTE"
            )

            try:

                id_estudiante = int(
                    input(
                        "ID del estudiante: "
                    )
                )

                datos = {}

                datos["nombre"] = input(
                    "Nuevo nombre: "
                )

                datos["apellido"] = input(
                    "Nuevo apellido: "
                )

                datos["email"] = input(
                    "Nuevo email: "
                )

                datos["carnet"] = input(
                    "Nuevo carnet: "
                )

                exito, mensaje = (
                    EstudianteController.actualizar(
                        id_estudiante,
                        datos
                    )
                )

                if exito:

                    imprimir_exito(
                        mensaje
                    )

                else:

                    imprimir_error(
                        mensaje
                    )

            except ValueError:

                imprimir_error(
                    "El ID debe ser un número."
                )

            pausa()

        # ==================================
        # ELIMINAR
        # ==================================

        elif opcion == "6":

            imprimir_titulo(
                "ELIMINAR ESTUDIANTE"
            )

            try:

                id_estudiante = int(
                    input(
                        "ID del estudiante: "
                    )
                )

                estudiante = None

                estudiantes = (
                    EstudianteController.listar()
                )

                for item in estudiantes:

                    if item.id == id_estudiante:

                        estudiante = item
                        break

                if estudiante is None:

                    imprimir_error(
                        "No existe un estudiante con ese ID."
                    )

                else:

                    if confirmar(
                        "¿Está seguro de eliminar "
                        f"a {estudiante.nombre_completo}?"
                    ):

                        exito, mensaje = (
                            EstudianteController.eliminar(
                                id_estudiante
                            )
                        )

                        if exito:

                            imprimir_exito(
                                mensaje
                            )

                        else:

                            imprimir_error(
                                mensaje
                            )

                    else:

                        imprimir_info(
                            "Operación cancelada."
                        )

            except ValueError:

                imprimir_error(
                    "El ID debe ser un número."
                )

            pausa()
        elif opcion == "0":

            imprimir_info(
                "Hasta luego."
            )

            break

        else:

            imprimir_error(
                "Opción inválida."
            )

            pausa()


if __name__ == "__main__":
    menu()