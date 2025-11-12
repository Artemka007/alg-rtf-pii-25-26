import math
import random
import string
from typing import List, Dict, Any

from task19 import solution
from test_func import universal_test_solution

def generate_random_string(length: int, char_pool: str = string.ascii_lowercase) -> str:
    """Генерирует случайную строку из заданного набора символов"""
    return ''.join(random.choice(char_pool) for _ in range(length))

def generate_related_strings(n: int, m: int, pattern: str = None) -> tuple[str, str]:
    """
    Генерирует связанные строки s и t, где t может содержать повторяющиеся паттерны
    """
    if pattern is None:
        pattern = generate_random_string(random.randint(2, 5))
    
    # Создаем строку s
    s_parts = []
    remaining_n = n
    while remaining_n > 0:
        part_len = min(len(pattern), remaining_n)
        s_parts.append(pattern[:part_len])
        remaining_n -= part_len
    s = ''.join(s_parts)[:n]
    
    # Создаем строку t с повторениями паттерна
    t_parts = []
    remaining_m = m
    k = random.randint(2, 5)  # Количество повторений паттерна
    while remaining_m > 0:
        if random.random() < 0.7:  # 70% chance to add pattern
            part_len = min(len(pattern) * k, remaining_m)
            repetitions = part_len // len(pattern)
            t_parts.append(pattern * repetitions)
            remaining_m -= repetitions * len(pattern)
        else:
            # Добавляем случайную часть
            part_len = min(random.randint(1, 10), remaining_m)
            t_parts.append(generate_random_string(part_len))
            remaining_m -= part_len
    
    t = ''.join(t_parts)[:m]
    return s, t

# Тестовые случаи
test_cases = [
    # Тест 1: Пример из условия
    {
        'input': (4, 8, "abcd", "abcbcbcd"),
        'expected': 1
    },
    
    # Тест 2: Второй пример из условия
    {
        'input': (3, 5, "aaa", "aaaaa"),
        'expected': 5
    },
    
    # Тест 3: Третий пример из условия
    {
        'input': (12, 16, "abbababacaab", "abbababababacaab"),
        'expected': 8
    },
    
    # Тест 4: Простой тест с одинаковыми символами
    {
        'input': (2, 4, "aa", "aaaa"),
        'expected': 3  # (x="", y="a", z=""), (x="a", y="a", z=""), (x="", y="aa", z="")
    },
    
    # Тест 5: Тест без совпадений
    {
        'input': (3, 5, "abc", "xyzpq"),
        'expected': 0
    },
    
    # Тест 6: Производительный тест - средний размер
    {
        'input': (1000, 2000, *generate_related_strings(1000, 2000, "abc")),
        'expected': None  # Проверяем только что не падает
    },
    
    # Тест 7: Производительный тест - большие строки
    {
        'input': (10**4, 2*10**4, *generate_related_strings(10**4, 2*10**4, "test")),
        'expected': None
    },
    
    # Тест 8: Производительный тест - очень большие строки
    {
        'input': (10**5, 2*10**5, *generate_related_strings(10**5, 2*10**5, "pattern")),
        'expected': None
    },
    
]

def run_solution_test():
    """Запускает тестирование solution функции"""
    
    def wrapper_func(n: int, m: int, s_str: str, t_str: str):
        """Обертка для совместимости с universal_test_solution"""
        return solution(n, m, s_str, t_str)
    
    # Запускаем тестирование
    results = universal_test_solution(
        wrapper_func,
        test_cases,
        show_input_preview=1,  # Показываем только первые элементы из-за больших строк
        show_output_preview=1,
        include_memory=True,
        include_time=True,
        verbose=True,
        copy_to_clipboard=True
    )
    
    print(f"\n📊 ИТОГИ ТЕСТИРОВАНИЯ:")
    print(f"Всего тестов: {results['total_tests']}")
    print(f"Пройдено: {results['passed_tests']}")
    print(f"Не пройдено: {results['failed_tests']}") 
    print(f"Ошибок: {results['errors']}")
    print(f"Общее время: {results['total_time']:.2f} мс")
    print(f"Максимальная память: {results['max_memory']:.2f} МБ")
    
    # Проверяем производительность
    max_time_ms = 2000  # 2 секунды ограничение
    max_memory_mb = 1024  # 1 ГБ ограничение
    
    performance_ok = True
    if results['total_time'] > max_time_ms * len(test_cases):
        print(f"⚠ ВНИМАНИЕ: Общее время выполнения превышает ожидаемое")
        performance_ok = False
    
    if results['max_memory'] > max_memory_mb:
        print(f"⚠ ВНИМАНИЕ: Использование памяти превышает {max_memory_mb} МБ")
        performance_ok = False
    
    if performance_ok:
        print("✅ Производительность в пределах ограничений")
    
    return results

# Дополнительная функция для проверки корректности на маленьких тестах
def verify_small_tests():
    """Проверяет корректность на маленьких ручных тестах"""
    print("\n🔍 ПРОВЕРКА КОРРЕКТНОСТИ НА МАЛЕНЬКИХ ТЕСТАХ:")
    
    small_tests = [
        # (n, m, s, t, expected, description)
        (1, 2, "a", "aa", 1, "Простой случай с одним символом"),
        (2, 4, "ab", "abab", 2, "Повторяющийся паттерн длины 2"),
        (3, 6, "abc", "abcabc", 3, "Повторяющийся паттерн длины 3"),
        (2, 3, "ab", "aba", 0, "Некорректное разбиение"),
    ]
    
    for n, m, s, t, expected, desc in small_tests:
        result = solution(n, m, s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} {desc}: n={n}, m={m}, expected={expected}, got={result}")

if __name__ == "__main__":
    verify_small_tests()
    run_solution_test()