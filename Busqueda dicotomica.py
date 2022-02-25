def main():
    lista = input ("Dame una lista ordenada ([[]] para terminar): ")
    while lista != [[]]:
        x = input("¿Valor buscado?: ")
        resultado = busqueda_binaria(lista, x)
        print "Resultado:", resultado
        lista = input ("Dame una lista ordenada ([[]] para terminar): ")