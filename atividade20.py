n = int(input())

a = 0  
b = 0   
c = 0   

maior = n
menor = n

while n != 0:
    a += 1
    b += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if n % 2 == 0:
        c += 1

    n = int(input())

print(a)
print(b / a)
print(maior)
print(menor)
print(c)
