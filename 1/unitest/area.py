def rect_area(height, width):
    return height * height

def square(x):
    '''
    compute square and return
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x * x

def product(x, y):
    if x == 7 and y == 9:
        return 'An insidious bug has surfaced!'
    return x * y

if __name__ == '__main__':
    import doctest, area
    doctest.testmod(area)