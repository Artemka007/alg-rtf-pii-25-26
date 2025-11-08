from typing import Dict, List, Tuple


def solution(N, M, K, *items: Tuple[int, int]):
    teammeits: Dict[int, List[int]] = {}

    for (key, val) in items:
        if not teammeits.get(key):
            teammeits[key] = []

        if not teammeits.get(val):
            teammeits[val] = []

        teammeits[key].append(val)
        teammeits[val].append(key)
    
    teammeits = {
        key: teammeits[key] for key in sorted(teammeits, key=lambda x: len(teammeits[x]), reverse=True)
    }

    res = []
    total_count = 0

    for key, val in teammeits.items():
        if total_count == K:
            break
        
        if key in res:
            continue
        
        if len(val) + 1 > K - total_count:
            continue
        
        res.append(key)

        for i in val:
            res.append(i)

        total_count += len(val) + i
        
    return res

print(solution(5, 3, 3, (1, 3), (2, 5), (5, 4)))