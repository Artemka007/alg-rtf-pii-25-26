import io
import time
import tracemalloc
from typing import List, Dict, Any

from task22 import solution
from test_func import universal_test_solution

def run_tests():
    test_cases = [
        # Пример 1 из условия
        {
            'input': io.StringIO("3\n2[a]2[ab]\n3[a]2[r2[t]]\na2[aa3[b]]"),
            'expected': ['a', 'a', 'a']
        },
        
        # Пример 2 из условия
        {
            'input': io.StringIO("3\nabacabaca\n2[abac]a\n3[aba]"),
            'expected': ['a', 'b', 'a']
        },
        
        # Производительный тест 1: одинаковые простые строки
        {
            'input': io.StringIO("100\n" + "a" * 1000 + "\n" * 99 + "a" * 1000),
            'expected': ['a'] * 1000
        },
        
        # Производительный тест 2: глубоко вложенные повторения
        {
            'input': io.StringIO("10\n" + "2[3[4[5[a]]]]\n" * 9 + "2[3[4[5[a]]]]"),
            'expected': ['a'] * 120
        },
        
        # Производительный тест 3: много строк с небольшими повторениями
        {
            'input': io.StringIO("500\n" + "10[abc]\n" * 499 + "10[abc]"),
            'expected': ['a', 'b', 'c'] * 10
        },
        
        # Производительный тест 4: строки с цифрами в начале
        {
            'input': io.StringIO("200\n" + "5[x]3[y]2[z]\n" * 199 + "5[x]3[y]2[z]"),
            'expected': ['x'] * 5
        },
        
        # Производительный тест 5: смешанные простые и сложные строки
        {
            'input': io.StringIO("300\n" + "simple\n" * 150 + "2[com2[plex]]\n" * 149 + "2[com2[plex]]"),
            'expected': []  # разные первые символы
        },
        
        # Производительный тест 6: максимально допустимая длина после распаковки
        {
            'input': io.StringIO("50\n" + "1000[a]\n" * 49 + "1000[a]"),
            'expected': ['a'] * 1000
        },
        
        # Производительный тест 7: строки с разными префиксами
        {
            'input': io.StringIO("100\n" + "abc" * 100 + "\n" * 99 + "abd" * 100),
            'expected': ['a', 'b']
        },
        
        # Производительный тест 8: сложная вложенность
        {
            'input': io.StringIO("20\n" + "2[3[2[a]2[b]]4[c]]\n" * 19 + "2[3[2[a]2[b]]4[c]]"),
            'expected': ['a'] * 12
        },
        
        # Производительный тест 8: сложная вложенность
        {
            'input': io.StringIO("1000\n" + "1000[a]1000[b]1000[c]1000[d]1000[e]1000[f5[g]]\n"*999 +"10000[a]\n"),
            'expected': ['a'] * 1000
        }
    ]

    results = universal_test_solution(
        solution,
        test_cases,
        show_input_preview=2,
        show_output_preview=3,
        include_time=True,
        include_memory=True,
        verbose=True,
        copy_to_clipboard=True
    )
    
    return results

# Запуск тестов
if __name__ == "__main__":
    run_tests()