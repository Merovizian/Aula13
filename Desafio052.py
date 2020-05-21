'''print(f"\033[;1m{'Desafio 053 - Numero Primo':*^70}\033[m")
numero = int(input("Infome um número: "))
aux = 0
for c in range(1,numero):
    if numero % c == 0:
        aux += 1
if aux < 2 and numero != 1 and numero != 2:
    print(f"O número {numero} é Primo")
else:
    print(f"O número {numero} não é Primo")
'''
numero = int(input("Infome um número: "))
aux = 0

for d in range(1,numero+1):
    for c in range(1,d+1):
        if d % c == 0:
            aux += 1
    if aux == 2:
        print(c)
        aux += 0
    aux = 0