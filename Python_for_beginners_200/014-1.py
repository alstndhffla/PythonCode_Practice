x = 1
total = 0
while 1:    # 무한루프
    total = total + x
    if total > 100000:  # total 100000 넘아가면 끝남(break)
        print(x)
        print(total)
        break
    x = x + 1
