class Integer:
    value: str

    def parsing_int(self, value: str):
       # Парсит строку и устанавливает значение целого числа
        if len(value) == 0:
            raise ValueError("Нужно ввести целое число")
        if value[0] == '-':
            if value[1:].isdigit():
                self.value = value # сохраняем отрицательное значение
            else:
                raise ValueError("Нужно ввести целое число")
        elif value.isdigit():
            self.value = value
        else:
            raise ValueError("Нужно ввести целое число")

    def __str__(self):
        """Возвращает строковое представление целого числа"""
        return f"{self.value}"

    def __init__(self, value: str = "0"):
        self.parsing_int(value)
