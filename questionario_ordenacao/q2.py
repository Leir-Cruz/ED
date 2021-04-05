lista = [float(input()) for i in range(int(input()))]
lista.sort(reverse=True)
[print(f"{item:.2f}") for item in lista]
