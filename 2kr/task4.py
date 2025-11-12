from lib import quick_sort
from lib.hash import Hash


def solution(N: int, items: list[str]):
    hasht = Hash(N)

    for i in items:
        hasht.put(i, True)
    
    result = []

    for s in items:
        l = len(s)
        if l < 2:
            continue
        
        for i in range(1, l):
            pref = s[:i]
            postf = s[i:]

            if hasht.get(pref) and hasht.get(postf):
                result.append(s)

    quick_sort.quick_sort(result)

    return result

print(solution(2, ['ab', 'ba']))