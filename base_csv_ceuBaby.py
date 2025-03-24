import csv
import random
from datetime import datetime, timedelta

# Listas de dados para bairros e cidades da Paraíba
bairros = ["Centro", "Jatobá", "Belo Horizonte", "Salgadinho", "Liberdade", "Jardim Guanabara", "Santa Clara"]
cidades_paraiba = ["Patos", "Campina Grande", "João Pessoa", "Sousa", "Cajazeiras", "Guarabira", "Itaporanga", "Pombal"]

# Criar o arquivo CSV
with open("loja_artigos_infantis_refinado.csv", mode="w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["ID", "Nome Cliente", "Descrição Produto", "Quantidade", "Valor", "Idade", "Bairro", "Cidade", "Estado", "Data da Venda"])

    for i in range(1, 501):  # Gerar 500 registros
        nome = random.choice(["Ana", "João", "Marcos", "Beatriz", "Carlos", "Maria", "Lucas", "Fernanda", "José", "Laura"])
        produto = random.choice(["Roupa", "Calçados", "Chupetas", "Saída de Maternidade"])
        quantidade = random.randint(1, 10)
        valor = round(random.uniform(10.0, 500.0), 2)  # Valor entre R$10,00 e R$500,00
        idade = random.randint(18, 60)  # Idade entre 18 e 60
        bairro = random.choice(bairros)
        cidade = random.choice(cidades_paraiba)
        estado = "PB"
        # Gerar uma data aleatória nos últimos 180 dias
        data_venda = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%d/%m/%Y")

        escritor.writerow([i, nome, produto, quantidade, valor, idade, bairro, cidade, estado, data_venda])

print("Arquivo CSV 'loja_artigos_infantis_refinado.csv' gerado com sucesso!")