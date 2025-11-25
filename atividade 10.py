n1 = int(input("Digite o 1º número: "))
menor = n1
maior = n1

for a in range(9):
    k = int(input("Digite um numero: "))

    if k < menor:
        menor = k
    if k > maior:
        maior = k

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
