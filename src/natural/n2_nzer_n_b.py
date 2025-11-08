from src.natural.natural import Natural


class NaturalZeroCheck(Natural):
    """Дочерний класс для проверки натурального числа на ноль"""

    def is_not_zero(self) -> str:
        """Проверка на ноль: если число не равно нулю, то 'да' иначе 'нет'"""
        if int(self.value) != 0:
            return "да"
        else:
            return "нет"