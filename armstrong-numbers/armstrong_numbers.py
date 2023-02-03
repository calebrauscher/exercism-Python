def is_armstrong_number(number):
    ''' Determine if given number is an armstrong number. An armstrong number
        is a number that is the sum of its own digits each raised to the power
        of the number of digits.
    '''
    numbers = [int(_) for _ in str(number)]
    power = len(numbers)
    return number == sum([int(x)**power for x in numbers])
