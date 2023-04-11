# imprime o identificador
print("Seja bem-vindo(a) a loja da EVELLYN REBEKA PEREIRA DA COSTA - RU 4206514")

# Define a função para cadastrar uma nova peça
def cadastrar_peca():
    global contador
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))
    peca = {"codigo": contador, "nome": nome, "fabricante": fabricante, "valor": valor}
    pecas.append(peca)
    contador += 1
    print("Peça cadastrada com sucesso!")


# Define a função para consultar uma peça pelo código
def consultar_peca_por_codigo():
    codigo = int(input("Digite o código da peça: "))
    for peca in pecas:
        if peca["codigo"] == codigo:
            print(f"Código: {peca['codigo']}")
            print(f"Nome: {peca['nome']}")
            print(f"Fabricante: {peca['fabricante']}")
            print(f"Valor: R$ {peca['valor']:.2f}")
            return
    print("Peça não encontrada.")


# Define a função para consultar peças por fabricante
def consultar_peca_por_fabricante():
    fabricante = input("Digite o nome do fabricante: ")
    encontrou = False
    for peca in pecas:
        if peca["fabricante"] == fabricante:
            encontrou = True
            print(f"Código: {peca['codigo']}")
            print(f"Nome: {peca['nome']}")
            print(f"Valor: R$ {peca['valor']:.2f}")
    if not encontrou:
        print("Nenhuma peça encontrada para esse fabricante.")


# Define a função para remover uma peça
def remover_peca():
    codigo = int(input("Digite o código da peça a ser removida: "))
    for i, peca in enumerate(pecas):
        if peca["codigo"] == codigo:
            del pecas[i]
            print("Peça removida com sucesso!")
            return
    print("Peça não encontrada.")

# Define a função para consultar todas as peças
def consulta_todas():
    if not pecas: # Verifica se a lista de peças está vazia
        print("Não há peças cadastradas.")
    else:
        print("Lista de peças cadastradas:")
        for peca in pecas:
            print("Código:", peca["codigo"])
            print("Nome:", peca["nome"])
            print("Fabricante:", peca["fabricante"])
            print("Valor:", peca["valor"])
            print("------------------------------")

# Define a função principal do programa
def main():
    global pecas, contador
    pecas = []  # Inicializa a lista de peças
    contador = 1  # Inicializa o contador de códigos exclusivos
    while True:
        # Exibe o menu principal
        print("\nMenu principal:")
        print("1 - Cadastrar peça")
        print("2 - Consultar peça por código")
        print("3 - Consultar peças por fabricante")
        print("4 - Consultar todas as pecas")
        print("5 - Remover peça")
        print("0 - Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            consultar_peca_por_codigo()
        elif opcao == "3":
            consultar_peca_por_fabricante()
        elif opcao == "4":
            consulta_todas()
        elif opcao == "5":
            remover_peca()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()