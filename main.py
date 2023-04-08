print('Bem vindo a lanchonete do Vinicius Alfonso')
print('*'* 10 + 'CARDAPIO' + '*' * 10)

# tabela de preços dos produtos
produtos = {
    '100': {'nome': 'Cachorro-Quente', 'preco': 9.00},
    '101': {'nome': 'Cachorro-Quente Duplo', 'preco': 11.00},
    '102': {'nome': 'X-Egg', 'preco': 12.00},
    '103': {'nome': 'X-Salada', 'preco': 13.00},
    '104': {'nome': 'X-Bacon', 'preco': 14.00},
    '105': {'nome': 'X-Tudo', 'preco': 17.00},
    '200': {'nome': 'Refrigerante Lata', 'preco': 5.00},
    '201': {'nome': 'Chá Gelado', 'preco': 4.00},
}

# variáveis iniciais
total = 0
pedido = []

# exibe o menu
for codigo, produto in produtos.items():
    print(f'{codigo} - {produto["nome"]} (R$ {produto["preco"]:.2f})')

# laço principal
while True:
    # lê a opção do usuário
    opcao = input('Entre com o código desejado: ')

    # verifica se a opção é válida
    if opcao not in produtos:
        print('Opção inválida.')
        continue

    # adiciona o produto ao pedido e atualiza o total
    produto = produtos[opcao]
    pedido.append(produto)
    total += produto['preco']

    print('Você pediu um', produtos[opcao]['nome'], 'no valor de', produtos[opcao]['preco'], 'reais')

    # pergunta se o usuário deseja fazer outro pedido
    opcao = input('Deseja pedir mais alguma coisa? (0-Não/1-Sim) ')
    if opcao.upper() == '0':
        break
    elif opcao.upper() == '1':
        continue
    else:
        print('Opção inválida.')
        continue

# exibe o pedido e o total

print(f'O total a ser pago é: R$ {total:.2f}')