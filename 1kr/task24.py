from typing import TypeVar
import io
import sys

T = TypeVar('T')

class MinQueue[T]:
    def __init__(self):
        self.min_queue = []
        self.main_queue = []

    def push(self, item: T):
        self.main_queue.append(item)
        while self.min_queue and self.min_queue[-1] > item:
            self.min_queue.pop()
        self.min_queue.append(item)
    
    def pop(self):
        value = self.main_queue.pop(0)
        if value == self.min_queue[0]:
            self.min_queue.pop(0)
        return value
    
    def min(self):
        return self.min_queue[0]
    
    def empty(self):
        return len(self.main_queue) == 0

def run_large_test():
    """Тест со 106 командами с выводом только для операций '?'"""
    commands = []
    outputs = []
    
    # Генерируем 106 команд
    # Паттерн: добавляем числа, иногда запрашиваем минимум, иногда удаляем
    
    # Первая часть: добавляем числа от 1 до 50 в разном порядке
    numbers_to_add = [i for i in range(1, 51)]
    import random
    random.shuffle(numbers_to_add)
    
    for num in numbers_to_add:
        commands.append(f"+ {num}")
    
    # Добавляем запросы минимума
    for i in range(10):
        commands.append("?")
    
    # Удаляем некоторые элементы
    for i in range(20):
        commands.append("-")
    
    # Добавляем больше запросов
    for i in range(10):
        commands.append("?")
    
    # Добавляем новые числа (от 51 до 80)
    new_numbers = [i for i in range(51, 81)]
    random.shuffle(new_numbers)
    
    for num in new_numbers:
        commands.append(f"+ {num}")
    
    # Еще запросы
    for i in range(10):
        commands.append("?")
    
    # Удаляем больше элементов
    for i in range(30):
        commands.append("-")
    
    # Финальные запросы
    for i in range(6):
        commands.append("?")
    
    # Общее количество команд должно быть 106
    total_commands = len(commands)
    if total_commands < 106:
        # Добавляем недостающие команды
        for i in range(106 - total_commands):
            commands.append("?")
    
    # Запускаем выполнение
    queue = MinQueue()
    
    print("КОМАНДЫ И ВЫВОД:")
    print("=" * 30)
    
    for i, cmd in enumerate(commands, 1):
        if cmd.startswith('+'):
            n = int(cmd[1:].strip())
            queue.push(n)
            print(f"{i:3d}. {cmd}")
        
        elif cmd == '-':
            if not queue.empty():
                queue.pop()
                print(f"{i:3d}. {cmd}")
            else:
                print(f"{i:3d}. {cmd} -> Очередь пуста")
        
        elif cmd == '?':
            if not queue.empty():
                min_val = queue.min()
                print(f"{i:3d}. {cmd} -> {min_val}")
            else:
                print(f"{i:3d}. {cmd} -> Очередь пуста")

# Альтернативный вариант с более интересной последовательностью
def run_structured_test():
    """Структурированный тест с понятным паттерном"""
    commands = []
    
    # Этап 1: Добавляем числа в убывающем порядке
    for i in range(20, 0, -1):
        commands.append(f"+ {i}")
    
    # Запросы минимума (должен быть 1)
    for i in range(5):
        commands.append("?")
    
    # Удаляем первые 10 элементов
    for i in range(10):
        commands.append("-")
    
    # Запросы минимума (должен быть 11)
    for i in range(5):
        commands.append("?")
    
    # Добавляем числа меньше текущего минимума
    for i in range(5, 0, -1):
        commands.append(f"+ {i}")
    
    # Запросы минимума (должен быть 1)
    for i in range(5):
        commands.append("?")
    
    # Удаляем до пустой очереди
    for i in range(15):
        commands.append("-")
    
    # Запросы к пустой очереди
    for i in range(5):
        commands.append("?")
    
    # Добавляем новые числа
    for i in range(30, 10, -1):
        commands.append(f"+ {i}")
    
    # Финальные запросы
    for i in range(10):
        commands.append("?")
    
    # Удаляем некоторые
    for i in range(15):
        commands.append("-")
    
    # Последние запросы
    for i in range(6):
        commands.append("?")
    
    # Обрезаем или дополняем до 106 команд
    commands = commands[:106] if len(commands) > 106 else commands + ["?"] * (106 - len(commands))
    
    # Выполняем
    queue = MinQueue()
    
    print("СТРУКТУРИРОВАННЫЙ ТЕСТ (106 команд):")
    print("=" * 40)
    
    for i, cmd in enumerate(commands, 1):
        if cmd.startswith('+'):
            n = int(cmd[1:].strip())
            queue.push(n)
            print(f"{i:3d}. {cmd}")
        
        elif cmd == '-':
            if not queue.empty():
                popped = queue.pop()
                print(f"{i:3d}. {cmd} (удален {popped})")
            else:
                print(f"{i:3d}. {cmd} -> Очередь пуста")
        
        elif cmd == '?':
            if not queue.empty():
                min_val = queue.min()
                print(f"{i:3d}. {cmd} -> {min_val}")
            else:
                print(f"{i:3d}. {cmd} -> Очередь пуста")

if __name__ == "__main__":
    # Выберите один из тестов:
    
    print("ТЕСТ 1: Случайная последовательность")
    run_large_test()
    
    print("\n" + "="*50 + "\n")
    
    print("ТЕСТ 2: Структурированная последовательность")
    run_structured_test()