def encontrar_repetidos(vetor):
    

    repetidos = set()
    for i in range(len(vetor)):
        num = vetor[i]
        if num in repetidos:
            print(f"O número {num} se repete na posição {i}")
        else:
            repetidos.add(num)


vetor = []
for _ in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)

