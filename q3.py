# imprime o identificador
print("Seja bem-vindo(a) a companhia de logistica da EVELLYN REBEKA PEREIRA DA COSTA - RU 4206514")

# Função para obter as dimensões do objeto
def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            if altura <= 0 or largura <= 0 or comprimento <= 0:
                print("Erro: as dimensões devem ser maiores que zero.")
                continue
            volume = altura * comprimento * largura
            if volume < 1000:
                return 10
            elif volume < 10000:
                return 20
            elif volume < 30000:
                return 30
            elif volume < 100000:
                return 50
            else:
                print("As dimensões do objeto ultrapassaram o limite aceito (100000 cm³). Tente novamente.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

# Função para obter o peso do objeto
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))
            if peso <= 0:
                print("Erro: o peso deve ser maior que zero.")
                continue
            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            else:
                print("O peso do objeto ultrapassou o limite aceito (30 kg). Tente novamente.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

# Função para obter a rota do objeto
def rotaObjeto():
    rotas = {
        "RS": 1,
        "SR": 1,
        "BS": 1.2,
        "SB": 1.2,
        "BR": 1.5,
        "RB": 1.5
    }
    while True:
        rota = input("Digite a rota do objeto (ex: RS para Rio de Janeiro - São Paulo): ").upper()
        if rota in rotas:
            return rotas[rota]
        else:
            print("Rota inválida. Tente novamente.")

# Obtendo as informações do objeto
print("Informe as informações do objeto:")
valor_dimensoes = dimensoesObjeto()
valor_peso = pesoObjeto()
valor_rota = rotaObjeto()

# Calculando o valor total a ser pago
valor_total = valor_dimensoes * valor_peso * valor_rota
print(f"Valor total a ser pago: R$ {valor_total:.2f}")