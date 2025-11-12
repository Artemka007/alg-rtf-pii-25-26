from io import StringIO
import os
import sys
import time
import tracemalloc

from test_func import universal_test_solution


def run_database_solution(inp_file):
    """Запускает решение базы данных с заданными входными данными"""
    # Сохраняем оригинальный stdin и stdout
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    
    try:
        # Очищаем предыдущие данные
        if os.path.exists('db_buckets'):
            import shutil
            shutil.rmtree('db_buckets')
        
        # Перенаправляем ввод
        sys.stdin = open(inp_file, 'r')
        
        # Перехватываем вывод
        output_capture = StringIO()
        sys.stdout = output_capture
        
        # Запускаем решение
        from task13_ext import solution  # Импортируем ваше решение
        solution()
        
        # Получаем результат
        result = output_capture.getvalue().strip()
        return result
        
    finally:
        # Восстанавливаем оригинальные потоки
        sys.stdin = original_stdin
        sys.stdout = original_stdout

def plain_test():
    """Тестирование на конкретных примерах"""
    print("\n📋 ТЕСТИРОВАНИЕ НА ПРИМЕРАХ")
    print("=" * 80)
    
    # Тест 1
    test_cases = [
        {
            "name": "Тест 1 (10 команд)",
            "input": """10
ADD JW SJXO
ADD RZBR YMW
ADD ADX LVT
ADD LKFLG UWM
PRINT ADX
UPDATE HNTP JQPVG
PRINT QURWB
DELETE MB
PRINT ADX
DELETE ADX""",
            "expected": """ADX LVT
ERROR
ERROR
ADX LVT
ERROR"""
        },
        {
            "name": "Тест 2 (15 команд)",
            "input": """15
ADD RWJSN JFTF
ADD ZDH GOON
ADD FCDS TCAY
ADD FCDS TCAY
ADD HMGVI BWK
ADD JTDU TLWWN
ADD IXRJ ERF
ADD IAOD GRDO
PRINT IXRJ
PRINT JTDU
PRINT IXRJ
UPDATE ZDH IOX
PRINT ZDH
ADD GVWU RTA
DELETE ZDH
ADD FCDS IVFJV""",
            "expected": """ERROR
IXRJ ERF
JTDU TLWWN
IXRJ ERF
ZDH IOX"""
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n🧪 {test['name']}")
        print(f"Входные данные:\n{test['input']}")
        print(f"Ожидаемый вывод:\n{test['expected']}")
        
        # Создаем временный файл с входными данными
        with open(f'test_input_{i}.txt', 'w') as f:
            f.write(test['input'])
        
        try:
            result = run_database_solution(f'test_input_{i}.txt')
            print(f"Полученный вывод:\n{result}")
            
            # Сравниваем результаты
            expected_lines = test['expected'].strip().split('\n') if test['expected'].strip() else []
            result_lines = result.strip().split('\n') if result.strip() else []
            
            if expected_lines == result_lines:
                print("✅ ТЕСТ ПРОЙДЕН")
            else:
                print("❌ ТЕСТ НЕ ПРОЙДЕН")
                print(f"Расхождения:")
                for j, (exp, res) in enumerate(zip(expected_lines, result_lines)):
                    if exp != res:
                        print(f"  Строка {j+1}: ожидалось '{exp}', получено '{res}'")
                
                # Если количество строк разное
                if len(expected_lines) != len(result_lines):
                    print(f"  Разное количество строк: ожидалось {len(expected_lines)}, получено {len(result_lines)}")
                    
        except Exception as e:
            print(f"❌ Ошибка при выполнении теста: {e}")
        
        finally:
            # Удаляем временный файл
            if os.path.exists(f'test_input_{i}.txt'):
                os.remove(f'test_input_{i}.txt')

def stress_test():
    """Стресс-тест для проверки производительности"""
    print("\n🔥 СТРЕСС-ТЕСТ")
    print("=" * 80)
    
    with open('inp.txt', 'w') as f:
        f.write('100000\n')
        # ADD команды (первые 50000)
        for i in range(50000):
            f.write(f"ADD key{i} value{i}\n")
        
        # PRINT команды (следующие 25000)
        for i in range(25000):
            f.write(f"PRINT key{i}\n")
        
        # UPDATE команды (следующие 12500)
        for i in range(12500):
            f.write(f"UPDATE key{i} newvalue{i}")
        
        # DELETE команды (последние 12500)
        for i in range(12500, 25000):
            f.write(f"DELETE key{i}\n")
    
    print("Запуск стресс-теста с 100000 команд...")
    
    start_time = time.time()
    tracemalloc.start()
    
    try:
        result = run_database_solution('inp.txt')
        execution_time = time.time() - start_time
        current, peak = tracemalloc.get_traced_memory()
        
        print(f"Время выполнения: {execution_time:.2f} сек")
        print(f"Пиковое использование памяти: {peak / 1024 / 1024:.2f} МБ")
            
    except Exception as e:
        print(f"❌ Ошибка в стресс-тесте: {e}")

if __name__ == "__main__":
    plain_test()