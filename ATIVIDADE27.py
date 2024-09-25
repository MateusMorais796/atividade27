# Solicite ao usuário que insira o nome de até 7 convidados.
# Armazene os nomes em uma lista.
# Permita ao usuário remover um convidado da lista, caso necessário.
# Exiba a lista final de convidados.

# Digite o nome do convidado 1: João
# Digite o nome do convidado 2: Maria
# ...
# Digite o nome do convidado 7: Pedro
# Deseja remover algum convidado da lista? (sim/não): sim
# Digite o nome do convidado a ser removido: Maria

convidados = []
for n in range(0, 7):
    convidados.append(str(input("Digite o nome do convidado ")))

print(f'sua lita de convidados: {convidados}' )

remover = str(input('Deseja remover algum convidado da lista? (sim/não) '))

if remover == 'sim':
    convidados.remove(input('Digite o nome do convidado que deeja remover '))
else:
    print('o nome digitado não foi encontrado na lista.')

print(convidados)