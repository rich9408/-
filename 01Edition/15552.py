import sys
input = sys.stdin.readline
x = int(input())

for i in range(x):
    n = input().split(' ')
    result = int(n[0]) + int(n[1])
    print(result)