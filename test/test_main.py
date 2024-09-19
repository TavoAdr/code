from main import is_in_fibo, count_a

from pytest import mark

@mark.parametrize(('value', 'result'), (
    (30, False),
    (5, True),
    (7, False),
    (11, False),
    (1, True),
    (0, True),
    (3, True),
    (6, False),
))
def test_if_is_in_fibo(value, result):
    assert is_in_fibo(value) is result
    
@mark.parametrize(('text', 'amount'), (
    ('abacate', 3),
    ('tomate', 1),
    ('ovo', 0),
    ('boala', 2),
))
def test_count_a(text: str, amount: int):
    assert count_a(text) == amount