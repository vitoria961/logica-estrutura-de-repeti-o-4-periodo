import random  

numero_secreto = random.randint(1, 20)

print("Estou pensando em um número entre 1 e 20. Tente adivinhar!")

acertou = False

while not acertou:
    palpite = int(input("Digite seu palpite: "))

    if palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou. O número era {numero_secreto}.")
        acertou = True
