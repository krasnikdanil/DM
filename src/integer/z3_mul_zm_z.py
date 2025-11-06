from src.integer.integer import Integer

""" К целому числу прибавляем единицу"""
class Mulzmz(Integer):
    def mul_zm_z(self) -> str:
        # Получаем числовое значение и меняем его знак на противоположный
        return str(int(self.value) * -1)
