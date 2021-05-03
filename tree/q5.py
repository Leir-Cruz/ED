for i in range(int(input())):
    instruction, base_list,  = input(), ['0/1', '1/1' , '1/0']
    if not instruction == "":
        for j in range(len(instruction)):
            if instruction[j] == 'E':
                numerator1, denominator1 = base_list[0].split("/")
                numerator2, denominator2 = base_list[1].split("/")
                base_list[2] = base_list[1]
                base_list[1] =  f'{int(numerator1) + int(numerator2)} / {int(denominator1) + int(denominator2)}'
            if instruction[j] == 'D':
                numerator1, denominator1 = base_list[1].split("/")
                numerator2, denominator2 = base_list[2].split("/")
                base_list[0] = base_list[1]
                base_list[1] =  f'{int(numerator1) + int(numerator2)} / {int(denominator1) + int(denominator2)}'
        print(base_list[1])
    else:
        print("1 / 1")

