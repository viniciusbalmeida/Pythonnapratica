from random import randint
from time
print('========Desafio 28========')

computador = randint(0, 5)#Onde o computador vai "PENSAR"
print('-=-' * 20 )
print('Vou pensar em um número entre 0 e 5. Tente adivinhar! ;)')
print('-=-' * 20)

jogador = int(input('Em qual número eu pensei agora?: '))

if computador == jogador:
    print('Parabéns você acertou!')
else:
    print(f'Errou! Na verdade eu pensei no número {computador} e não no {jogador}')








#def pensar_numero():
    #return random.randint(0, 5) #Faz o comutador "Pensar"

#numero_pensado = pensar_numero()

#print('Pensei em um número entre 0 e 5. Consegue adivinhar qual é?')



#palpite = None

#while palpite!= numero_pensado:
    #palpite = int(input('digite seu palpite: '))

    #if palpite == numero_pensado:
        #print(f'Parabéns! Você adivinhou o número {numero_pensado}.')
    #else:
        #print('Tente novamente!')







