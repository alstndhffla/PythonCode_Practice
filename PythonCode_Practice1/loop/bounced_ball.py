# 고무 공을 100미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다
# 원래 높이의 3/5 만큼 튀어오른다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산한다.
# 소수 넷째자리까지 계산하라.
# round 함수는 반올림해준다. 지정 자리에서

d = 100
i = 1
while i <= 10:
    d *= (3/5)
    print(i, round(d, 4))
    i += 1
