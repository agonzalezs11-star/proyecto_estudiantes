from views import EstudianteController
from shared.herramientas import (
    imprimir_titulo,
    imprimir_exito,
    imprimir_error,
    imprimir_info
)


def pausa():
    input("\nPresione Enter para continuar...")


def menu():

    while True:

        imprimir_titulo("SISTEMA DE ESTUDIANTES")

        print("1. Crear estudiante")
        print("2. Ver estudiantes")
        print("3. Buscar")
        print("4. Agregar nota")
        print("5. Eliminar")
        print("0. Salir")

        opcion = input("\nOpción: ")

        if opcion == "1":

            datos = {}

            for campo in EstudianteController.MODELO.CAMPOS:
                datos[campo] = input(f"{campo}: ")

            exito, mensaje = EstudianteController.crear(datos)

            if exito:
                imprimir_exito(mensaje)
            else:
                imprimir_error(mensaje)

            pausa()

        elif opcion == "2":

            imprimir_titulo("LISTA DE ESTUDIANTES")

            estudiantes = EstudianteController.listar()

            if not estudiantes:
                imprimir_info("No hay estudiantes registrados.")
            else:
                for estudiante in estudiantes:
                    print(estudiante)

            pausa()

        elif opcion == "3":

            termino = input("Buscar: ")

            encontrados = EstudianteController.buscar(termino)

            if not encontrados:
                imprimir_info("No se encontraron coincidencias.")
            else:
                for estudiante in encontrados:
                    print(estudiante)

            pausa()

        elif opcion == "4":

            id_est = int(input("ID del estudiante: "))
            materia = input("Materia: ")
            nota = float(input("Nota: "))

            exito, mensaje = EstudianteController.agregar_nota(
                id_est,
                materia,
                nota
            )

            if exito:
                imprimir_exito(mensaje)
            else:
                imprimir_error(mensaje)

            pausa()

        elif opcion == "5":

            id_est = int(input("ID del estudiante: "))

            exito, mensaje = EstudianteController.eliminar(id_est)

            if exito:
                imprimir_exito(mensaje)
            else:
                imprimir_error(mensaje)

            pausa()

        elif opcion == "0":

            imprimir_info("Hasta luego.")
            break

        else:

            imprimir_error("Opción inválida.")
            pausa()


if __name__ == "__main__":
    menu()
    