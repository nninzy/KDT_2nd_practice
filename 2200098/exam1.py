# 최빈수 구하기 문제
t = int(input())
for _ in range(t) :
    t_case = '#' + input()
    cnt_dict = {}
    num_list = list(map(int, input().split()))
    for num in num_list :
        cnt_dict[num] = (cnt_dict[num] + 1 if num in cnt_dict.keys() else 1)
    max_cnt = max(cnt_dict.values())
    max_list = []
    for key, value in cnt_dict.items() :
        if value == max_cnt : max_list.append(key)
    print(t_case, sorted(max_list)[-1])

# 메모리 (60448KB), 실행시간(173ms), 코드길이(418B)