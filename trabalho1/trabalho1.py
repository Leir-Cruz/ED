class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque


def adicionar_alfabeto(deque, alfabeto):
    for l in alfabeto:
        deque.add_front(l)

def decifrar(deque, texto_cifrado, chave):
    decifrada = ""
    for i in texto_cifrado:
        ponteiro = deque.remove_front()
        deque.add_rear(ponteiro)
        while ponteiro != i:
            ponteiro = deque.remove_front()
            deque.add_rear(ponteiro)       #aqui ele achou a letra
        for i in range(chave):
            ponteiro = deque.remove_front()
            deque.add_rear(ponteiro)
        decifrada += ponteiro
    return decifrada

def selecionar_subconjunto_missoes():
    hours_avaiable = int(input())
    show = int(input())
    ordination = int(input())
    alfabet = input()
    key = int(input())
    num_missions = int(input())
    d, missions = Deque(), []

    adicionar_alfabeto(d, alfabet)

    for i in range(num_missions):
        stringi = input()
        sem_colchete = stringi.replace('[', '').replace(']', '')
        deciphered = decifrar(d, sem_colchete, key)
        missions.append(deciphered.split(','))
#----Todas as missoes foram adicionadas a um array como outro array com: nome, duracao, valor, nivel-----#

    matriz = []
    for i in range(num_missions + 1):
        matriz.append([])
        for j in range(hours_avaiable + 1):
            if i == 0 or j == 0:
                matriz[i].append(0)
            else:
                matriz[i].append(-1)

    def mochila(num_mission, missoes, tempo_total):
        if matriz[num_mission][tempo_total] == -1:
            if int(missoes[num_mission - 1][1]) > tempo_total:
                matriz[num_mission][tempo_total] = mochila(num_mission - 1, missoes, tempo_total)
            else:
                usa = int(missoes[num_mission - 1][2]) + mochila(num_mission - 1, missoes, tempo_total - int(missoes[num_mission -1][1]))
                naousa = mochila(num_mission - 1, missoes, tempo_total)
                matriz[num_mission][tempo_total] = max(usa, naousa)
        return matriz[num_mission][tempo_total]

    def solucao(matrx, all_mission):
        num, feitas, tempo_total = len(matrx), [], len(matrx[0])
        while num >= 1:
            if matrx[num - 1][tempo_total - 1] == matrx[num - 2][tempo_total -1 - int(all_mission[num - 2][1])] + int(all_mission[num -2][2]):
                feitas.append(all_mission[num - 2])
                tempo_total -= int(all_mission[num - 2][1])
            num -= 1
        return feitas

    mochila(num_missions, missions, hours_avaiable)
    missoes_feitas = solucao(matriz, missions)

    if show == 1:
        array = []
        for i in range(len(missoes_feitas)):
            result = missoes_feitas[i][0] + ", " + missoes_feitas[i][1] + ", " + missoes_feitas[i][2] + ", " + \
                     missoes_feitas[i][3]
            array.append(result)
        if ordination == 0:
           sorted_array = sorted(array)
        elif ordination == 1:
            def ordering(e):
                a = e.split(', ')
                return int(a[1])
            sorted_array = sorted(array, key=ordering)
        elif ordination == 2:
            def ordering(e):
                a = e.split(', ')
                return int(a[2])
            sorted_array = sorted(array, key=ordering)
        elif ordination == 3:
            def ordering(array):
                easy, medium, hard = [], [], []
                for item in array:
                    frase = item.split(', ')
                    if frase[3] == "easy":
                        easy.append(item)
                    elif frase[3] == "medium":
                        medium.append(item)
                    elif frase[3] == "hard":
                        hard.append(item)
                sorted_easy, sorted_medium, sorted_hard = sorted(easy), sorted(medium), sorted(hard)
                return sorted_easy + sorted_hard + sorted_medium
            sorted_array = ordering(array)

        for misson in sorted_array:
            print(misson)

    print(f"Tempo restante: {hours_avaiable - sum([int(missao[1]) for missao in missoes_feitas])}")
    print(f"Valor: {sum(int(missao[2]) for missao in missoes_feitas)}")

d = Deque()
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
adicionar_alfabeto(d, alfabeto)
texto_cifrado = 'XTYSLKNLCL'
print(f'texto_plano: {decifrar(d, texto_cifrado, len(alfabeto))}')
print(f'{str(d)}')
print(f'{len(str(d))}')

d = Deque()
adicionar_alfabeto(d, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(f'Alfabeto: {d}')
print(f'Tamanho: {len(str(d))}')

d = Deque()
adicionar_alfabeto(d, ' ')
print(f'Alfabeto: {d}')
print(f'Tamanho: {len(str(d))}')

d = Deque()
adicionar_alfabeto(d, '0123456789 ')
print(f'Alfabeto: {d}')
print(f'Tamanho: {len(str(d))}')

d = Deque()
adicionar_alfabeto(d, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
texto_cifrado = 'ECUC'
print(f'{str(d)}')
print(f'texto_plano: {decifrar(d, texto_cifrado, 2)}')
print(f'{str(d)}')
print(f'{len(str(d))}')

selecionar_subconjunto_missoes()