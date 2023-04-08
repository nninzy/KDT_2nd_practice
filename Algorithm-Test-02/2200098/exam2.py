# 신용카드 만들기 1

t = int(input())
for num in range(1, t+1) :
    num_list = list(map(int, input().split()))
    total = 0
    for i in range(len(num_list)) :
        if i % 2 == 0 : total += (num_list[i] * 2)
        else : total += num_list[i]
    print('#' + str(num), (10 - (total % 10)) % 10)

# 메모리 (58264KB), 실행시간(151ms), 코드길이(279B)