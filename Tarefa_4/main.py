# Função de ordenação por inserção
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move os elementos da arr[0..i-1], que são maiores que o key, para uma posição à frente
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Leitura da entrada
N = int(input())  # Número de candidatos
times = list(map(float, input().split()))  # Tempos dos candidatos

# Ordenando os tempos usando o algoritmo de ordenação por inserção
insertion_sort(times)

# Imprimindo os tempos ordenados com 2 casas decimais
print(" ".join(f"{time:.2f}" for time in times))

#Teste
#5
#10.23 9.85 9.56 10.00 9.74