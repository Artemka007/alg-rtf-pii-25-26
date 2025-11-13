import sys

class HashedString:
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
        # [l, r)
        h = (self.hashes[r] - self.hashes[l] * self.pows[r-l]) % self.mod
        return h if h >= 0 else h + self.mod

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    
    d = m - n
    hs = HashedString(s)
    ht = HashedString(t)
    
    count = 0
    
    # Перебираем делители d
    for b in range(1, d + 1):
        if d % b != 0:
            continue
            
        k = d // b + 1
        
        # Перебираем возможные длины префикса
        for a in range(0, n - b + 1):
            c = n - a - b
            
            if c < 0:
                continue
                
            # Проверяем префикс
            if a > 0 and hs.get_hash(0, a) != ht.get_hash(0, a):
                continue
                
            # Проверяем суффикс
            if c > 0 and hs.get_hash(n - c, n) != ht.get_hash(m - c, m):
                continue
                
            # Проверяем среднюю часть в s
            y_hash = hs.get_hash(a, a + b)
            
            # Проверяем все вхождения y в t
            valid = True
            for i in range(a, m - c, b):
                if ht.get_hash(i, i + b) != y_hash:
                    valid = False
                    break
                    
            if valid:
                count += 1
    
    print(count)

if __name__ == "__main__":
    main()