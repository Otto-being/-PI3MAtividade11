def calcular_raiz(n, x):
    return n ** (1 / x)


n = float(input("Digite o radicando: "))
x = float(input("Digite a ordem da raiz: "))

resultado = calcular_raiz(n, x)
print("Resultado da raiz:", resultado)
