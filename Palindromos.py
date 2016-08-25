
def es_Palindromo(numero):
    n = str(numero)
    tam = len(n)
    for i in range(tam):
        if n[i] != n[tam - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    contador = 0
    for i in range(10000000):
        if es_Palindromo(i) and es_Palindromo(bin(i)[2:]):
            contador += 1
    print(contador)

