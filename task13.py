import math

def solution(N: int):
    dp = [None, True, False, True] + [False] * (N - 3)

    for i in range(N + 1):
        max_take = int(math.isqrt(i))
        
        for take in range(1, max_take + 1):
            if not dp[i - take]:
                dp[i] = True
                break
    
    print(dp)
            
    return "Second" if dp[N] else "First"

if __name__ == "__main__":
    N = int(input().strip())
    
    print(solution(N))