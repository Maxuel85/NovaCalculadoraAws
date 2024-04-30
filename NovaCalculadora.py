def calculadora():
    while True:
        print("\nCalculadora - Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        try:
            opcao = int(input("Digite o número da operação desejada: "))

            if opcao == 0:
                print("Encerrando a calculadora. Até logo!")
                break
            elif opcao in [1, 2, 3, 4]:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))

                if opcao == 1:
                    resultado = num1 + num2
                elif opcao == 2:
                    resultado = num1 - num2
                elif opcao == 3:
                    resultado = num1 * num2
                elif opcao == 4:
                    if num2 != 0:
                        resultado = num1 / num2
                    else:
                        print("Erro: Divisão por zero. Resultado: 0")
                        continue

                print(f"Resultado: {resultado}")
            else:
                print("Essa opção não existe. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

calculadora()
