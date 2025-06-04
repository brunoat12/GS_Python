#GS
#Criação da varíavel de quantidade de desastres
n_desastres = int(input('Digite a quantidade desastres: '))

#Criação das variáveis das listas, inicialmente vazias
tipo = []
pais = []
cidade = []
bairro = []
rua = []
quantidade_pessoas = []
criancas = []
adultos = []
idosos = []
mob_reduz = []
feridos = []

#Criação de um laço de repitação, que irá pedir as informações para a quantidade de desastres informados
for c in range(0,n_desastres):
    #Já estou solicitando as informações e colocando nas listas
    tipo.append(input('Digite o tipo de desastres: '))
    pais.append(input('Digite o país: '))
    cidade.append(input('Digite a cidade: '))
    bairro.append(input('Digite o bairro: '))
    rua.append(input('Digite a rua: '))
    #Laço de repetição usando while True, que irá rodar enquanto a condição do if for verdadeira, quando for falso vai sair do while
    while True:
        quantidade_pessoas_veri = int(input('Digite a quantidade de pessoas afetadas: '))
        criancas_veri = int(input('Digite a quantidade de crianças: '))
        adultos_veri = int(input('Digite a quantidade de adultos: '))
        idosos_veri = int(input('Digite a quantidade de idosos: '))
        mob_reduz_veri = int(input('Digite a quantidade de pessoas com mobilidade reduzida: '))
        feridos_veri = int(input('Digite a quantidade de feridos: '))
        #Condição que verifica se a quantidad de pessoas é diferente da a soma de todas as categorias,
        # se for verdadeiro, vai pedir para digitar essas informações novamente
        #Se for falso, ele adiciona as informações nas listas e sai do while
        if quantidade_pessoas_veri != criancas_veri+adultos_veri+idosos_veri+mob_reduz_veri+feridos_veri:
            print('Erro! A soma das categorias é maior que a quantidade de pessoas. Digite novamente!')
        else:
            quantidade_pessoas.append(quantidade_pessoas_veri)
            criancas.append(criancas_veri)
            adultos.append(adultos_veri)
            idosos.append(idosos_veri)
            mob_reduz.append(mob_reduz_veri)
            feridos.append(feridos_veri)
            break

print()
#Printando a quantidade de desastres registrados
print(f'Foram registrados {n_desastres} desastres!')
total_pes = sum(quantidade_pessoas)
#Criando um dicinário que irá facilitar na hora de puxar a categoria mais afetada
categorias = {
    'Criança': sum(criancas),
    'Adultos': sum(adultos),
    'Idosos': sum(idosos),
    'Mobilidade reduzida': sum(mob_reduz),
    'Feridos': sum(feridos)
}

print()
#printando a quantidade de afetados por categoria
print(f'O Total de crianças afetadas: {sum(criancas)}.\nTotal de adultos afetados: {sum(adultos)}.\nTotal de idosos afetados: {sum(idosos)}.\nTotal de pessoas com mobilidade reduzida: {sum(mob_reduz)}.\nTotal de feridos: {sum(feridos)}')
print()
#printando a categoria mais afetada
print(f'A categoria mais afetada foi a de {max(categorias, key=categorias.get)}')

#pegando o indice do local mais afetado
local_mais_afetado = max(quantidade_pessoas)
indice_afetado = quantidade_pessoas.index(local_mais_afetado)
print()
#printado o tipo de desastre com mais afetados
print(f'Tipo de desastre com mais afetados: {tipo[indice_afetado]}')
print()
#printando o endereço completo do local mais afetado
print(f'O local mais afetado: {rua[indice_afetado]}, {bairro[indice_afetado]}, {cidade[indice_afetado]}, {pais[indice_afetado]}')