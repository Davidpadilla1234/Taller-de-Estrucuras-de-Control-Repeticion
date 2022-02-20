lista = []
numero = int ( input ( "numero 1 para agregar una altura y numero 2 para buscar la altura mas grande" ))
norte = 0
mientras que  es cierto :
    si ( numero == 1 ):
        n = flotador ( entrada ( "altura" ))
        numero = int ( input ( "numero 1 para agregar una altura y numero 2 para buscar el numero mas grande" ))
        lista _ agregar ( n )
    elif ( numero == 2 ):
        print ( "la mayor altura:" , max ( lista ))