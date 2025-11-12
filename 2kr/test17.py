import random
import string
from typing import List, Dict, Any

from task17 import heap_optimized_solution
from test_func import universal_test_solution

def generate_random_word(length: int = 5) -> str:
    """Генерирует случайное слово из маленьких латинских букв"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_document(num_words: int = 50) -> str:
    """Генерирует случайный документ"""
    words = [generate_random_word(random.randint(3, 8)) for _ in range(num_words)]
    return ' '.join(words)

def generate_query(words_pool: List[str], num_words: int = 5) -> str:
    """Генерирует случайный запрос из пуска слов"""
    query_words = random.choices(words_pool, k=num_words)
    return ' '.join(query_words)

# Тестовые случаи
test_cases = [
    # Тест 1: Пример из условия
    {
        'input': (3, 3, [
            "i love coffee",
            "coffee with milk and sugar", 
            "free tea for everyone",
            "i like black coffee without milk",
            "everyone loves new year",
            "mary likes black coffee without milk"
        ]),
        'expected': [['1', '2'], ['3'], ['2', '1']]
    },
    
    # Тест 2: Второй пример из условия
    {
        'input': (6, 1, [
            "buy flat in moscow",
            "rent flat in moscow", 
            "sell flat in moscow",
            "want flat in moscow like crazy",
            "clean flat in moscow on weekends",
            "renovate flat in moscow",
            "flat in moscow for crazy weekends"
        ]),
        'expected': [['4', '5', '1', '2', '3']]
    },
    
    # Тест 3: Простой тест с одним документом
    {
        'input': (1, 1, [
            "hello world",
            "hello"
        ]),
        'expected': [['1']]
    },
    
    # Тест 4: Тест с повторяющимися словами
    {
        'input': (2, 1, [
            "test test test",
            "test check test",
            "test test"
        ]),
        'expected': [['1', '2']]
    },
    
    # Тест 5: Производительный тест - 100 документов, 50 запросов
    {
        'input': (100, 50, [
            *[generate_document(20) for _ in range(100)],
            *[generate_query(["test", "hello", "world", "python", "code"], 3) for _ in range(50)]
        ]),
        'expected': None  # Проверяем только что не падает
    },
    
    # Тест 6: Производительный тест - 500 документов, 100 запросов  
    {
        'input': (500, 100, [
            *[generate_document(30) for _ in range(500)],
            *[generate_query([f"word{i}" for i in range(100)], 4) for _ in range(100)]
        ]),
        'expected': None
    },
    
    # Тест 7: Производительный тест - 1000 документов, 200 запросов
    {
        'input': (1000, 200, [
            *[generate_document(25) for _ in range(1000)],
            *[generate_query([f"term{i}" for i in range(200)], 5) for _ in range(200)]
        ]),
        'expected': None
    },
    
    # Тест 8: Тест с максимальным размером - 10000 документов, 1000 запросов
    {
        'input': (10000, 1000, [
            *[generate_document(10) for _ in range(10000)],
            *[generate_query([f"token{i}" for i in range(500)], 3) for _ in range(1000)]
        ]),
        'expected': None
    },
    
    # Тест 9: Тест с длинными документами
    {
        'input': (50, 10, [
            *[generate_document(100) for _ in range(50)],
            *[generate_query([f"longword{i}" for i in range(20)], 2) for _ in range(10)]
        ]),
        'expected': None
    },
    
    # Тест 10: Тест с короткими запросами
    {
        'input': (200, 50, [
            *[generate_document(15) for _ in range(200)],
            *[generate_query([f"short{i}" for i in range(50)], 1) for _ in range(50)]
        ]),
        'expected': None
    }
]

def run_heap_optimized_test():
    """Запускает тестирование heap_optimized_solution"""
    
    def wrapper_func(N: int, M: int, items: List[str]):
        """Обертка для совместимости с universal_test_solution"""
        result = list(heap_optimized_solution(N, M, items))
        return result
    
    # Запускаем тестирование
    results = universal_test_solution(
        wrapper_func,
        test_cases,
        show_input_preview=2,
        show_output_preview=3,
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
    
    return results

if __name__ == "__main__":
    run_heap_optimized_test()