from src import code1

def test_sumnumbers():
    result1, result2 = code1.sum_numbers(2, 1)
    assert result1 == 3
    assert result2 == 1
