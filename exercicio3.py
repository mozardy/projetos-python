import json

# Carregar os dados do arquivo JSON
with open('faturamento.json.json', 'r') as file:
    faturamento_data = json.load(file)

# Extrair valores de faturamento e ignorar dias sem faturamento (valor = 0.0)
faturamento = [dia['faturamento'] for dia in faturamento_data if dia['faturamento'] > 0]

# Menor e maior faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Dias com faturamento acima da média
dias_acima_da_media = sum(1 for dia in faturamento if dia > media_mensal)

print("Menor faturamento:", menor_faturamento)
print("Maior faturamento:", maior_faturamento)
print("Dias com faturamento acima da média:", dias_acima_da_media)
