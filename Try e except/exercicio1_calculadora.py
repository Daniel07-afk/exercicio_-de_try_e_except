num1 = input("Digite a primeiro número:")
num2 = input("Digite o segundo número:")

while True:
    print('Opções:')
    print('1-Adição')
    print('2-Subtração')
    print('3-Multiplicação')
    print('4-Divisão')
    print('5-Sair')
    
    opcao = input("Digite a operação que deseja realizar:")
    if opcao == '1':
        try:
            num1 = float(num1)
            num2 = float(num2)
            print(f'A soma dos dois números são: {num1 + num2}')
        except:
            print('Digite o número correto!')
    elif opcao == '2':
        try:
            num1 = float(num1)
            num2 = float(num2)
            print(f'A subtração dos dois números são: {num1 - num2}')
        except:
            print('Digite o número exato!')
    elif opcao == '3':
        try:
            num1 = float(num1)
            num2 = float(num2)
            print(f'A multiplicação dessa conta é: {num1 * num2}')
        except:
            print('Digite números que você deseja!')
    elif opcao == '4':
        try:
            num1 = float(num1)
            num2 = float(num2)
            print(f'A divisão dessa conta é: {num1 / num2}')
        except:
            print('Digite o número correto!')
    elif opcao == '5':
        print('Saindo do programa...')
        break
    
    else:
        print('Opção invalida! Tente novamente')