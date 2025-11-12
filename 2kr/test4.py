# Стресс-тест для проверки производительности
from task4 import solution
from test_func import universal_test_solution


def generate_stress_test():
    """Генерирует тест на максимальных ограничениях"""
    N = 1000
    items = []
    
    # Генерируем 1000 уникальных строк длиной до 1000 символов
    import random
    import string
    
    # Базовые короткие строки для составных слов
    base_strings = [''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 5))) 
                   for _ in range(200)]
    
    # Добавляем составные слова
    for i in range(800):
        if i % 3 == 0:  # Каждое третье слово - составное
            s1 = random.choice(base_strings)
            s2 = random.choice(base_strings)
            items.append(s1 + s2)
        else:
            items.append(''.join(random.choices(string.ascii_uppercase, 
                              k=random.randint(1, 20))))
    
    # Убираем дубликаты и берем первые N
    unique_items = list(set(items))[:N]
    
    return {
        'input': [N, unique_items],
        'expected': None  # Результат не проверяем, только производительность
    }


print("🚀 Запуск тестов с стресс-тестом...")# Тестовые случаи
test_cases = [
    # Тест 1: Пример из условия
    {
        'input': [5, ["A", "AB", "B", "AA", "ABC"]],
        'expected': ["AA", "AB"]
    },
    
    # Тест 2: Второй пример из условия
    {
        'input': [10, [
            "ABC", "DEFG", "AB", "ABCAB", "DEFGA", 
            "FG", "ABFG", "ABCAFG", "FGFG", "ABABC"
        ]],
        'expected': ["ABCAB", "ABFG", "FGFG"]
    },
    
    # Тест 3: Нет составных слов
    {
        'input': [4, ["CAT", "DOG", "BIRD", "FISH"]],
        'expected': []
    },
    
    # Тест 4: Все слова составные
    {
        'input': [3, ["AB", "A", "B"]],
        'expected': ["AB"]
    },
    
    # Тест 5: Многоуровневые составные слова
    {
        'input': [6, ["A", "B", "C", "AB", "BC", "ABC"]],
        'expected': ["AB", "ABC"]
    },
    
    # Тест 6: Слова разной длины
    {
        'input': [5, ["X", "Y", "Z", "XY", "XYZ"]],
        'expected': ["XY", "XYZ"]
    },
    
    # Тест 7: Минимальный случай
    {
        'input': [4, ["A", "B", "AA", "AB"]],
        'expected': ["AA", "AB"]
    },
    
    # Тест 8: Слова с одинаковыми префиксами
    {
        'input': [5, ["A", "AB", "ABC", "ABCD", "BCD"]],
        'expected': ["AB", "ABC", "ABCD"]
    },
    
    # Тест 9: Большие строки (в пределах ограничений)
    {
        'input': [4, ["LONGSTRING", "SHORT", "LONG", "LONGSHORT"]],
        'expected': ["LONGSHORT"]
    },
    
    # Тест 10: Слова которые можно составить разными способами
    {
        'input': [6, ["A", "B", "C", "AB", "BC", "AC", "ABC"]],
        'expected': ["AB", "AC", "BC", "ABC"]
    },
    generate_stress_test()
]

# Запуск тестов
if __name__ == "__main__":
    results = universal_test_solution(
        solution_func=solution,
        test_cases=test_cases,
        show_input_preview=3,  # Показывать первые 3 элемента в preview
        show_output_preview=5, # Показывать первые 5 элементов вывода
        include_memory=True,
        include_time=True,
        verbose=True,
        copy_to_clipboard=True
    )
    
    # Дополнительная статистика
    print(f"\n📊 Итоговая статистика:")
    print(f"Всего тестов: {results['total_tests']}")
    print(f"Пройдено: {results['passed_tests']}")
    print(f"Не пройдено: {results['failed_tests']}")
    print(f"Ошибок: {results['errors']}")
    
    if results['total_time'] > 0:
        print(f"Общее время: {results['total_time']:.2f} мс")
        print(f"Среднее время: {results['total_time']/results['total_tests']:.2f} мс")
    
    if results['max_memory'] > 0:
        print(f"Максимальная память: {results['max_memory']:.2f} МБ")