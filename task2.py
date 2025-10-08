def solution(n, *rows):
    counter = 0
    numbers = {}
    
    for i in rows:
        for j in i:
            if j == '.':
                continue
            j = int(j)
            if not numbers.get(j):
                numbers[j] = 1
            numbers[j] += 1
    
    for i in range(1, 10):
        counter += bool(numbers.get(i) and numbers[i] <= n * 2)
    
    return counter

print(solution(4, '1111', '9999', '1111', '1199'))
        