def contar_digitos(numero):
    numero = abs(numero)

    if numero == 0:
        return 1

    contador = 0

    while numero > 0:
        numero = numero // 10
        contador += 1

    return contador


n = int(input("Digite um número inteiro: "))
print("Quantidade de dígitos:", contar_digitos(n))
