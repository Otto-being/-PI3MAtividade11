def numero_perfeito(n):
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma += i

    return soma == n


num = int(input("Digite um número inteiro: "))

if numero_perfeito(num):
    print(num, "é um número perfeito.")
else:
    print(num, "não é um número perfeito.")
