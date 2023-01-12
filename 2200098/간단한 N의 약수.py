import sys
sys.stdin = open('input_N의 약수.txt', 'r')

N = int(input())
list_N = []
for n in range(1,N+1) :
    if N % n == 0 :
        list_N.append(n)
print(*list_N)