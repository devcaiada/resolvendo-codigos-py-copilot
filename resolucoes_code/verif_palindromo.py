def verificar_palindromo(s):
    # Remove espaços e converte para minúsculas
    s = s.replace(" ", "").lower()

    # Verifica se a string é um palíndromo
    if s == s[::-1]:
        return "A string é um palíndromo."
    else:
        return "A string não é um palíndromo."

# Solicita uma string do usuário
str_usuario = input("Por favor, insira uma string: ")

# Usa a função para verificar se a string é um palíndromo
resultado = verificar_palindromo(str_usuario)

print(resultado)