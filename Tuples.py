n = int(input())

integers = tuple(map(int, input().split()))

t = integers

print(hash(t))
