from src.integer import Integer
from src.integer.z4_trans_n_z import Trans_n_z

def test_trans_natural_positive_to_integer():
    """Тест преобразования положительного натурального числа в целое"""
    natural_number = '5'
    result = Trans_n_z(natural_number)
    assert isinstance(result, Integer)
    assert result.value == '5'

def test_trans_natural_zero_to_integer():
    """Тест преобразования нуля в целое число"""
    natural_number = '0'
    result = Trans_n_z(natural_number)
    assert isinstance(result, Integer)
    assert result.value == '0'

def test_trans_large_natural_to_integer():
    """Тест преобразования большого натурального числа в целое"""
    natural_number = '1234567890'
    result = Trans_n_z(natural_number)
    assert isinstance(result, Integer)
    assert result.value == '1234567890'

def test_trans_natural_one_to_integer():
    """Тест преобразования единицы в целое число"""
    natural_number = '1'
    result = Trans_n_z(natural_number)
    assert isinstance(result, Integer)
    assert result.value == '1'
