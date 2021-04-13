x = 0
while x < 10:
    x = x+1     # 1, 2 까지는 출력하지 않음.
    if x < 3:
        continue    # continue 타면 그 아래는 아예 실행하지 않는다. 다시 while 문 초반으로 돌아감
    print(x)    # 8까지만 출력함.
    if x > 7:
        break
