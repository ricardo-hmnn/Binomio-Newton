from math import factorial

x, a = '',''
lista = []
n =  int(input("Expoente n do polinomio (x + a)^n: "))
for i in range(0,(n+1)):
    c = factorial(n) / (factorial(n-i) * factorial(i))
    #instrução para tirar x^0
    if (n-i) != 0:
        x = 'x^{} '.format(n-i)
    else :
        x = ''
    #instrução para tirar a^0
    if i != 0:
        a = 'a^{}'.format(i)
    
    z = str(int(c))
    #instrução para tirar o 1
    if z != '1':
        con = z + ' ' + x + a + ' '
    else:
        con = x + a + ' '
    lista.append(con)
    print(con)