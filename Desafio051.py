print(f"\033[;1m{'Desafio 051 - Progressão aritmética':*^70}\033[m")
primeiro_termo = int(input("Informe o primeiro termo da progressão: "))
razao = int(input("Informe a razão da progressão: "))
termos = int(input("Informe a limite_cadastro de termos: "))
for c in range(primeiro_termo, (razao*termos+primeiro_termo), razao):
    if c == primeiro_termo:
        print(c,end=',')
    elif c < (razao*termos + primeiro_termo)-razao:
        print(c,end=',')
    ##    print(razao*termos+primeiro_termo)
    else:
        print(c)
