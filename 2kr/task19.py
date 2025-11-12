import math
import random
import sys


def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


class HashedString:
    def __init__(self, s: str, base=311, mod=10**9+7):
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod
        
        max_len = self.n + 5
        self.pows = [1] * (max_len)
        self.hashes = [0] * (self.n + 1)
        
        for i in range(1, max_len):
            self.pows[i] = (self.pows[i-1] * base) % mod
        
        for i in range(self.n):
            self.hashes[i+1] = (self.hashes[i] * base + ord(s[i])) % mod
    
    def get_hash(self, l: int, r: int):
        length = r - l
        h = (self.hashes[r] - self.hashes[l] * self.pows[length]) % self.mod
        if h < 0: 
            h += self.mod
        return h
    
    def __len__(self):
        return self.n
    
    def __str__(self):
        return self.s


def solution(n: int, m: int, s_str: str, t_str: str):
    s = HashedString(s_str)
    t = HashedString(t_str)

    pref_z = z_function(s_str + t_str)
    mx_prefix = pref_z[n]
    
    rs = s_str[::-1]
    rt = t_str[::-1]
    postf_z = z_function(rs + rt)
    mx_postfix = postf_z[n]

    count = 0

    for postf_l in range(0, mx_postfix):
        max_pref_l = min(mx_prefix, n - postf_l - 1) 
        
        for pref_l in range(0, max_pref_l + 1):
            delta_n = n - (pref_l + postf_l)
            delta_m = m - (pref_l + postf_l)
            
            if delta_n <= 0 or delta_m <= 0 or delta_m % delta_n != 0:
                continue
            
            hashed_middle_s = s.get_hash(pref_l, n - postf_l)
            found = True
            
            for i in range(pref_l, m - postf_l, delta_n):
                if hashed_middle_s != t.get_hash(i, i + delta_n):
                    found = False
                    break
            
            count += found

    return count


def main():
    input = sys.stdin.readline().split()
    n, m = int(input[0]), int(input[1])
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    solution(n, m, s, t)