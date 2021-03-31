def inverte(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[len(string) - 1] + inverte(string[:(len(string) -1)])