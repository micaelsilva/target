dados = [
("sp", 67_836_43),
("rj", 36_678_66),
("mg", 29_229_88),
("es", 27_165_48),
("outros", 19_849_53)
]

soma = sum([i[1] for i in dados])

for i in dados:
	print(f"{i[0]} - {(i[1] / soma) * 100:.2f}%")