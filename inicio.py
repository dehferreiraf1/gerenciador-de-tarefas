while True:

	nome = input("nome? ")
	idade = int(input("idade? "))

	if idade >= 16:
		print(f"Olá, {nome}, você tem {idade} anos e ja pode votar")
	else:
		print(f"Olá, {nome}, você tem {idade} anos e não pode votar :(")

	continuar = input("Quer continuar? (s/n): ")
	if continuar.lower() != 's':
		break


#ano_atual = 2024
#ano_nascimento = ano_atual - idade
#print(f"você nasceu em {ano_nascimento}.")

