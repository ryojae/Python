def solution(chicken):
    answer = 0
    chicken_coupon = chicken
    while chicken_coupon >= 10:
        answer += chicken_coupon // 10
        chicken_coupon = chicken_coupon % 10 + chicken_coupon // 10
    return answer
