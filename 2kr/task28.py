import sys


def count_distinct_substrings(s):
    n = len(s)
    
    # Построение суффиксного массива и LCP
    suffixes = sorted([(s[i:], i) for i in range(n)])
    lcp = [0] * n
    
    # Вычисление LCP
    for i in range(1, n):
        a, b = suffixes[i-1][0], suffixes[i][0]
        j = 0
        while j < len(a) and j < len(b) and a[j] == b[j]:
            j += 1
        lcp[i] = j
    
    # Подсчёт различных подстрок
    total = n * (n + 1) // 2  # общее количество подстрок
    total -= sum(lcp)          # вычитаем повторяющиеся
    return total

s = sys.stdin.readline().strip()
print(count_distinct_substrings(s))