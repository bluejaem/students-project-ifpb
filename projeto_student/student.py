class Student:
    def __init__(self, student_id: int, name: str, house: str):
        self.id = student_id
        self.name = name
        self.house = house

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, student_id: int):
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("ID deve ser um número inteiro positivo.")
        self._id = student_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if not name or not name.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._name = name.strip()

    @property
    def house(self) -> str:
        return self._house

    @house.setter
    def house(self, house: str):
        if not house or not house.strip():
            raise ValueError("Casa não pode ser vazia.")
        self._house = house.strip()

    def __str__(self) -> str:
        return f"ID: {self.id} | {self.name} ({self.house})"