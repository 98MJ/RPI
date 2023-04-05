def solution (num):

    divisor = []
    # num = int(input(print("숫자를 입력하세요")))

    for i in range(1, num+1):
        if (num % i == 0):
            divisor.append(i)

    sum_div = sum(divisor)

    return sum_div

print(solution(15))