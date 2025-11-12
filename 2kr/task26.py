def minimal_palindrome_extension(s):
    n = len(s)
    if n == 0:
        return ""
    
    t = ['#'] * (2 * n + 1)
    for i in range(n):
        t[2 * i + 1] = s[i]
    
    m = len(t)
    p = [0] * m
    center, right = 0, 0
    
    for i in range(m):
        if i < right:
            mirror = 2 * center - i
            p[i] = min(right - i, p[mirror])
        
        a = i + (1 + p[i])
        b = i - (1 + p[i])
        while a < m and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        
        if i + p[i] > right:
            center = i
            right = i + p[i]
    
    best_i = 0
    for i in range(m):
        if i + p[i] == m - 1:
            start = (i - p[i]) // 2
            if start < best_i or best_i == 0:
                best_i = start
    return s + s[:best_i][::-1]

def minimal_palindrome_extension_simple(s):
    n = len(s)
    
    def longest_palindromic_suffix(s):
        n = len(s)
        combined = s + '#' + s[::-1]
        m = len(combined)
        
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = pi[j - 1]
            if combined[i] == combined[j]:
                j += 1
            pi[i] = j
        
        return pi[m - 1]
    
    lps_len = longest_palindromic_suffix(s)
    
    if lps_len == n:
        return s
    
    return s + s[:n - lps_len][::-1]

if __name__ == "__main__":
    s1 = input().strip()
    # Используем простую версию с префикс-функцией
    result = minimal_palindrome_extension_simple(s1)
    print(result)