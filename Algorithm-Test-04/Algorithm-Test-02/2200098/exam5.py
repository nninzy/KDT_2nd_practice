# 소득 불균형

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    earn_list = list(map(int, input().split()))
    aver = sum(earn_list)//N
    cnt = 0
    for value in earn_list :
        if value <= aver : cnt += 1
    print('#' + str(t), cnt)

# 메모리 (63048KB), 실행시간(258ms), 코드길이(245B)