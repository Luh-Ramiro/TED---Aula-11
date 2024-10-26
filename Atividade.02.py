import random

# Criando a matriz A 10x10 com valores aleatórios
A = [[random.randint(1, 100) for _ in range(10)] for _ in range(10)]

# Imprimindo a matriz A (opcional, para visualização)
for linha in A:
    print(linha)

# Calculando a soma de todos os elementos da matriz A
soma_total = sum(sum(linha) for linha in A)
print(f"A soma de todos os elementos da matriz A é: {soma_total}")

# Criando a matriz B, multiplicando cada elemento de A por 3
B = [[elemento * 3 for elemento in linha] for linha in A]

# Imprimindo a matriz B (opcional, para visualização)
print("Matriz B:")
for linha in B:
    print(linha)