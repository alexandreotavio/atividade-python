# Exercicio 4: funcao que retorna True se o numero for primo e False caso contrario.
# O teste e feito com os numeros de 1 a 100.


def eh_primo(numero):
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def main():
    for numero in range(1, 101):
        print(f"{numero}: {eh_primo(numero)}")


if __name__ == "__main__":
    main()