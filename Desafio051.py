print(f"\033[;1m{'Desafio 051 - Progressão aritmética':*^70}\033[m")
primeiro_termo = int(input("Informe o primeiro termo da progressão: "))
razao = int(input("Informe a razão da progressão: "))
termos = int(input("Informe a quantidade de termos: "))
for c in range(primeiro_termo, termos, 1):
    if c == primeiro_termo:
        print(c,end=',')
    print((primeiro_termo+(razao*c)),end='')
    if c < termos-1:
        print(',',end='')
