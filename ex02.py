
import math

# Exercicio 2: le 3 valores inteiros e positivos e verifica se formam um triangulo.
# Se formarem, calcula a area 
# Se nao formarem, escreve os valores lidos.




def forma_triangulo(a, b, c):
    # O maior lado precisa ser menor que a soma dos outros dois.
    maior = max(a, b, c)
    soma_dos_outros = a + b + c - maior
    return maior < soma_dos_outros


def calcular_area(a, b, c):
    semiperimetro = (a + b + c) / 2
    return math.sqrt(
        semiperimetro
        * (semiperimetro - a)
        * (semiperimetro - b)
        * (semiperimetro - c)
    )


def main():
    a = int(input("Informe o valor de a: "))
    b = int(input("Informe o valor de b: "))
    c = int(input("Informe o valor de c: "))

    if forma_triangulo(a, b, c):
        print(f"Os valores formam um triangulo. Area: {calcular_area(a, b, c):.2f}")
    else:
        print(f"Os valores nao formam um triangulo: a={a}, b={b}, c={c}")


if __name__ == "__main__":
    main()
