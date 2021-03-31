import math

num_hole = int(input())
bunny_x, bunny_y = map(float, input().split())
fox_x, fox_y = map(float, input().split()) #a velocidade da raposa é o dobro da do coelho
validate = 0

for j in range(num_hole):
    hole_x, hole_y = input().split()
    bunny_distance = math.sqrt((float(hole_x) - bunny_x)**2 + (float(hole_y) - bunny_y)**2)
    fox_distance = math.sqrt((float(hole_x) - fox_x)**2 + (float(hole_y) - fox_y)**2)
    if bunny_distance < fox_distance/2:
        print(f"O coelho pode escapar pelo buraco ({hole_x}, {hole_y}).")
        validate += 1
        break
if validate == 0:
    print("O coelho nao pode escapar.")
