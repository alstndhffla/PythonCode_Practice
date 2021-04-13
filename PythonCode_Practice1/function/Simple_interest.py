# 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때
# 이자를 구하는 함수 simple_interest()를 작성

def simple_interest(p, r, t):
    rate = p * r * t
    return rate


print(simple_interest(10000000, 0.03875, 5))


# 원금(p), 단리 이율(r), 기간(t)이 주어졌을 때
# 원리금을 계산하는 함수 simple_interest_amount()를 작성


def simple_interest_amount(p, r, t):
    m = p + simple_interest(p, r, t)
    return m


print(simple_interest_amount(1100000, 0.05, 5/12))