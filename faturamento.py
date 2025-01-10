import json

with open("dados.json", "r") as f:
	dados = json.load(f)

faturamentos = [i['valor'] for i in dados if i['valor'] != 0]
media = sum(faturamentos) / len(faturamentos)
dias_maior_media = [i for i in faturamentos if i > media]

print(f'- Houveram {len(dias_maior_media)} dias com faturamento maior que a média')
print(f'- O maior faturamento diário foi de {max(faturamentos)}')
print(f'- O menor faturamento diário foi de {min(faturamentos)}')