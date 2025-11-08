from lib import quick_sort


def solution(input):
    M1 = []
    M2 = []

    splited_input = input.split(' ')
    i = 0

    while splited_input[i] != '0':
        M1.append(splited_input[i])
        i += 1

    i += 1

    while splited_input[i] != '0':
        M2.append(splited_input[i])
        i += 1
    
    quick_sort.quick_sort(M1)
    quick_sort.quick_sort(M2)

    j = 0
    k = 0
    result = []

    while j < len(M1) and k < len(M2):
        if M1[j] == M2[k]:
            k += 1
            j += 1
            continue
        
        if M1[j] > M2[k]:
            result.append(M2[k])
            k += 1
            continue
        
        if M1[j] < M2[k]:
            result.append(M1[j])
            j += 1
            continue

    while j < len(M1):
        result.append(M1[j])
        j += 1
        

    while k < len(M2):
        result.append(M2[k])
        k += 1
    
        
    return result


print(solution('1 2 6 8 7 3 0 4 1 6 2 3 9 0'))