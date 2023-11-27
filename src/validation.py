def get_numbers(event):
    number_a = event.get('a')
    number_b = event.get('b')
    if not isinstance(number_a, int) or not isinstance(number_b, int):
        raise ValueError('event doesn\'t satisfy the type { a: number, b: number }')

    return number_a, number_b
