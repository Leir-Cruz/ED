def somalista(numeros):
   if len(numeros) == 1:
        return numeros[0]
   else:
        return numeros[0] + somalista(numeros[1:])

print(somalista([1,3,5,7,9]))