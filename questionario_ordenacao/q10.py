quant_num, fator = map(int, input().split())
lst = [int(input()) for i in range(quant_num)]
new_lst = [((x % fator) / quant_num, x) for x in lst]

