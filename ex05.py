# Exercicio 5: funcao que recebe uma frase e retorna uma nova frase
# com as letras de cada palavra invertidas, mantendo a ordem das palavras.


def inverter_palavras(frase):
    palavras = frase.split(" ")
    invertidas = []
    for palavra in palavras:
        invertidas.append(palavra[::-1])
    return " ".join(invertidas)


def main():
    frase = input("Informe uma frase: ")
    print(inverter_palavras(frase))


if __name__ == "__main__":
    main()