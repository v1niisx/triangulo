#Sistema verfica se um numero informado é impar ou par
print('\n\t\t --- verficar num, impar ou par --- \n\t\t')
#entrada
vr = int(input('Digite um numero: '))

if (vr % 2) == 0:
    print('Parabéns, o número é par!')
else:
    print('O número é impar :(')

