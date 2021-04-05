num_alunos, tentativas = map(int, input().split())
alunos = []
for i in range(num_alunos):
    alunos.append(input().split())
alunos.sort(key=lambda x: x[0], reverse=True)
for i in range(tentativas):
    escolhido = alunos[int(input()) - 1]
    if len(escolhido) > 2:
        for j in range(1, len(escolhido) - 1):
            escolhido[j] += " " + escolhido[j + 1]
            escolhido.pop(j + 1)
    print(f"{escolhido[1]} ({escolhido[0]})")