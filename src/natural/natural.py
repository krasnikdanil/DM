""" Выполнял Зацепин Тимофей 4384 """
class Natural:

    values: list[int]

    """ Проверка на Natural """
    def parsing_numbern(self, value: str):
        if not value.isdigit():
            raise ValueError("Вы ввели не натуральное число")
        return [int(digit) for digit in reversed(value)]
    
    """ Инцализация Natural """
    def __init__(self, value: str = "0"):
        self.values = self.parsing_numbern(value)
    
    """ Вывод Natural """
    def __str__(self) -> str:
        return "".join(map(str, self.values))[::-1]
    
    ''' Сравнение на Natural на ==  '''
    def __eq__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        return self.values == other.values
    ''' Сравнение на Natural на !=  '''
    def __ne__(self, other: Natural) -> bool:
        return not self == other
    ''' Сравнение на Natural на <  '''
    def __lt__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        len1 = len(self.values)
        len2 = len(other.values)
        if len1 != len2:
            return len1 < len2
        # Сравниваем цифры от старших разрядов к младшим
        for i in range(len1 - 1, -1, -1):
            if self.values[i] != other.values[i]:
                return self.values[i] < other.values[i]
        return False
    ''' Сравнение на Natural на >  '''
    def __gt__(self, other: Natural) -> bool:
        if not isinstance(other, Natural):
            return NotImplemented
        len1 = len(self.values)
        len2 = len(other.values)
        if len1 != len2:
            return len1 > len2
        # Сравниваем цифры от старших разрядов к младшим
        for i in range(len1 - 1, -1, -1):
            if self.values[i] != other.values[i]:
                return self.values[i] > other.values[i]
        return False
    ''' Сравнение на Natural на <=  '''
    def __le__(self, other: Natural) -> bool:
        return self < other or self == other
    ''' Сравнение на Natural на >=  '''
    def __ge__(self, other) -> bool:
        return self > other or self == other

    """ Унарный + для Natural """
    def __pos__(self):
        return self

    @staticmethod
    def _format(lnumber: list[int]) -> Natural:
        result = Natural()
        result.values = lnumber
        return result
    
    """ Сложение Natural с Natural """
    def __add__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            raise ValueError("Сложение подерживаетя только для N чисел")
        # Длина наибольшого числа
        maxln = max(len(self.values), len(other.values))
        # Результат сложения
        result = []
        # Остаток после сложения
        remnant = 0
        for i in range(maxln):
            num1 = self.values[i] if len(self.values) > i else 0
            num2 = other.values[i] if len(other.values) > i else 0
            number = num1 + num2 + remnant
            result.append(number%10)
            remnant = number // 10
        if remnant != 0:
            result.append(remnant)
        return Natural._format(result)
    
    """ Вычитание Natural из Natural """
    def __sub__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            raise ValueError("Вычитание поддерживается только для натуральных чисел")
        if self < other:
            raise ValueError("Результат вычитания не может быть отрицательным")
        result_digits = []
        borrow = 0
        len1 = len(self.values)
        len2 = len(other.values)
        for i in range(len1):
            digit1 = self.values[i]
            digit2 = other.values[i] if i < len2 else 0
            # Вычитание с учетом заёма
            diff = digit1 - digit2 - borrow
            if diff < 0:
                # Если результат отрицательный, занимаем 10
                diff += 10
                borrow = 1
            else:
                # Заём не нужен
                borrow = 0
            result_digits.append(diff)
        # Удаление лидирующих нулей
        # (например, 105 - 102 = 003 -> 3)
        while len(result_digits) > 1 and result_digits[-1] == 0:
            result_digits.pop()        
        return Natural._format(result_digits)
    
    """ Умножение Natural из Natural """
    def __mul__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            raise ValueError("Умножение поддерживается только для натуральных чисел")

        # Если одно из чисел 0, результат 0
        if self.values == [0] or other.values == [0]:
            return Natural("0")

        total_res = Natural("0")
        
        # Итерация по каждой цифре второго числа
        for i, digit_b in enumerate(other.values):
            carry = 0
            current_res_digits = []
            
            # Умножение первого числа на одну цифру второго
            for digit_a in self.values:
                prod = digit_a * digit_b + carry
                current_res_digits.append(prod % 10)
                carry = prod // 10
            
            if carry > 0:
                current_res_digits.append(carry)
            # Сдвиг результата
            # Умножение на 10, 100, 1000 и т.д.
            # эквивалентно добавлению нулей в начало перевернутого списка
            shifted_digits = [0] * i + current_res_digits
            # Создаем Natural из промежуточного результата
            current_res_natural = Natural._format(shifted_digits)
            
            # Суммируем с общим результатом
            total_res += current_res_natural
        return total_res

    """ Деление Natural на Natural """
    def __floordiv__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            raise ValueError("Деление поддерживается только для натуральных чисел")
        if other.values == [0]:
            raise ZeroDivisionError("Деление на ноль")

        if self < other:
            return Natural("0")
        if self == other:
            return Natural("1")

        # Предвычисляем multiples: other * d для d от 1 до 9
        multiples = {d: other * Natural(str(d)) for d in range(1, 10)}

        res = Natural("0")
        cur = Natural("0")

        # Перебираем цифры делимого с старших разрядов
        for i in range(len(self.values) - 1, -1, -1):
            digit = self.values[i]
            # Сдвигаем текущее значение влево на один разряд и добавляем новую цифру
            cur = cur * Natural("10") + Natural(str(digit))

            if cur < other:
                # Цифра частного = 0
                res = res * Natural("10")
            else:
                # Подбираем максимальную цифру d (от 9 до 1), такую что multiples[d] <= cur
                chosen_d = 0
                for d in range(9, 0, -1):
                    if multiples[d] <= cur:
                        chosen_d = d
                        break
                # Вычитаем multiples[chosen_d] из cur
                cur = cur - multiples[chosen_d]
                # Добавляем chosen_d к результату
                res = res * Natural("10") + Natural(str(chosen_d))

        return res
             
    def __mod__(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            raise ValueError("Деление поддерживается только для натуральных чисел")
        if other.values == [0]:
            raise ZeroDivisionError("Деление на ноль")

        if self < other:
            return self

        # Предвычисляем other * d для d от 1 до 9
        multiples = {d: other * Natural(str(d)) for d in range(1, 10)}

        cur = Natural("0")  # Текущий остаток при делении

        # Обрабатываем цифры делимого справа налево (старшие разряды первыми)
        for i in range(len(self.values) - 1, -1, -1):
            digit = self.values[i]
            cur = cur * Natural("10") + Natural(str(digit))  # "Опускаем" цифру

            if cur >= other:
                # Подбираем максимальную цифру d (9 до 1), чтобы multiples[d] <= cur
                chosen_d = 0
                for d in range(9, 0, -1):
                    if multiples[d] <= cur:
                        chosen_d = d
                        break
                cur = cur - multiples[chosen_d]  # Вычитаем из остатка

        return cur  # Остаток от деления
    
    """ Сравнение натуральных чисел: 
    2 - если первое больше второго,
    0, если равно, 1 иначе. """
    def comnn(self, other: Natural) -> str:
        if self > other:
            return "2"
        if self == other:
            return "0"
        else:
            return "1"
    
    """ Проверка на ноль: если число не равно нулю, 
        то «да» иначе «нет» """
    def nzernb(self) -> str:
        if self.values != [0]:
            return "Дa"
        else:
            return "Нет"
    
    """ Вычитание из первого большего натурального числа
    второго меньшего или равного """
    def subnn(self, other: Natural) -> Natural:
        result = self - other if self > other else other - self
        return result
        
    """ Умножение натурального числа на 10^k """
    def mul_10k(self, k: int) -> Natural:
        if k < 0:
            raise ValueError("Степень k не может быть отрицательной")
        if k == 0:
            # Возвращаем копию, чтобы избежать неожиданных изменений
            return Natural(str(self))

        # Добавляем k нулей в начало перевернутого списка
        new_values = [0] * k + self.values

        # Создаем новый объект Natural с результатом
        result = Natural()
        result.values = new_values
        # Убираем возможный лидирующий ноль, если исходное число было 0
        if len(result.values) > 1 and result.values[-1] == 0:
            result.values = [0]
        return result

    """ Вычитание из натурального другого натурального, умноженного на цифру """
    def sub_mul_digit(self, other: Natural, digit: int) -> Natural:
        if not 0 <= digit <= 9:
            raise ValueError("'digit' должен быть от 0 до 9")
        
        product = other * Natural(str(digit))
        
        if self < product:
            raise ValueError("Результат вычитания не может быть отрицательным")
            
        return self - product


        """ Вычисляет первую цифру деления (self / other) и её позицию k.
        Возвращает кортеж (цифра, k). """
    def div_first_digit(self, other: Natural) -> tuple[int, int]:
        if not isinstance(other, Natural) or other.values == [0]:
            raise ValueError("Делитель должен быть натуральным числом, не равным нулю.")

        if self < other:
            return 0, 0

        len_self = len(self.values)
        len_other = len(other.values)
        
        # Определяем "рабочую" часть делимого
        len_cur = len_other
        cur_values = self.values[len_self - len_cur:]
        cur = Natural("".join(map(str, reversed(cur_values))))

        # Определяем позицию k
        k = len_self - len_cur
        
        if cur < other:
            # Если "рабочей" части не хватило, берем еще одну цифру
            len_cur += 1
            # И позиция k, соответственно, уменьшается
            k = len_self - len_cur
            # Проверяем, не вышли ли мы за пределы
            if k < 0:
                # Это случай, когда self > other, но разница в длине 0
                # и старшие цифры self меньше. Например 899 / 900
                # Но мы уже проверили self < other, так что сюда не попадем.
                # Оставляем для надежности.
                return 0, 0
            cur_values = self.values[len_self - len_cur:]
            cur = Natural("".join(map(str, reversed(cur_values))))

        # Находим, сколько раз other помещается в cur
        l, r = 1, 10
        while r - l > 1:
            m = (l + r) // 2
            if other * Natural(str(m)) > cur:
                r = m
            else:
                l = m
        # l - это и есть искомая первая цифра
        return l, k

    """ Вычисление НОД по алгоритму Евклида. """
    def gcd(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            raise ValueError("Аргумент должен быть натуральным числом.")

        a = Natural(str(self))
        b = Natural(str(other))
        
        zero = Natural("0")

        while b > zero:
            a, b = b, a % b
        
        return a

    """ Вычисление НОК (Наименьшего Общего Кратного).
    НОК(a, b) = (a * b) / НОД(a, b) """
    def lcm(self, other: Natural) -> Natural:
        if not isinstance(other, Natural):
            raise ValueError("Аргумент должен быть натуральным числом.")

        # Обработка случая с нулем
        if self.values == [0] or other.values == [0]:
            return Natural("0")

        # Вычисляем произведение
        product = self * other
        
        # Вычисляем НОД
        greatest_common_divisor = self.gcd(other)
        
        # Возвращаем результат деления
        return product // greatest_common_divisor
