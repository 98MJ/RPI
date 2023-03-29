n = int(input(print("인원수를 입력하세요")))
s = int(input(print("피자 한판당 원하는 조각 개수를 입력하세요")))
p = 1


for i in range (n):
    if (((s*p) / n) < 1):
        p = p + 1       
        
print(p,"판 시키면 됩니다.")