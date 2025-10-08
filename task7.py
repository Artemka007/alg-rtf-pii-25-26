from lib import quick_sort


def solution(N, *args):
    min_delta = 10**9

    args = list(args)
    quick_sort.quick_sort(args)
    
    sm = [0]

    for i in range(N):
        sm.append(sm[i] + args[i])
    
      
    for k in range(1, N):
        for j in range(N + 1 - k):
            max_init = sm[len(sm) - 1]

            sm1 = max_init - (sm[k + j] - sm[j])
            sm2 = max_init - sm1

            min_delta = min(min_delta, abs(sm1 - sm2))
    
    return min_delta

print(solution(6, 14, 2, 12, 9, 9, 8))