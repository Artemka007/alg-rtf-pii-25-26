from timeit import timeit
from memory_profiler import memory_usage, profile
from time import sleep


def test_func(solution, tests):
    print(
      f'''N.;Input;Output;Time;Memory\r'''
    )
    for i in range(len(tests)):
        result = solution(len(tests[i]), tests[i])
        memory_used_mb = memory_usage(-1, interval=0.3, timeout=3)[0]


        time = timeit(lambda: solution(len(tests[i]), tests[i]), number=100)
        result_str = ' '.join([str(i) for i in result]) if len(result) < 15 else ' '.join([str(i) for i in result[0:15]]) + '...'
        test_data = ' '.join([str(i) for i in tests[i]]) if len(result) < 15 else ' '.join([str(i) for i in tests[i][0:15]]) + '...'
        print(
            f'''{i+1}.;{test_data};{result_str};{time:.8f};{memory_used_mb:.8f}\r'''
        )
    