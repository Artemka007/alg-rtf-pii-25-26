def solution(N: int, M: int) -> str:
    if N == 0:
        return "0"
    
    sign = ""
    if (N < 0) != (M < 0):
        sign = "-"
    N, M = abs(N), abs(M)
    
    integer_part = N // M
    remainder = N % M
    
    if remainder == 0:
        return sign + str(integer_part)
    
    result = []
    remainders = {}
    position = 0
    
    while remainder != 0:
        if remainder in remainders:
            non_repeating = result[:remainders[remainder]]
            repeating = result[remainders[remainder]:]
            
            if integer_part == 0:
                return sign + "0." + "".join(non_repeating) + "(" + "".join(repeating) + ")"
            else:
                return sign + str(integer_part) + "." + "".join(non_repeating) + "(" + "".join(repeating) + ")"
        
        remainders[remainder] = position
        
        remainder *= 10
        digit = remainder // M
        result.append(str(digit))
        remainder %= M
        position += 1
    
    if integer_part == 0:
        return sign + "0." + "".join(result)
    else:
        return sign + str(integer_part) + "." + "".join(result)

def main():
    N, M = map(int, input().split())
    print(solution(N, M))

if __name__ == "__main__":
    main()