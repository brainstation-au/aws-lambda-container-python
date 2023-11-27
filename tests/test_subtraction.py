from src.subtraction import handler

def test_handler():
    assert handler(dict(
        a = 5,
        b = 2
    ), None) == 3
