a = 0
b = 0
for b in range(10):
    n = int(input())
    if n % 2 == 0:
        a += n
    else:
        b += n
print(a)
print(b)