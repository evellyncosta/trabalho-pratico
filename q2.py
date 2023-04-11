# imprime o identificador
print("Seja bem-vindo(a) a lanchonete da EVELLYN REBEKA PEREIRA DA COSTA - RU 4206514")

# cria um dicionario para armazenar as informacoes dos produtos
cardapio = {
    100: {"descricao": "Cachorro-Quente", "valor": 9.0},
    101: {"descricao": "Cachorro-Quente Duplo", "valor": 11.0},
    102: {"descricao": "X-Egg", "valor": 12.0},
    103: {"descricao": "X-Salada", "valor": 13.0},
    104: {"descricao": "X-Bacon", "valor": 14.0},
    105: {"descricao": "X-Tudo", "valor": 17.0},
    200: {"descricao": "Refrigerante Lata", "valor": 5.0},
    201: {"descricao": "Chá Gelado", "valor": 4.0},
}

# inicializa o pedido
pedido_total = 0.0

# o loop é usado para que o cliente faça vários pedidos. Até que o cliente responda que não irá fazer mais pedidos, continua em loop
while True:
    # le o codigo do produto
    codigo = input("Digite o código do produto desejado: ")

    # testa se o codigo eh um numero
    if codigo.isnumeric():
        # converte para inteiro
        codigo = int(codigo)
        # verifica se está no cardapio
        if codigo in cardapio:
            # se estiver no cardapio, soma
            produto = cardapio[codigo]
            pedido_total += produto["valor"]
            print(f"Produto: {produto['descricao']} - Valor: R$ {produto['valor']:.2f}")
        else:
            # se não estiver no cardapio, mostra opcao invalida
            print("Opção inválida!")
            continue
    else:
        # se o codigo nao for um numero, opcao invalida
        print("Opção inválida!")
        continue

    # permite que o cliente peça mais alguma coisa
    continuar = input("Deseja pedir mais alguma coisa? (S/N) ")
    if continuar.lower() == "n":
        # caso a resposta seja N, mostra o valor total do pedido e interrompe
        print(f"Valor total do pedido: R$ {pedido_total:.2f}")
        break
    elif continuar.lower() != "s":
        # se a resposta não for S ou N, mostra opção inválida e interrompe
        print("Opção inválida!")
        break