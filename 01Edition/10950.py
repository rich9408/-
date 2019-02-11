import sys

x = int(sys.stdin.readline().rstrip())

for i in range(x):
    n = input().split(' ')
    result = int(n[0]) + int(n[1])
    print(result)