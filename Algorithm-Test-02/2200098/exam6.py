T = int(input())
for t in range(1, T + 1) :
    num_list = list(map(int, input().split()))
    answer = num_list[2] if num_list[0] == num_list[1] else sum(num_list) - (num_list[2] * 2)
    print('#' + str(t), answer)

# 메모리 (63032KB), 실행시간(375ms), 코드길이(216B)