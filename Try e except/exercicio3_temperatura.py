temp = input('Digite a temperatura atual:')


while True:
    print('Opções:')
    print('1-Celsius para fahrenheit')
    print('2-Celsius para kelvin')
    print('3-Sair')

    opcao = input('Digite a opção que você deseja:')
    if opcao == '1':
        try:
            temp = int(temp)
            print(f'{temp}°C em fahrenheit é: {(temp * 9/5) + 32}')
        except:
            print('Digite a temperatura novamente!')
    elif opcao == '2':
        try:
            temp = int(temp)
            print(f'{temp}°C em kelvin é: {temp + 273.15}')
        except:
            print('Coloque números inteiros!')
    elif opcao == '3':
        print('Saindo do programa...')
        break
    else:
        print('Digite em números, por favor!')