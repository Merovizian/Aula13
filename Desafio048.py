print(f"\033[1;1m{'Desafio 048 - Somatoria de impares entre intervalo':*^70}\033[;m")
intervalo = input("Informe o intervalo(MIN/MAX): ")
soma = 0
if intervalo.find('/') != -1:
    intervalo_min = int(intervalo[:intervalo.find('/')])
    intervalo_max = int(intervalo[(intervalo.find('/')+1):])
    if intervalo_min < intervalo_max:
        multiplos = int(input("Informe qual multiplo quer: "))
        for c in range(intervalo_min, intervalo_max):
            if c % 2 == 1 and c % multiplos == 0:
                soma += c
        print(soma)