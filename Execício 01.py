#-------------
#UFRJ
#IM
#TMAA-2019.1
#GUSTAVO MACIEL
#-------------

print('Calculadora de Equação do 2o grau')
print(' ')
print('Equação da forma ax^2 + bx + c')

a= float(input('Qual é o coeficiente a?'))
b= float(input('Qual é o coeficiente b?'))
c= float(input('qual é o coeficiente c?'))

if a==0 : print('NÃO É UMA EQUAÇÃO DO 2o GRAU') 
if a!=0 : print('De fato é uma equação do 2o grau')

delta= b * b - (4* a * c)
print('O delta vale',delta)
if delta==0 : print('A equação tem raízes reais e iguas')
if delta<0 : print(' Não tem raízes reais') 
if delta>0 : print(' A equação tem duas raízes reais e distintas')

x1= (-b + delta**(1/2))/ (2 * a)
x2= (-b - delta**(1/2))/ (2 * a)


print(' uma raiz é',x1)
print(' a outra raiz é',x2)                   
                   
                   
