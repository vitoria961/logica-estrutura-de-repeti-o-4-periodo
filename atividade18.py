opcao = ""  

while opcao != "3": 
    print("MENU :")
    print("1 - Somar dois números")
    print("2 - Subtrair dois números")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"O resultado da soma é: {n1 + n2}")

    elif opcao == "2":
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"O resultado da subtração é: {n1 - n2}")

    elif opcao == "3":
        print("Saindo do programa...")

    else:
        print("Opção inválida! Escolha novamente.")
