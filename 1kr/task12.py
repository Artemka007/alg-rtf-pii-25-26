from typing import Tuple, TypeVar

from lib.quick_sort import custom_quick_sort
from test_func import universal_test_solution


T = TypeVar('T')
    

def comp_func(item: Tuple[str, int, int], pivot: Tuple[str, int, int]):
    if item[1] > pivot[1]:
        return True
    
    if item[1] == pivot[1] and item[2] < pivot[2]:
        return True
    
    if item[1] == pivot[1] and item[2] == pivot[2] and item[0].lower() < pivot[0].lower():
        return True
    
    return False


def solution(n: int, items: Tuple[str, int, int]):
    arr = list(items)
    custom_quick_sort(arr, comp_func, 0, n - 1)

    return arr

# ТЕСТОВЫЕ КЕЙСЫ ДЛЯ СОРТИРОВКИ
test_cases = [
    # Базовый тест из примера
    {
        'input': {
            'n': 5,
            'items': [
                ('alla', 4, 100),
                ('genna', 6, 1000), 
                ('gosha', 2, 90),
                ('rita', 2, 90),
                ('Timofey', 4, 80)
            ]
        },
        'expected': [
            ('genna', 6, 1000),    # 1 место: наибольшие баллы (6)
            ('alla', 4, 100),      # 2 место: баллы 4, штраф 100
            ('Timofey', 4, 80),    # 3 место: баллы 4, штраф 80 (меньше = лучше)
            ('gosha', 2, 90),      # 4 место: баллы 2
            ('rita', 2, 90)        # 5 место: баллы 2, лексикографически 'gosha' < 'rita'
        ]
    },
    
    # Все нули (проверка лексикографической сортировки)
    {
        'input': {
            'n': 5,
            'items': [
                ('alla', 0, 0),
                ('genna', 0, 0),
                ('gosha', 0, 0),
                ('rita', 0, 0),
                ('Timofey', 0, 0)
            ]
        },
        'expected': [
            ('alla', 0, 0),        # Лексикографически: 'alla' < 'genna' < 'gosha' < 'rita' < 'Timofey'
            ('genna', 0, 0),
            ('gosha', 0, 0), 
            ('rita', 0, 0),
            ('Timofey', 0, 0)
        ]
    },
    
    # Одинаковые баллы, разные штрафы
    {
        'input': {
            'n': 4,
            'items': [
                ('alice', 5, 50),
                ('bob', 5, 30),
                ('charlie', 5, 70),
                ('diana', 5, 10)
            ]
        },
        'expected': [
            ('diana', 5, 10),      # Наименьший штраф
            ('bob', 5, 30),
            ('alice', 5, 50), 
            ('charlie', 5, 70)     # Наибольший штраф
        ]
    },
    
    # Одинаковые баллы и штрафы, разные имена
    {
        'input': {
            'n': 4,
            'items': [
                ('zeta', 3, 100),
                ('alpha', 3, 100),
                ('gamma', 3, 100),
                ('beta', 3, 100)
            ]
        },
        'expected': [
            ('alpha', 3, 100),     # Лексикографически: 'alpha' < 'beta' < 'gamma' < 'zeta'
            ('beta', 3, 100),
            ('gamma', 3, 100),
            ('zeta', 3, 100)
        ]
    },
    
    # Смешанный случай
    {
        'input': {
            'n': 6,
            'items': [
                ('ivan', 10, 5),
                ('petr', 10, 5),
                ('sidor', 8, 2),
                ('oleg', 8, 8),
                ('anna', 12, 15),
                ('maria', 12, 10)
            ]
        },
        'expected': [
            ('anna', 12, 15),      # Наибольшие баллы (12), но больший штраф
            ('maria', 12, 10),     # Наибольшие баллы (12), меньший штраф
            ('ivan', 10, 5),       # Баллы 10, лексикографически 'ivan' < 'petr'
            ('petr', 10, 5),       # Баллы 10
            ('sidor', 8, 2),       # Баллы 8, меньший штраф
            ('oleg', 8, 8)         # Баллы 8, больший штраф
        ]
    },
    
    # Граничный случай - один элемент
    {
        'input': {
            'n': 1,
            'items': [('single', 100, 50)]
        },
        'expected': [('single', 100, 50)]
    },
    
    # Граничный случай - пустой список
    {
        'input': {
            'n': 0,
            'items': []
        },
        'expected': []
    },
    
    # Проверка регистра (case-insensitive)
    {
        'input': {
            'n': 4,
            'items': [
                ('Alpha', 5, 10),
                ('alpha', 5, 10),
                ('BETA', 5, 10),
                ('beta', 5, 10)
            ]
        },
        'expected': [
            ('Alpha', 5, 10),      # 'Alpha' и 'alpha' считаются одинаковыми? 
            ('alpha', 5, 10),      # зависит от реализации .lower()
            ('BETA', 5, 10),
            ('beta', 5, 10)
        ]
    },
    
    # Большие числа
    {
        'input': {
            'n': 3,
            'items': [
                ('max', 1000000, 999999),
                ('min', 1, 1),
                ('mid', 500000, 500000)
            ]
        },
        'expected': [
            ('max', 1000000, 999999),
            ('mid', 500000, 500000),
            ('min', 1, 1)
        ]
    },
    
    # Отрицательные значения (если допустимы по условию)
    {
        'input': {
            'n': 3,
            'items': [
                ('first', -5, -10),
                ('second', -5, -5),
                ('third', -10, -1)
            ]
        },
        'expected': [
            ('second', -5, -5),    # -5 > -10, меньший штраф (-5 > -10)
            ('first', -5, -10),    # -5 > -10, больший штраф
            ('third', -10, -1)     # наименьшие баллы
        ]
    },
    {
        'input': {
            'n': 1000,
            'items': [('student' + str(i), i % 100, i % 50) for i in range(1000)]
        },
        'expected': None  # Проверяем только что не падает
    },
    {
        'input': {
            'n': 500,
            'items': [('test', 50, 25)] * 500  # Все элементы одинаковые
        },
        'expected': [('test', 50, 25)] * 500
    }
]

if __name__ == "__main__":
    universal_test_solution(
        solution, 
        test_cases,
        show_input_preview=2,
        show_output_preview=3
    )
    