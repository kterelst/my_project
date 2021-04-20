def power(x, y):
    try:
        return int(x)**int(y)
    except ValueError:
        return "invalid input"
