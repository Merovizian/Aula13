print(f"\033[;1m{'Desafio 056 - Nome idade e sexo':*^70}\033[m")
masculino_database = ('m','M','Masculino','MASCULINO')
masculino_have = 0
feminino_have = 0
feminino_database = ('f','F','Feminino','FEMININO')
quantidade = int(input("Quantas pessoas cadastrar: "))
media = 0
homem_velho = 0
homem_velho_aux = 0
mulher_menos20 = 0
mulher_aux = 0


for c in range(0, quantidade):
    usuario_nome = input(f"Qual o nome do usuário {c+1}: ")
    usuario_sexo = input(f"Qual o sexo do usuário {c+1}: ")

    for d in range(0, 4):
        if usuario_sexo == masculino_database[d]:
            masculino_have += 1
        if usuario_sexo == feminino_database[d]:
            feminino_have += 1

    if masculino_have == 0 and feminino_have == 0:
        print("\033[1;31mVocê informou um sexo incorreto!\033[;m")
        usuario_sexo = input(f"Tente novamente. Qual o Sexo do Usuário {c + 1}: ")
        for d in range(0, 4):
            if usuario_sexo == masculino_database[d]:
                masculino_have += 1
            if usuario_sexo == feminino_database[d]:
                feminino_have += 1

    if masculino_have >= 1:
        masculino_have = 0
        usuario_idade = int(input(f"Qual a idade do usuário {c+1}: "))
        media += usuario_idade
        if usuario_idade > homem_velho:
           homem_velho = usuario_idade
           homem_velho_aux = usuario_nome

    if feminino_have >= 1:
       feminino_have = 0
       usuario_idade = int(input(f"Qual a idade do usuário {c+1}: "))
       media += usuario_idade
       mulher_aux = 1
       if usuario_idade < 20:
           mulher_menos20 += 1

print('\n')
print(f"A média de idade do grupo é: {media/quantidade}")
if homem_velho != 0:
    print(f"O homem mais velho é o usuário {homem_velho_aux} com {homem_velho} anos")
else:
    print("\033[1;33mNão há lista_homens no grupo!\033[m")
if mulher_aux == 1 and mulher_menos20 != 0:
    print(f"No grupo existem {mulher_menos20} Mulher(es) com menos de 20 anos.")
else:
    print("\033[1;33mNão há lista_mulheres com menos de 20 anos no grupo!")