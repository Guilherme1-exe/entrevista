def is_fibonacci(num):
    # Função para verificar se um número é quadrado perfeito
    def is_perfect_square(x):
        s = int(x**0.5)
        return s*s == x
    
    # Um número é Fibonacci se e somente se 5*n^2 + 4 ou 5*n^2 - 4 for um quadrado perfeito
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

# Defina um número (ou solicite uma entrada do usuário com input())
num = int(input("Informe um número: "))

# Verificação
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
