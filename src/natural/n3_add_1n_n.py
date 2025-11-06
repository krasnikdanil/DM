from src.natural.natural import Natural

class Add1n(Natural):
    #Класс для добавления 1 к натуральному числу
    def add_1n(self) -> 'Natural':
        result_value = str(int(self.value) + 1)
        return Natural(result_value)
