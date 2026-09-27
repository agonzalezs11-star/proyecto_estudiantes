from models import Estudiante
from shared.json_manager import GestorJSON
from views import ClienteController


class EstudianteController(ClienteController):
    """Hereda las 5 operaciones. Solo cambia la configuración."""

    MODELO = Estudiante
    ARCHIVO = "data/estudiantes.json"
    CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "carnet")
    _gestor = GestorJSON(ARCHIVO)

    @classmethod
    def carnets_registrados(cls, excepto_id=None):
        """Igual que emails_registrados, pero con el campo carnet."""
        return {
            registro["carnet"].upper()
            for registro in cls._registros()
            if registro["id"] != excepto_id
        }

    @classmethod
    def agregar_nota(cls, id_estudiante, materia, nota):
        """Obtiene el estudiante, agrega la nota y vuelve a guardar."""

        try:
            estudiante = cls.obtener(id_estudiante)

            if estudiante is None:
                return False, f"No existe un estudiante con id {id_estudiante}"

            estudiante.agregar_nota(materia, nota)

            registros = cls._registros()

            for i, registro in enumerate(registros):
                if registro["id"] == id_estudiante:
                    registros[i] = estudiante.a_diccionario()
                    break

            cls._gestor.guardar(registros)

            return True, f"Nota agregada a {estudiante.nombre_completo}"

        except ValueError as error:
            return False, str(error)