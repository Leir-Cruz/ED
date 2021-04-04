def piloto():
    nome = input()
    parciais = map(float, input().split())
    total = sum(parciais)
    return [nome, total]

def convert_time(time):
    converted_mili = round(time, 3)
    new = str(converted_mili).split(".")
    converted_min = round(float(new[0])/60, 2)
    return str(converted_min) + "." + str(new[1])


num_pilotos, h = int(input()), []
for i in range(num_pilotos):
    nome, total = piloto()
    novo_tempo = convert_time(total)
    h.append([nome, float(novo_tempo)])

print(h)

