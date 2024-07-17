
print('========Desafio 35========')

# Função para verificar se três lados podem formar um triângulo
def pode_formar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Ler os comprimentos dos três lados

lado1 = float(input('Digite o comprimento do primeiro lado: '))

lado2 = float(input('Digite o comprimento do segundo lado:  '))

lado3 = float( input('Digite o comprimento do terceiro lado: '))

# Verificar se podem formar um triângulo

if pode_formar_triangulo(lado1, lado2, lado3):
    print('As medidas {}, {}, {} podem formar um triângulo! '.format(lado1, lado2, lado3))
else:
    print('Essas medidas não podem formar um triângulo')

# Verificar se podem formar um triângulo






















