def salvar_pessoas(pessoas):
	with open("pessoas.txt","w") as f:
		for nome, idade in pessoas.items():
			f.write(f"{nome},{idade}\n")

def ler_pessoas():
	pessoas = {}
	try:
		with open("pessoas.txt","r") as f:
			for linha in f:
				nome,idade = linha.strip().split(",")
				pessoas[nome] = int(idade)

	except FileNotFoundError:
		print("arquivo não encontrado.")
	return pessoas

pessoas = ler_pessoas()

while True:
	nome = input("nome ")
	idade = input("idade ")
	pessoas[nome] = idade

	continuar = input("s/n ")
	if continuar.lower() != 's':
		break

salvar_pessoas(pessoas)
print("dados salvos")