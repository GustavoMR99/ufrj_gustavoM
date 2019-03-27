#-------------------
#UFRJ
#
#IM
#
#TMAA-2019.1
#
#GUSTAVO MACIEL
#-------------------
print('calculadora dos n primeiros múltiplos de 5 e 7')

n = int(input('qual valor de n: '))

for x in range(0,n*35):
    if x % 35 == 0:
        print(x)
    else:
        print('')
