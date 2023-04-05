#  1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

def solution (num):
    prime = []
# num = int(input(print("숫자를 입력하세요")))

    for i in range (2, num+1):
        n =0
        for j in range(1,i+1):
            if i%j == 0:
                n+=1
        if n==2:
            prime.append(i)    
    return len(prime)


print(solution(8))

