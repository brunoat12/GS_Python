n_desastres = int(input('Digite a quantidade desastres: '))

for c in range(0,n_desastres):
    tipo=input('Digite o tipo de desastres: ')
    pais=input('Digite o país: ')
    cidade = input('Digite a cidade: ')
    bairro = input('Digite o bairro: ')
    rua = input('Digite a rua: ')

    while True:
        quantidade_pessoas = int(input('Digite a quantidade de pessoas afetadas: '))
        criancas = int(input('Digite a quantidade de crianças: '))
        adultos = int(input('Digite a quantidade de adultos: '))
        idosos = int(input('Digite a quantidade de idosos: '))
        mob_reduz = int(input('Digite a quantidade de pessoas com mobilidade reduzida: '))
        feridos = int(input('Digite a quantidade de feridos: '))
        if quantidade_pessoas < criancas+adultos+idosos+mob_reduz+feridos:
            print('Erro! A soma das categorias é maior que a quantidade de pessoas. Digite novamente!')
        else:
            break
