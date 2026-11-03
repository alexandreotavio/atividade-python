# Exercicio 1: le a idade em dias e mostra em anos, meses e dias.
# Considera que 1 ano tem 365 dias e 1 mes tem 30 dias.


def converter_idade(total_dias):
    anos = total_dias // 365
    resto = total_dias % 365
    meses = resto // 30
    dias = resto % 30
    return anos, meses, dias


def main():
    total_dias = int(input("Informe a idade em dias: "))
    anos, meses, dias = converter_idade(total_dias)
    print(f"Idade: {anos} ano(s), {meses} mes(es) e {dias} dia(s)")


if __name__ == "__main__":
    main()
