import time
import tracemalloc
import pyperclip
from typing import Callable, Any, List, Dict

def universal_test_solution(
    solution_func: Callable,
    test_cases: List[Dict[str, Any]],
    *,
    show_input_preview: int = 5,
    show_output_preview: int = 5,
    include_memory: bool = True,
    include_time: bool = True,
    verbose: bool = False,
    copy_to_clipboard: bool = True
) -> Dict[str, Any]:
    """
    Универсальная функция для тестирования solution функций с копированием в буфер обмена
    """
    
    results = {
        'total_tests': len(test_cases),
        'passed_tests': 0,
        'failed_tests': 0,
        'errors': 0,
        'test_details': [],
        'total_time': 0,
        'max_memory': 0
    }
    
    # Собираем всю таблицу в одну строку
    table_lines = []
    
    # Заголовки таблицы
    headers = ["№", "Входные данные", "Результат", "Корректность"]
    if include_time:
        headers.append("Время(мс)")
    if include_memory:
        headers.append("Память(Мб)")
    
    table_lines.append("\t".join(headers))
    
    for i, test_case in enumerate(test_cases, 1):
        test_result = {
            'test_number': i,
            'input_data': test_case.get('input', test_case),
            'expected': test_case.get('expected'),
            'actual': None,
            'correctness': '?',
            'execution_time': 0,
            'memory_used': 0,
            'error': None
        }
        
        # Подготовка параметров для функции
        if 'input' in test_case:
            func_params = test_case['input']
        else:
            func_params = {k: v for k, v in test_case.items() if k != 'expected'}
        
        # Измерение производительности
        if include_memory:
            tracemalloc.start()
        
        start_time = time.time() if include_time else 0
        
        try:
            # Вызов тестируемой функции
            if isinstance(func_params, (list, tuple)):
                result = solution_func(*func_params)
                # Форматируем preview для списка/кортежа
                if len(func_params) > show_input_preview:
                    input_preview = str(func_params[:show_input_preview]) + "..."
                else:
                    input_preview = str(func_params)
            elif isinstance(func_params, dict):
                result = solution_func(**func_params)
                # Форматируем preview для словаря
                preview_dict = {}
                for key, value in func_params.items():
                    if isinstance(value, list) and len(value) > show_input_preview:
                        preview_dict[key] = value[:show_input_preview]
                    else:
                        preview_dict[key] = value
                input_preview = str(preview_dict)
                if len(str(func_params)) > 50:  # Если данные большие, добавляем многоточие
                    input_preview = input_preview[:-1][:200] + ", ...}" if input_preview.endswith("}") else input_preview[:200] + "..."
            else:
                result = solution_func(func_params)
                # Форматируем preview для одиночного значения
                input_preview = str(func_params)
                if len(input_preview) > 50:
                    input_preview = input_preview[:50] + "..."
            
            if include_time:
                test_result['execution_time'] = (time.time() - start_time) * 1000
                results['total_time'] += test_result['execution_time']
            
            if include_memory:
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                test_result['memory_used'] = peak / 1024 / 1024
                results['max_memory'] = max(results['max_memory'], test_result['memory_used'])
            
            test_result['actual'] = result
            
            # Проверка корректности
            expected = test_case.get('expected')
            if expected is not None:
                if result == expected:
                    test_result['correctness'] = '✓'
                    results['passed_tests'] += 1
                else:
                    test_result['correctness'] = '✗'
                    results['failed_tests'] += 1
            else:
                test_result['correctness'] = '?'
                results['passed_tests'] += 1
            
            # Форматирование вывода
            if isinstance(result, list):
                if len(result) > show_output_preview:
                    result_preview = str(result[:show_output_preview])[:200] + "..."
                else:
                    result_preview = str(result)[:200]
            else:
                result_preview = str(result)[:200]
            
            # Формируем строку таблицы
            row = [f"{i}", input_preview, result_preview[:200], test_result['correctness']]
            if include_time:
                row.append(f"{test_result['execution_time']:.2f}")
            if include_memory:
                row.append(f"{test_result['memory_used']:.2f}")
            
            table_lines.append("\t".join([i[:100] for i in row]))
            
        except Exception as e:
            if include_memory:
                tracemalloc.stop()
            if include_time:
                test_result['execution_time'] = (time.time() - start_time) * 1000
            
            test_result['error'] = str(e)
            test_result['correctness'] = 'ERROR'
            results['errors'] += 1
            
            # Форматируем input_preview для случая с ошибкой
            if isinstance(func_params, (list, tuple)):
                if len(func_params) > show_input_preview:
                    input_preview = str(func_params[:show_input_preview]) + "..."
                else:
                    input_preview = str(func_params)
            elif isinstance(func_params, dict):
                preview_dict = {}
                for key, value in func_params.items():
                    if isinstance(value, list) and len(value) > show_input_preview:
                        preview_dict[key] = value[:show_input_preview]
                    else:
                        preview_dict[key] = value
                input_preview = str(preview_dict)
            else:
                input_preview = str(func_params)
                if len(input_preview) > 50:
                    input_preview = input_preview[:50] + "..."
            
            row = [f"{i}", input_preview, f"Ошибка: {str(e)[:20]}", "ERROR"]
            if include_time:
                row.append(f"{test_result['execution_time']:.2f}")
            if include_memory:
                row.append("-")
            
            table_lines.append("\t".join([i[:100] for i in row]))
        
        results['test_details'].append(test_result)
    
    # Объединяем все строки
    final_table = "\n".join(table_lines)
    
    # Выводим в консоль
    print(final_table)
    
    # Копируем в буфер обмена
    if copy_to_clipboard:
        try:
            pyperclip.copy(final_table)
            print(f"\n✅ Таблица скопирована в буфер обмена! ({len(final_table)} символов)")
        except Exception as e:
            print(f"\n⚠ Не удалось скопировать в буфер обмена: {e}")
            print("Скопируйте таблицу выше вручную")
    
    return results