from functools import lru_cache

def solution(N: int, M: int, MOD: int, *args):
    coefficients = tuple(args[:N+1])
    
    @lru_cache(maxsize=None)
    def evaluate_polynomial(x):
        result = 0
        power = 1
        # Вычисляем от младших степеней к старшим
        for coeff in reversed(coefficients):
            result = (result + coeff * power) % MOD
            power = (power * x) % MOD
        return result
    
    for j in range(N + 1, M + N + 1):
        yield evaluate_polynomial(args[j])
# N, M, MOD = [int(i) for i in input().split(' ')]

# args = []

# for i in range(N + M + 1):
#     args.append(int(input()))

for i in solution(2, 5, 10, 1, 5, 4, 0, 1, 2, 3, 4):
    print(i)