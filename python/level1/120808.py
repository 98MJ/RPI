#첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
#두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom = numer = 0
    if (denom1 > denom2):
        ma = denom1
    else:
        ma = denom2
        
    for i in range(ma, (denom1*denom2) + 1):
        if i % denom1 == 0 and i % denom2 == 0:
            denom = i
    numer = (denom / denom1) * numer1 + (denom / denom2) * numer2
    
    lesat = 1
    
    if (denom > numer):
        mi = numer
    else:
        mi = denom
    
    for j in range(mi, 1, -1):
        if denom % j == 0 and numer % j == 0:
            least = j       
            numer = numer / least
            denom = denom / least
    
    
    answer.append(numer)
    answer.append(denom)
    
    return answer

print(solution(9,2,1,3))
print(solution(231,415,123,4))