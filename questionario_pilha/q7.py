lista, esperado_pref, esperado_geral = [], [], []
while 1:
    x = input()
    if x != "":
        lista.append(int(x))
    else:
        break

print("Fila geral original")
for i in range(len(lista)):
    print(f"{i+ 1} - {lista[i]}")

print("\nFila preferencial")
for i in range(len(lista)):
    if lista[i] > 59:
        print(f"{i + 1} - {lista[i]}")
        esperado_pref.append((i+ 1, lista[i]))
    else:
        esperado_geral.append((i + 1, lista[i]))

print("\nFila geral atualizada")
for i in range(len(lista)):
    if lista[i] < 60:
        print(f"{i+1} - {lista[i]}")

print("\nResultado esperado fila preferencial")
for i in range( len(esperado_pref)):
    print(f"{i+ 1} - {esperado_pref[i][0]}")

print("\nResultado esperado fila geral")
for i in range( len(esperado_geral)):
    print(f"{i+ 1} - {esperado_geral[i][0]}")



