from test_func import universal_test_solution


def solution(n: int, m: int):
    if m == 0:
        return 1
    
    if m == 1:
        return n
    
    res = 0

    for i in range(1, n + 1):
        ocuppied_places_count = (m - 1) * i + 1

        if ocuppied_places_count > n:
            break
        
        res += n - ocuppied_places_count + 1

    return res

test_cases = [
    {'input': {'n': 4, 'm': 2}, 'expected': 6},
    {'input': {'n': 4, 'm': 3}, 'expected': 2},
    {'input': {'n': 5, 'm': 3}, 'expected': 4},
    {'input': {'n': 6, 'm': 3}, 'expected': 7},
    {'input': {'n': 1000, 'm': 999}, 'expected': 2},
]

if __name__ == "__main__":
    universal_test_solution(solution, test_cases,
        show_input_preview=3,
        show_output_preview=1)
    