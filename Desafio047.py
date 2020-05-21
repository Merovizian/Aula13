import time

print(f"\033[;1m{'Desafio 047 - Numeros pares em um intervalo':*^70}\033[;m")
menu = 10
for c in range(0,menu):
    if menu != -1:
        intervalo = input("\033[;mInforme o intervalo(MIN/MAX): ")
    if (intervalo.find('/') == -1):
        print("\033[1;31mError! Informe um intervalo correto!")
        time.sleep(0)
    elif menu != -1:
        intervalo_min = int(intervalo[0:(intervalo.find('/'))])
        intervalo_max = int(intervalo[(intervalo.find('/') + 1):])
        if intervalo_min > intervalo_max:
            print("\033[1;31mError! Informe um intervalo correto!")
            time.sleep(0)
        else:
            aberto = (input("Intervalo fechado? (S/N): "))
            menu = -1
            print(f"Os números pares entre {intervalo_min} e {intervalo_max} são: ",end='')
            if aberto == 'S':
                for a in range(intervalo_min, intervalo_max):
                    if a % 2 == 0:
                        print(a, end=',')
                if (a+1) % 2 ==0:
                    print(a+1)
            else:
                for a in range(intervalo_min+1, intervalo_max):
                    if a % 2 == 0:
                        print(a, end=',')

