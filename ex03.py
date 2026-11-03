# Exercicio 3: le 3 numeros inteiros e mostra o menor deles.


def encontrar_menor(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor


def main():
    n1 = int(input("Informe o primeiro numero: "))
    n2 = int(input("Informe o segundo numero: "))
    n3 = int(input("Informe o terceiro numero: "))
    print(f"O menor numero e: {encontrar_menor(n1, n2, n3)}")


if __name__ == "__main__":
    main()