# Тесты для функции распределения капиталов
from task2 import solution
from test_func import universal_test_solution


def test_solution():
    # Определяем тестируемую функцию
    def solution_wrapper(N, capitals):
        """Обертка для функции solution, принимающая параметры в нужном формате"""
        return solution(N, capitals)
    
    # Тестовые случаи
    test_cases = [
        # Базовые тесты
        {
            'input': (5, [1, 2, 3, 4, 5]),
            'expected': 0.33
        },
        {
            'input': (10, [2, 10, 100, 30, 7, 4, 15, 2, 15, 80]),
            'expected': 6.52
        },
        
        # Граничные значения
        {
            'input': (2, [1, 2]),
            'expected': 0.03
        },
        {
            'input': (2, [1000000, 1000000]),
            'expected': 20000.0
        },
        {
            'input': (3, [1, 1, 1]),
            'expected': 0.05
        },
        # Минимальные значения
        {
            'input': (2, [1, 1]),
            'expected': 0.02
        },
        {
            'input': (2, [1, 1000000]),
            'expected': 10000.01
        },
        
        # Максимальные значения (упрощенные для производительности)
        {
            'input': (100, [1000000] * 100),
            'expected': 990000.0  # Сумма всех комиссий
        },
        
        # Специальные случаи
        {
            'input': (4, [10, 20, 30, 40]),
            'expected': 1.0
        },
        {
            'input': (6, [1, 2, 3, 4, 5, 6]),
            'expected': 0.45
        },
        {
            'input': (3, [100, 200, 300]),
            'expected': 6.0
        },
        
        # Тест с одинаковыми значениями
        {
            'input': (5, [50, 50, 50, 50, 50]),
            'expected': 3.0
        },
        
        # Тест с возрастающей последовательностью
        {
            'input': (4, [10, 100, 1000, 10000]),
            'expected': 111.1
        },
        
        # Тест с убывающей последовательностью
        {
            'input': (4, [10000, 1000, 100, 10]),
            'expected': 111.1
        },
        # Абсолютные минимумы
        {
            'input': (2, [1, 1]),
            'expected': 0.02
        },
        {
            'input': (2, [1, 2]),
            'expected': 0.03
        },
        
        # Большие числа
        {
            'input': (3, [1000000, 1000000, 1000000]),
            'expected': 30000.0
        },
        # Большие числа
        {
            'input': (10**6, [i for i in range(10**5)]),
            'expected': None
        },
    ]
    
    # Запуск тестов
    results = universal_test_solution(
        solution_wrapper,
        test_cases,
        show_input_preview=3,
        show_output_preview=2,
        include_time=True,
        include_memory=True,
        verbose=True,
        copy_to_clipboard=True
    )
    
    # Дополнительная статистика
    print(f"\n📊 Статистика тестирования:")
    print(f"Всего тестов: {results['total_tests']}")
    print(f"Пройдено: {results['passed_tests']}")
    print(f"Не пройдено: {results['failed_tests']}")
    print(f"Ошибок: {results['errors']}")
    
    print(f"Общее время: {results['total_time']:.2f} мс")
    print(f"Среднее время: {results['total_time']/results['total_tests']:.2f} мс")
    
    print(f"Максимальная память: {results['max_memory']:.2f} Мб")
    
    return results

# Дополнительные тесты для проверки edge cases
def test_edge_cases():
    """Тесты граничных случаев"""
    
    def solution_wrapper(N, capitals):
        return solution(N, capitals)
    
    edge_test_cases = [
        # Абсолютные минимумы
        {
            'input': (2, [1, 1]),
            'expected': 0.02
        },
        {
            'input': (2, [1, 2]),
            'expected': 0.03
        },
        
        # Большие числа
        {
            'input': (3, [1000000, 1000000, 1000000]),
            'expected': 30000.0
        },
        
        # Тест с одним элементом (если функция должна обрабатывать)
        # {
        #     'input': (1, [100]),
        #     'expected': 0.0
        # },
        
        # Тест с повторяющимися значениями
        {
            'input': (4, [5, 5, 10, 10]),
            'expected': 0.35
        }
    ]
    
    print("\n🧪 Тестирование граничных случаев:")
    results = universal_test_solution(
        solution_wrapper,
        edge_test_cases,
        show_input_preview=2,
        show_output_preview=2,
        include_time=True,
        include_memory=False,
        verbose=True,
        copy_to_clipboard=False
    )
    
    return results

# Запуск тестов
if __name__ == "__main__":
    main_results = test_solution()