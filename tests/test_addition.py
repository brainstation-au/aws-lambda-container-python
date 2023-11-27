from src.addition import handler

def test_handler():
    assert handler(dict(
        a = 3,
        b = 2
    ), None) == 5
