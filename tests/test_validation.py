import pytest

from src.validation import get_numbers

def test_validation_for_valid_values():
    assert get_numbers(dict(
        a = 3,
        b = 2
    )) == (3, 2)

def test_validation_for_valid_values():
    with pytest.raises(ValueError):
        get_numbers(dict(
            a = 3
        ))

def test_validation_for_valid_values():
    with pytest.raises(ValueError):
        get_numbers(dict(
            a = 3,
            b = 'x'
        ))
