a = int(input("Digite um número: "))

b = 0  

for i in range(1, a + 1):
    if a % i == 0:   
        b += 1    

if b == 2:   
    print(f"{a} é primo")
else:
    print(f"{a} não é primo")
