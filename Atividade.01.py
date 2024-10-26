def encontrar_repetidos(vetor):
    """
    Encontra números repetidos em um vetor e suas posições.

    Args:
        vetor: Um vetor de números inteiros.

    Returns:
        None
    """

    repetidos = set()
    for i in range(len(vetor)):
        num = vetor[i]
        if num in repetidos:
            print(f"O número {num} se repete na posição {i}")
        else:
            repetidos.add(num)

# Leitura dos 10 números
vetor = []
for _ in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)

