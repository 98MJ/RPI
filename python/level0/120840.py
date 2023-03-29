# 문제 설명
# 머쓱이는 구슬을 친구들에게 나누어주려고 합니다. 구슬은 모두 다르게 생겼습니다. 
# 머쓱이가 갖고 있는 구슬의 개수 balls와 친구들에게 나누어 줄 구슬 개수 share이 매개변수로 주어질 때, 
# balls개의 구슬 중 share개의 구슬을 고르는 가능한 모든 경우의 수를 return 하는 solution 함수를 완성해주세요.

# Combination

def Comnination (balls, share):
    count = balls - share
    sum1 = sum2 = 1
    
    for i in range (count+1):
        sum1 = sum1 * balls
        balls = balls - 1
        
    for j in range (share):
        sum2 = sum2 * share
        share = share - 1
    
    answer = sum1 / sum2
    return answer
    # return sum1, sum2

print(Comnination(5,3))