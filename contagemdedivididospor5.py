def contar_divisiveis_por_5(n):
    contador = 0

    for i in range(1, n + 1):
        if i % 5 == 0:
            contador += 1

    return contador


n = int(input("Digite um número: "))
resultado = contar_divisiveis_por_5(n)

print("Quantidade de números divisíveis por 5 entre 1 e", n, "=", resultado)
