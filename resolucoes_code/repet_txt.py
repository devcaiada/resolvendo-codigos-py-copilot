# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def repetir_string(s, n):
    # Repete a string 's' 'n' vezes
    return s * n

# Solicita uma string do usuário
str_usuario = input("Por favor, insira uma string: ")

# Solicita um número inteiro do usuário
num_usuario = int(input("Por favor, insira um número inteiro: "))

# Usa a função para repetir a string
resultado = repetir_string(str_usuario, num_usuario)

print("A string repetida é: ", resultado)