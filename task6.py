from lib import custom_pow


def solution(N: int, M: int, MOD: int, *args):
    for j in range(N + 1, M + N + 1):
        res = 0
        for i in range(N + 1):
            res += args[i] * custom_pow.custom_pow(args[j], (N - i))
        yield res % MOD

# N, M, MOD = [int(i) for i in input().split(' ')]

# args = []

# for i in range(N + M + 1):
#     args.append(int(input()))

for i in solution(2, 5, 10, 1, 5, 4, 0, 1, 2, 3, 4):
    print(i)