#3) Faça um programa no qual o usuário precisa cadastrar as informações de dois produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total das compras.

print("Cadastro do Produto 1:")
cod1 = input("Digite o código do produto: ")
nome1 = input("Digite o nome do produto: ")
qtd1 = int(input("Digite a quantidade do produto: "))
preco1 = float(input("Digite o preço do produto: "))


print("\nCadastro do Produto 2:")
cod2 = input("Digite o código do produto: ")
nome2 = input("Digite o nome do produto: ")
qtd2 = int(input("Digite a quantidade do produto: "))
preco2 = float(input("Digite o preço do produto: "))


total1 = qtd1 * preco1
total2 = qtd2 * preco2
valor_total = total1 + total2


print("\n----------------------------")
print("Produto 1:")
print(f"CÓDIGO: {cod1}")
print(f"NOME: {nome1}")
print(f"QUANTIDADE: {qtd1}")
print(f"PREÇO UNITÁRIO: R$ {preco1}")
print(f"TOTAL: R$ {total1}")
print("----------------------------")

print("Produto 2:")
print(f"CÓDIGO: {cod2}")
print(f"NOME: {nome2}")
print(f"QUANTIDADE: {qtd2}")
print(f"PREÇO UNITÁRIO: R$ {preco2:}")
print(f"TOTAL: R$ {total2:.2f}")
print("----------------------------")

print(f"VALOR TOTAL DAS COMPRAS: R$ {valor_total:}")
print("----------------------------")
