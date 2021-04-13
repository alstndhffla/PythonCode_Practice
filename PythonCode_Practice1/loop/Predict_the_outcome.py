number = 358

rem = rev = 0

while number >= 1:
    rem = number % 10
    print(rem)
    rev = rev * 10 + rem
    print(rev)
    number = number // 10

print(rev)