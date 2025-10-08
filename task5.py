from memory_profiler import memory_usage, profile

@profile
def solution(num1: str, operand: str, num2: str):
    num1_is_negative = num1.startswith('-')
    num2_is_negative = num2.startswith('-')

    num1 = num1.replace('-', '')
    num2 = num2.replace('-', '')

    min_length_num = num2 if len(num1) >= len(num2) else num1
    max_length_num = num1 if len(num1) >= len(num2) else num2
    dp = 0
    result = ''

    for i in range(len(min_length_num)):
        current_num1_index = len(num1) - i - 1
        current_num2_index = len(num2) - i - 1

        temp = int(num1[current_num1_index]) + int(num2[current_num2_index])
        result = str((temp + dp) % 10) + result

        if temp + dp >= 10:
            dp = (temp + dp) // 10
        else:
            dp = 0

    for i in range(len(max_length_num) - len(min_length_num) - 1, -1, -1):
        temp = int(max_length_num[i])
        result = str((temp + dp) % 10) + result

        if temp + dp >= 10:
            dp = (temp + dp) // 10
        else:
            dp = 0
    
    if dp != 0:
        result = str(dp) + result

    
    return eval('9'*1000 + '+' + '9'*1000)

print(solution('9'*1000, '+', '9'*1000), eval('9'*1000 + '+' + '9'*1000))

