import sys
sys.stdin = open('input_서랍.txt', 'r')

P, K = list(map(int, input().split()))
result = P - K + 1
print(result)