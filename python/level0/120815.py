n = int(input(print("인원수를 입력하세요")))
p = 1


for i in range (n):
    if (((6*p) % n)!=0):
        p = p + 1       
        
print(p,"판 시키면 됩니다.")