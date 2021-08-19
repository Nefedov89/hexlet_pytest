def reverse(str):
    """Reverse string

        >>> reverse('')
        ''

        >>> reverse('Hexlet')
        'telxeH'
    """
    return str[::-1]


if __name__ == "__main__":
    # import doctest
    doctest.testmod()