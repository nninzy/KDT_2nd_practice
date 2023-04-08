# 신용카드 만들기 2

T = int(input())
first_num = [3, 4, 5, 6, 9]
for t in range(1, T+1) :
    num_str = input().replace('-', '')
    is_use = True if len(num_str) == 16 and int(num_str[0]) in first_num else False
    print('#' + str(t), int(is_use))

# 메모리 (58800KB), 실행시간(153ms), 코드길이(279B)
