import sys
sys.stdin = open('input_불면증.txt', 'r')

T = int(input())
for t in range(1,T+1) :
    N = int(input())
    result = []
    rp = 0
    test_num = '#' + str(t)
    while len(result) != 10 :
        rp += 1
        for num in str(rp * N) :
            result.append(int(num))
            result_no_ovl = list(set(result))
            result = result_no_ovl
    print(test_num, rp * N)