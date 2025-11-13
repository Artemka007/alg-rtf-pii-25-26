import sys

class HashedString(str):
    def __init__(self, s, base=311, mod=10**9+7):
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod
        
        self.pows = [1] * (self.n + 1)
        self.hashes = [0] * (self.n + 1)
        
        for i in range(1, self.n + 1):
            self.pows[i] = (self.pows[i-1] * base) % mod
            self.hashes[i] = (self.hashes[i-1] * base + ord(s[i-1])) % mod
    
    def get_hash(self, l, r):
        h = (self.hashes[r] - self.hashes[l] * self.pows[r-l]) % self.mod
        return h if h >= 0 else h + self.mod
    
def solution(n: int, m: int, s: str, t: str):
    s: HashedString = HashedString(s)
    t: HashedString = HashedString(t)
    count = 0

    max_prefix = 0
    while max_prefix < n and s[max_prefix] == t[max_prefix]:
        max_prefix += 1

    max_suffix = 0
    while max_suffix < n and s[n - 1 - max_suffix] == t[m - 1 - max_suffix]:
        max_suffix += 1

    for l in range(1, n):
        min_i = n - max_suffix + l
        max_i = max_prefix
        
        if min_i > max_i:
            continue

        if (min_i + m - max_prefix) % l != 0:
            continue

        found = False
        h = s.get_hash(min_i - l, min_i)
        for i in range(min_i + l, m - max_prefix, l):
            if h != t.get_hash(i - l, i):
                found = False
                break
        count += (max_i - min_i + 1) if found else 0


    return count

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    print(solution(n, m, s, t))

main()