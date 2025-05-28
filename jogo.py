import random

def escolher_palavra():
    # Abrir o arquivo e ler todas as linhas
    with open('Palavras.txt', 'r', encoding='utf-8') as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    # Escolher uma palavra aleatória
    palavra_selecionada = random.choice(palavras)
    return palavra_selecionada

def jogar():
    erros = 0
    palavra = escolher_palavra().lower()
    letras_descobertas = ["_" for _ in palavra]
    print(" ".join(letras_descobertas))

    while erros < 6:
        letra = str(input("Insira uma letra: ").lower())

        if letra in palavra.lower():
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            print("Letra incorreta!")
            erros += 1

        print(" ".join(letras_descobertas))
        if "_" not in letras_descobertas:
            print("Parabéns você ganhou!")
            break

    if erros == 6:
        print("Você perdeu, a palavra era:", palavra)

continuar = "s"
while continuar == "s":
    jogar()
    continuar = str(input("Deseja jogar novamente? (s/n) ").lower())