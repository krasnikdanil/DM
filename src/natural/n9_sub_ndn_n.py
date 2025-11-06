from src.natural.natural import Natural

# Вычитание из натурального другого натурального, умноженного на цифру
# для случая с неотрицательным результатом
class Subndnn(Natural):
    def sub_ndn_n(self, other: 'Natural', d: int):
        if 0 > d or d > 9:
            raise ValueError("d должно быть цифрой")
        result = int(self.value) - int(other.value) * d
        if result < 0:
            raise ValueError("Результат не должен быть отрицательным!")
        return str(result)