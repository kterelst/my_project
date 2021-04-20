def power(x, y):
    try:
        return str(int(x)**int(y))
    except ValueError:
        return "invalid input"
