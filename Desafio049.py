print(f"\033[;1m{'Desafio 049 -Tabuada entre dois numeros':*^70}\033[;m")
coeficiente = int(input("Informe o operando: "))
operando = int(input("Tabuada até qual operador: "))
print(f"Tabaada do numero: {coeficiente}")
for c in range(0, operando):
    print(f"{coeficiente}*{c}={c*coeficiente}")