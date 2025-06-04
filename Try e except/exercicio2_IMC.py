nome = input('Digite seu nome:')
altura = input('Digite sua altura:')
peso = input('Digite seu peso:')

try:
    altura = float(altura)
    peso = float(peso)
    print(f'O resultado do seu IMC é: {(peso/(altura ** 2))}')
except:
    print('Digite seu peso e altura novamente!')
