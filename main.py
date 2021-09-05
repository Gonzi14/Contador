num = True
laLista = ""
'''creo una variable que sea la lista donde guardo todos los numeros'''


def contacion(elNumerito, listovich):
    elNumeroPeroEnNumero = int(float(elNumerito))
    for i in range(1, elNumeroPeroEnNumero):
        listovich += str(i) + " "
    listovich += elNumerito
    '''basicamente aca lo que digo es que vaya sumando uno hasta llegar al numero deseado'''
    return print(listovich)


if num:
    corremelo = input("A que numero queres contar?")
    contacion(corremelo, laLista)
