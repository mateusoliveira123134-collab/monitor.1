import random

palavras = [
    "python", "variavel", "algoritmo", "computador", "programa",
    "teclado", "internet", "sistema", "funcao", "compilador"
]

palavra_secreta = random.choice(palavras)
MAX_ERROS = 6
letras_certas = []
letras_erradas = []
erros = 0
ganhou = False

print("=== JOGO DA FORCA ===")
print("A palavra secreta tem", len(palavra_secreta), "letras.")

while erros < MAX_ERROS and not ganhou:
    palavra_oculta = ""
    for letra in palavra_secreta:
        if letra in letras_certas:
            palavra_oculta = palavra_oculta + letra + " "
        else:
            palavra_oculta = palavra_oculta + "_ "

    print("\nPalavra:", palavra_oculta)
    print("Letras erradas:", letras_erradas)
    print("Tentativas restantes:", MAX_ERROS - erros)

    chute = input("Digite uma letra: ").lower().strip()

    if len(chute) != 1 or not chute.isalpha():
        print("Entrada inválida! Digite apenas UMA letra.")
    elif chute in letras_certas or chute in letras_erradas:
        print("Você já tentou a letra '" + chute + "'. Tente outra!")
    elif chute in palavra_secreta:
        print("Boa! A letra '" + chute + "' existe na palavra.")
        letras_certas.append(chute)
    else:
        print("Ops! A letra '" + chute + "' não existe na palavra.")
        letras_erradas.append(chute)
        erros = erros + 1

    ganhou = True
    for letra in palavra_secreta:
        if letra not in letras_certas:
            ganhou = False

print("\n=============================")
if ganhou:
    print("PARABÉNS! Você venceu!")
    print("A palavra era:", palavra_secreta)
else:
    print("Que pena! Você perdeu.")
    print("A palavra secreta era:", palavra_secreta)
print("=============================")