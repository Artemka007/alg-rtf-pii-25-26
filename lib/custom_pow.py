def custom_pow(n: int, base: int):
    res = 1

    while base != 0:
        if base & 1:
            res = res * n
    
        n = n * n
        base >>= 1
    
    return res
