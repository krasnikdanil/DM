class Integer:
    """Класс для целых чисел"""
    value: str

    def parsing_integer(self, value: str):
        if len(value) == 0:
            raise ValueError("Нужно ввести целое число")

        try:
            parsed = int(value)
        except ValueError:
            raise ValueError("Нужно ввести целое число")

        self.value = str(parsed)

    def __init__(self, value: str = "0"):
        self.parsing_integer(value)

    def __str__(self):
        return self.value