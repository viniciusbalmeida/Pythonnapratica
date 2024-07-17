
print('========Desafio 33========')

def encontrar_maior_numero():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    num3 = float(input('Digite o terceiro número: '))

    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3

    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    print(f'O maior número é: {maior}')
    print('O menor número é:{} '.format(menor))

encontrar_maior_numero()













