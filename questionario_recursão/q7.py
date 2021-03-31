
def fibonacci(n):
    if n <= 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fi = fibonacci(n -1)
        fi.append(fi[n -2] + fi[n -3])
        return fi

fibonacci(10)