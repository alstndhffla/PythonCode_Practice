# 정수를 한개 입력받아 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성

n = int(input('정수입력:'))

i = 1
while i <= n:
    print(i, i*i)
    i += 1
