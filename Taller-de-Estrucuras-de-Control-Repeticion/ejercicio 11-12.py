consumir = int ( input ( "¿Consumir licor? Digite 1 para si y 2 para No: " ))
agr = 0
Ron = 0
cuello uterino = 0
teq = 0
whi = 0
otro = 0
licor = 0
listaco = []
listaco . agregar ( consumir )
listalicor = []
listaa ños = [ ]
listacv = []
listawhi = []
listam = []
listaf = []
listap = []
mientras que  es cierto :
    si (( consumir == 2 )):
        print ( f"Aguardiente { agr } \n Ron { ron } \n Cerveza { cerv } \n Tequila { teq } \n whisky { whi } \n Otro { otro } " )
        imprimir ( len ( listaco ))
        imprimir ( len ( listaf ))
        imprimir ( suma ( listam ))
        imprimir ( suma ( listap ) / suma ( listacv ))
        imprimir ( len ( listawhi ) / len ( listaco ))
        descanso
    elif ( consumir == 1 ):
        a ñ os = int ( input ( "Ingrese su edad: " ))
        listaaños . _ _ anexar ( años ) _ _
        sexo = str ( input ( "Ingrese su sexo. 1 para femenino y 2 para masculino: " ))
        licor = int ( input ( "1.Aguardiente, 2.Ron, 3.Cerveza, 4.Tequila, 5.Whisky, 6.Otro: " ))
        listalicor _ añadir ( licor )
        imprimir ( "Encuesta nueva" )
        consumir = int ( input ( " Continuar la encuesta, 1 para sí, 2 para no: " ))
        si ( licor == 1 ):
            agr = agr + 1
        elif ( licor == 2 ):
            Ron = Ron + 1 
        si ( licor == 3 ):
            cuello = cuello + 1
            listacv . agregar ( cerv )
            si ( licor == 3  y  a ños > 0 ) :
                p = a ñ os
                listap _ agregar ( pag )
                Seguir
        si ( licor == 4 ):
            teq = teq + 1
        si ( licor == 5 ):
            whi = whi + 1
            listawhi _ agregar ( whi )
        si ( licor == 6 ):
            otro = otro + 1  
        elif ( a ñ os >= 0 ):
            listaaños . _ _ anexar ( años ) _ _
            Seguir
        elif ( a ñ os <= 18 ) y ( sexo == 1 ):
            f = años + sexo _ _
            listaf . agregar ( f )
            Seguir
        elif ( 20 >= a ños < = 25 ) and ( sexo == 2 ) and ( licor != 5 ):
            m = años + sexo _ _
            si ( licor != 5 ):
                listam . agregar ( m )
            Seguir