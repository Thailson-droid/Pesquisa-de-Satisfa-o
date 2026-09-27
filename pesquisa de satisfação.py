total_excelente = 0
total_bom = 0
total_ruim = 0

for i in range(50):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    satisfacao = input(
        "Qual a sua satisfação? (E = excelente, B = bom, R = ruim): "
    ).lower()

    if satisfacao == "e":
        total_excelente += 1
    elif satisfacao == "b":
        total_bom += 1
    elif satisfacao == "r":
        total_ruim += 1

print("Quantidade de respostas excelente:", total_excelente)
print("Quantidade de respostas bom:", total_bom)
print("Quantidade de respostas ruim:", total_ruim)
