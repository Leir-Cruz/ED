

num, n = map(int, input().split())
second_line = input().split()

for i in range(num - n + 1):
#    valor = sum([int(item) for item in second_line[i:i+n]])
    valor = 0
    for j in range(n):
        valor += int(second_line[i + j])
    print(valor// n)

