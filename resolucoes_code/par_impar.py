# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

def verificar_paridade(num):
    # Verifica se o número é par ou ímpar
    if num % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

# Solicita um número inteiro do usuário
num = int(input("Por favor, insira um número inteiro: "))

# Usa a função para verificar a paridade do número
resultado = verificar_paridade(num)

print(resultado)