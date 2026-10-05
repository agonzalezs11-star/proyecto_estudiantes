import os

COLORES = {
    "ROJO": "\033[91m",
    "VERDE": "\033[92m",
    "AZUL": "\033[94m",
    "AMARILLO": "\033[93m",
    "CYAN": "\033[96m",
    "BLANCO": "\033[97m",
    "RESET": "\033[0m",
}

RESPUESTAS_SI = (
    "si",
    "sí",
    "s",
    "yes",
    "y"
)

def limpiar_pantalla():
    os.system(
        "cls" if os.name == "nt" else "clear"
    )

def imprimir_color(texto, color):

    codigo = COLORES.get(
        color,
        COLORES["BLANCO"]
    )

    print(
        f"{codigo}"
        f"{texto}"
        f"{COLORES['RESET']}"
    )

def imprimir_titulo(texto):

    limpiar_pantalla()

    imprimir_color(
        "=" * 60,
        "AZUL"
    )

    print(
        texto.center(60)
    )

    imprimir_color(
        "=" * 60,
        "AZUL"
    )

def imprimir_exito(mensaje):

    imprimir_color(
        f"✓ {mensaje}",
        "VERDE"
    )

def imprimir_error(mensaje):

    imprimir_color(
        f"✗ {mensaje}",
        "ROJO"
    )

def imprimir_info(mensaje):

    imprimir_color(
        f"ℹ {mensaje}",
        "CYAN"
    )

def confirmar(pregunta):

    respuesta = input(
        f"{pregunta} (si/no): "
    )

    return (
        respuesta.strip().lower()
        in RESPUESTAS_SI
    )

def pausa():

    input(
        "\nPresione Enter para continuar..."
    )
