def divide(num1, num2, floor = True):
    try:
        if floor == False:
            return num1 / num2
        return num1 // num2
    except TypeError:
        return 'Invalid Input Type. Please make sure that you enter a valid number'