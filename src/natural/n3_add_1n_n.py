from src.natural.natural import Natural

#Добавляем 1 к натуральному числу
class Add1nn(Natural):
    def add_1n_n(self) -> 'Natural':
        result_value = str(int(self.value) + 1)
        return result_value
