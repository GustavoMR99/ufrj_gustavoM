#---------------
#UFRJ
#
#IM
#
#TMAA-2019.1
#
#GUSTAVO MACIEL
#---------------

print('Calculadora da soma dos dígitos de n elevado a m')

n = int(input('Digite um valor para n: '))
m = int(input('Digite um valor para m: '))


x= n ** m


soma = 0

while (x != 0):
    resto = x % 10
    x = (x - resto)//10
    soma = soma + resto
print('a soma dos dígitos vale: ')
print(soma)
