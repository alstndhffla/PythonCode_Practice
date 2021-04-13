scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)
    if x < 3:
        continue
    else:
        break

# 1, 2, 3까지 출력됨. 왜? if 문이 print 문 아래에 나왔기 때문이지
# test
# test1
