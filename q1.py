
# imprime o identificador
print("Seja bem-vindo(a) a loja da EVELLYN REBEKA PEREIRA DA COSTA - RU 4206514")

# le o valor unitario do produto
valor_unitario = float(input("Digite o valor unitário do produto: "))
#le a quantidade de produto
quantidade = int(input("Digite a quantidade desejada: "))

#obtem o valor total sem desconto
valor_sem_desconto = valor_unitario * quantidade
#inicializa o desconto
valor_com_desconto = 0

# se a quantidade esta entre 10 e 99, obtem-se 5% de desconto por un
if quantidade >= 10 and quantidade <= 99:
    valor_com_desconto = valor_unitario * quantidade * 0.95
# se a quantidade esta entre 100 e 999, obtem-se 10% de desconto por un
elif quantidade >= 100 and quantidade <= 999:
    valor_com_desconto = valor_unitario * quantidade * 0.9
# se a quantidade for maior ou igual a 1000, obtem-se 15% de desconto por un
elif quantidade >= 1000:
    valor_com_desconto = valor_unitario * quantidade * 0.85
else:
# para valores sem desconto
    valor_com_desconto = valor_unitario * quantidade

print("Valor total sem desconto: R$ {:.2f}".format(valor_sem_desconto))
print("Valor total com desconto: R$ {:.2f}".format(valor_com_desconto))
