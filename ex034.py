
print('========Desafio 34========')

#Função para calcular aumento de salário

def calcular_aumento(salario):
    if salario > 1250:
        porcentagem_aumento = 10
    else:
        porcentagem_aumento = 15

    aumento = salario * (porcentagem_aumento / 100)
    novo_salario = salario + aumento
    return aumento, novo_salario

#Pergunta o salário do funcionário
salario = float(input('Digite o salário do funcionário: R$ '))

#Calcula o aumento
aumento, novo_salario = calcular_aumento(salario)

#exibir o resutado

print(f'O  aumento será de: R$ {aumento: .2f}')
print(f'O novo salário será de: R$ {novo_salario: .2f}')




















