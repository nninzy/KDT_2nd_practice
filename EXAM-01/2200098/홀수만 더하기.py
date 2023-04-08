import sys
sys.stdin = open('input_홀수만.txt', 'r')

T = int(input())
for t in range(1, T+1) :
    numbers = list(map(int, input().split()))
    result = 0
    test_num = '#' + str(t)
    for n in numbers :
        if n % 2 == 1 :
            result += n
    print(test_num, result)