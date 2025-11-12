from task12 import solution
from test_func import universal_test_solution


test_cases = [
    # 2 теста из условия
    {'input': 'aabaabaabaabaa', 'expected': 24, 'description': 'Пример 1 из условия'},
    {'input': 'abcab', 'expected': 5, 'description': 'Пример 2 из условия'},
    
    # 8 тестов на максимальные значения
    {'input': 'abcde' * 20, 'expected': None, 'description': '100 символов с паттерном длины 5'},
    {'input': 'abcde' * 200, 'expected': None, 'description': '1000 символов с паттерном длины 5'},
    {'input': 'a' * 1000, 'expected': None, 'description': '1000 символов с паттерном длины 5'},
    {'input': 'ab' * 500, 'expected': None, 'description': '1000 символов с паттерном длины 5'},
]

# Запуск тестов
if __name__ == "__main__":
    print("🧪 10 ТЕСТОВ: 2 из условия + 8 на максимальные значения")
    print("=" * 80)
    
    results = universal_test_solution(
        solution,
        test_cases,
        show_input_preview=3,
        show_output_preview=5,
        include_memory=True,
        include_time=True,
        copy_to_clipboard=True
    )