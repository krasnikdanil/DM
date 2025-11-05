from src.common.errors import NaturalError


class Natural:
    """Класс для натуральных чисел"""
    value: str

    def parsing_natural(self, value: str):
        """Парсит строку и устанавливает значение натурального числа"""
        if len(value) == 0:
            raise NaturalError("Нужно ввести натуральное число")
        if value.isdigit() and int(value) > 0:
            self.value = value
        else:
            raise NaturalError("Нужно ввести натуральное число")

    def __str__(self):
        """Возвращает строковое представление натурального числа"""
        return f"{self.value}"

    def __init__(self, value: str = "1"):
        self.parsing_natural(value)