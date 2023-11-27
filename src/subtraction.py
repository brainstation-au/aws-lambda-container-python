from .validation import get_numbers

def handler(event, context):
    number_a, number_b = get_numbers(event)
    return number_a - number_b
