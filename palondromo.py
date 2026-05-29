def verificar_palindromo(texto):
    return texto == texto[::-1]


palavra = input("Digite uma palavra ou frase: ")

if verificar_palindromo(palavra):
    print("É palíndromo.")
else:
    print("Não é palíndromo.")
