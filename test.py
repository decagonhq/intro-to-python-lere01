def generator_function():
    n = 200

    while n <= 10000:
        if n % 2 == 0:
            yield n
            
        n += 1