from lib.hash import Hash
from lib.hashed_str import HashedStr


def solution(s: str):
    s = HashedStr(s)

    mx_freq = 0
    mx_weight = 0

    n = len(s)

    for length in range(n, 0, -1):
        possible_max = (n - length + 1) * length
        if possible_max <= mx_weight:
            continue
        hash_table = Hash()
        for start in range(0, n - length + 1):
            substr_hash = s.get_substr_hash(start, length)
            el = hash_table.get(substr_hash)
            if not el:
                hash_table[substr_hash] = 0
            hash_table[substr_hash] += 1
            if mx_freq < hash_table[substr_hash]:
                mx_freq = hash_table[substr_hash]
        if mx_weight < mx_freq * length:
            mx_weight = mx_freq * length
        mx_freq = 0
    return mx_weight
