lista = []
listan = []
listaf = []
estudiantes = int ( input ( "Ingrese la cantidad de estudiantes: " ))
estu = int ( input ( "Ingrese 1 para agregar nombres y puntajes: " ))
para  i  en  rango ( 0 , estudiantes ):
    est = entrada ()
    si ( estu == 1 ):
        s = ( nombre , puntaje ) = est . dividir ( " " )
        nombre = str ( nombre )
        puntaje = int ( puntaje )
        listán _ adjuntar ( nombre )
        listao . agregar ( puntuación )
        listaf . agregar ( es )
        promedio = sum ( listao ) / len ( listao )
        n  = [ i  para  i  en  listao  si  i > promedio ]       
        inf = ( len ( n ) * 100 ) / len ( listao )
        s  = [ i  para  i  en  listao  si  i < promedio ]
        sup = ( len ( s ) * 100 ) / len ( listao )
    elif ( estu == 2 ):
        descanso
print ( "El estudiante con el puntaje más alto es: " , ( listaf [ listao . index ( max ( listao ))]))
print ( "El estudiante con el puntaje más bajo es: " , ( listaf [ listao . index ( min ( listao ))]))
print ( "El puntaje maximo es: " , max ( listao ))
print ( "El puntaje máximo es: " , min ( listao ))
print ( "Promedio de puntajes: " , promedio )
print ( f"Porcentaje de estudiantes que estan bajo el promedio: { inf } %" )
print ( f"Porcentaje de estudiantes que estan sobre el promedio: { sup } %" )