def contacion(elNumerito, listovich):
    for i in range(1, int(elNumerito)):
        listovich += str(i) + " "
    listovich += elNumerito
    '''basicamente aca lo que digo es que vaya sumando uno hasta llegar al numero deseado'''
    print(listovich)


contacion(input("A que numero queres contar? "), "")
