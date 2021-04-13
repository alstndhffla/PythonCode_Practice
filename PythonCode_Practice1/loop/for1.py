# 정수 1개를 입력받아 1부터 입력받은 수까지 각각 제곱을 구해 프린트

num = int(input('number: '))

for i in range(1, num+1):
    print(i, i*i)