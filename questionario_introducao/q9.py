num_jogadores, campo, banco  = int(input()), [], []
habilidades = input().split()
for a in range(len(habilidades)):
    habilidades[a] = int(habilidades[a])
while len(campo) < 11:
    campo.append(max(habilidades))
    habilidades.remove(max(habilidades))
while len(banco) < 11:
    if len(habilidades) != 1:
        banco.append(max(habilidades))
        habilidades.remove(max(habilidades))
    else:
        banco.append(habilidades[0])
        habilidades.pop(0)
        break
print(sum(campo) - sum(banco))
