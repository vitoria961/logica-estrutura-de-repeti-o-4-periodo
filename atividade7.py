soma = 0  

for a in range(1, 6):
    n = float(input(f"Digite a nota {a}: "))
    soma += n

media = soma / 5  
print(f"\nA média final é: {media}")
