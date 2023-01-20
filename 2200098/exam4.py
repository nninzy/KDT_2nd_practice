# 문자열의 거울상

alp_dict = {'b' : 'd', 'd' : 'b', 'p' : 'q', 'q' : 'p'}
T = int(input())
for t in range(1, T+1) :
    t_num = '#' + str(t)
    text = input()
    answer = ''
    for i in range(len(text)-1, -1, -1) :
        answer += alp_dict[text[i]]
    print(t_num, answer)

# 메모리 (61976KB), 실행시간(195ms), 코드길이(260B)