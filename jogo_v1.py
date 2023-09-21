# Projeto 1 = Desenvovimento de Game em Linguagem Python - Versão 1

# Importando Bibliotecas
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():

	# Windows
	if name == 'nt':
		_ = system('cls')

	# Mac ou Linux
	else:
		_ = system('clear')

# Função 
def game():

	limpa_tela()
	print("\nBem-vido(a) ao jogo da forca!")
	print("Adivinhe a palavra abaixo:\n")

	# Lista de palavras para o jogo
	palavras = ["audi", "ferrari", "porsche", "mercedes benz", "bmw" ]

	# Escolhe randomicamente uma palavra
	palavra = random.choice(palavras)

	# List comprehension
	letras_descobertas = ['_' for letra in palavra]

	# Número de tentativas
	chances = 6

	# Lista para as letras erradas
	letras_erradas = []

	# Loop enquanto número de chances for maior do que zero
	while chances > 0:

		# Print
		print(" ".join(letras_descobertas))
		print("\nChances Restantes:", chances)
		print("Letras Erradas:", " ".join(letras_erradas))

		# Tentativa
		tentativa = input("\nDigite uma letra: ").lower()

		# Condicional
		if tentativa in palavra:
			index = 0
			for letra in palavra:
				if tentativa == letra:
					letras_descobertas[index] = letra
				index += 1

		else:
			chances -= 1
			letras_erradas.append(tentativa)
