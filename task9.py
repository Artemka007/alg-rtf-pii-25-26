def solution(n: int, m: int):
    if m == 0:
        return 1
    
    if m == 1:
        return n
    
    res = 0

    for i in range(1, n + 1):
        ocuppied_places_count = (m - 1) * i + 1

        if ocuppied_places_count > n:
            break
        
        res += n - ocuppied_places_count + 1

    return res

print(solution(1000, 3))