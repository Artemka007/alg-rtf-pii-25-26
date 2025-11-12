import sys
from typing import TextIO


def get_next_char(s: str, index: int):
    n = len(s)
    while index < n:
        if s[index].islower():
            yield s[index]
            index += 1
        elif s[index].isdigit():
            num = 0
            while index < n and s[index].isdigit():
                num = num * 10 + int(s[index])
                index += 1
            index += 1
            bracket_count = 1
            start = index
            while index < n and bracket_count > 0:
                if s[index] == '[':
                    bracket_count += 1
                elif s[index] == ']':
                    bracket_count -= 1
                index += 1
            sub_str = s[start:index-1]
            for _ in range(num):
                sub_gen_copy = get_next_char(sub_str, 0)
                for ch in sub_gen_copy:
                    yield ch
        else:
            index += 1


def solution(stream: TextIO):
    n = int(stream.readline())

    generators = []
    for _ in range(n):
        line = stream.readline()
        gen = get_next_char(line, 0)
        generators.append(gen)
    
    common_prefix = []

    for _ in range(10**5):
        char = None
        found = False
        try:
            for gen in generators:
                if char is None:
                    char = next(gen)
                elif char != next(gen):
                    found = True
                    break
        except StopIteration:
            break
        
        if found:
            break
        
        common_prefix.append(char)
    
    return common_prefix
