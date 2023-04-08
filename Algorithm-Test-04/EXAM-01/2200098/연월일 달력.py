import sys
sys.stdin = open('input_연월일.txt', 'r')

T = int(input())
# day_dict 만들기
day_dict = {}
up_31 = [1,3,5,7,8,10,12]
up_30 = [4,6,9,11]
up_28 = [2]
for i in range(1,13) :
    if i in up_31 :
        day_dict[i] = range(1,32)
    elif i in up_30 :
        day_dict[i] = range(1,31)
    else :
        day_dict[i] = range(1,29)

for t in range(1,T+1) :
    test_num = '#' + str(t)
    date = input() #'YYYYMMDD'
    if len(date) == 8 :
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        if int(month) in range(1,13) :
            if int(day) in day_dict[int(month)] :
                print(test_num, year + '/' + month + '/' + day)
            else :
                print(test_num, -1)
        else :
            print(test_num, -1)
    else :
        print(test_num, -1)