class Estudiante:

    CAMPOS = ("nombre", "apellido", "email", "carnet")
    OBLIGATORIOS = (
        "nombre",
        "apellido",
        "email",
        "carnet"
    )
    NOTA_MINIMA = 0
    NOTA_MAXIMA = 20

    total_creados = 0

    def __init__(
        self,
        id_estudiante,
        nombre,
        apellido,
        email,
        carnet,
        notas=None,
        materias=None
    ):

        self.__id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet

        self.__notas = dict(notas) if notas else {}
        self.__materias = set(materias) if materias else set()

        Estudiante.total_creados += 1

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        valor = str(valor).strip()

        if not valor:
            raise ValueError(
                "El nombre es obligatorio"
            )

        self.__nombre = valor.title()

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):

        valor = str(valor).strip()

        if not valor:
            raise ValueError(
                "El apellido es obligatorio"
            )

        self.__apellido = valor.title()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):

        valor = str(valor).strip()

        if "@" not in valor:
            raise ValueError(
                "El email no es válido"
            )

        self.__email = valor.lower()

    @property
    def carnet(self):
        return self.__carnet

    @carnet.setter
    def carnet(self, valor):

        valor = str(valor).strip().upper()

        if len(valor) < 4:
            raise ValueError(
                "El carnet debe tener al menos 4 caracteres"
            )

        self.__carnet = valor

    @property
    def materias(self):
        return set(self.__materias)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def promedio(self):

        todas = []

        for notas in self.__notas.values():
            todas.extend(notas)

        if not todas:
            return 0

        return round(
            sum(todas) / len(todas),
            2
        )

    def agregar_nota(self, materia, nota):

        if not (
            isinstance(nota, (int, float))
            and self.NOTA_MINIMA <= nota <= self.NOTA_MAXIMA
        ):
            raise ValueError(
                "La nota debe estar entre 0 y 20"
            )

        materia = str(materia).strip().title()

        if not materia:
            raise ValueError(
                "La materia es obligatoria"
            )

        self.__materias.add(materia)

        self.__notas.setdefault(
            materia,
            []
        ).append(nota)

    def notas_de(self, materia):

        materia = str(materia).strip().title()

        return list(
            self.__notas.get(
                materia,
                []
            )
        )

    def a_diccionario(self):

        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "email": self.__email,
            "carnet": self.__carnet,
            "notas": self.__notas,
            "materias": sorted(
                self.__materias
            )
        }

    @classmethod
    def desde_diccionario(cls, datos):

        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["carnet"],
            notas=datos.get(
                "notas",
                {}
            ),
            materias=datos.get(
                "materias",
                []
            )
        )

    def __str__(self):

        return (
            f"[{self.id}] "
            f"{self.nombre_completo} "
            f"| Carnet: {self.carnet} "
            f"| Promedio: {self.promedio}"
        )