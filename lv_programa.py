## Lautaro Villafañe
## ivilla1357@gmail.com
## 3513830721
## Argentina
## ############################################################################################################################## ##

## Programa ready. Si me importara el valor de la posición 2023202320232023, no se podría alcanzar por cuestión de tiempo.

ejecucion=1
while ejecucion:
    
    #----------------------------------------------------------------------------------------------------------------------------    
    contador=0
    sumador=0
    l=[]

    puesto=int(input('\n¿De qué puesto necesito el valor?\n>>>> '))

    a=2023
    b=2024
    c=2025

    l_a_b_c=[a,b,c]

    if puesto<=100:
        if puesto in (1,2,3):
            l.append(puesto)
            l.append(l_a_b_c[puesto-1])
                
        else:
            while contador<100-3:
                contador+=1
                sumador=a+b+c
                if contador==puesto-3:
                    l.append(contador+3)
                    l.append(sumador)
                a=b
                b=c
                c=sumador
        print('\nPosición '+str(l[0])+': '+str(l[1])+'\n')

        res = [int(x) for x in str(l[1])]
        print('Ultimas 4 cifras: ',res[len(res)-4],res[len(res)-3],res[len(res)-2],res[len(res)-1]) # ESTE CODIGO ES LA RESPUESTA!!!!
        
    else:
##        while contador<100+30:
##            contador+=1
##            sumador=a+b+c
##    ##        print(str(contador+3)+'. '+str(sumador))
##            a=b
##            b=c
##            c=sumador
##
##        contador=0
##        sumador=0
##        a=2023
##        b=2024
##        c=2025
        while contador<puesto+3:
            contador+=1
            sumador=a+b+c
            
            if contador==puesto-3:
                l.append(contador+3)
                l.append(sumador)
                
            a=b
            b=c
            suma_lista = [int(x) for x in str(sumador)]
            if len(suma_lista)>4:
                c=int(str(suma_lista[len(suma_lista)-4]) + str(suma_lista[len(suma_lista)-3]) + str(suma_lista[len(suma_lista)-2]) + str(suma_lista[len(suma_lista)-1]))
            else:
                c=sumador
        print('\nPosición '+str(l[0])+': '+str(l[1])+'\n')
        
        res = [int(x) for x in str(l[1])]
        print('Ultimas 4 cifras: ',res[len(res)-4],res[len(res)-3],res[len(res)-2],res[len(res)-1]) # ESTE CODIGO ES LA RESPUESTA!!!!
        
    #----------------------------------------------------------------------------------------------------------------------------     

    ejecucion=int(input('\n¿Quiere repetir? Si = 1, No = 0\n'))

## ###################################################################################################################### ##

##    BUENO, EL PROGRAMA ESTA LISTO. PARA SOLUCIONAR EL TIEMPO DE EJECUACION, SOLO SE TIENE QUE CONTINUAR
##    CON LOS ADELANTAMIENTOS DE LOS VALORES A, B Y C DE MANERA DE REDUCIR EL PODER DE COMPUTO
##    NECESARIO PARA EL VALOR DE INTERES A UN TIEMPO RAZONABLE.
##    EL ADELANTAMIENTO HASTA VALORES DE LOS PUESTOS 1000000 ES EL PRIMERO QUE SE PODRIA HACER, MOSTRANDO UNA IMPORTANTE
##    REDUCCION EN EL TIEMPO DE EJECUCION AL PEDIR, POR EJEMPLO, EL VALOR DEL PUESTO 10000000 EN RELACION AL TIEMPO
##    REQUERIDO PARTIENDO DE LOS INICIADORES A-B-C ORIGINALES.
##    SE PLANTEA CONTINAUR CON LOS ADELANTAMIENTOS HASTA APROXIMARSE AL BILLON.
##    SE ENTIENDE QUE LO IDEAL SERIA COLOCAR LOS INICIADORES EN VALORES DE LOS PUESTOS 10 BILLONES.

##    PARA ELLO, SE PLANTEA, POR EJEMPLO, HABIENDO HECHO EL ADELANTAMIENTO HASTA VALORES DEL TORNO AL
##    PUESTO 1000000, PEDIR LOS VALORES DE 10000001, 2, 3, 4 Y 5 DONDE LOS PRIMEROS 3 SIRVEN COMO INICIADORES PARA
##    EL SIGUIENTE ADELANTAMIENTO Y 4 Y 5 SIRVEN PARA CONTROL. SE RECOMIENTO ADICIONALMENTE OTROS PUNTOS
##    PUNTOS DE CONTROL. CON ESTA LOGICA, APROXIMARNOS TANTO COMO SEA POSIBLE A 100 BILLONES, PARA ASI PEDIR
##    EL VALOR DE INTERES.
##
##    SE DEBE TENER E CUENTA, QUE LA DIFERENCIA ENTRE 1 MILLON DE ITERACIONES CON 1 NO ES IGUAL A LA DIFERENCIA ENTRE
##    10 MILLONES Y 1 MILLON, 1000 MILLONES Y 100 MILLONES O 10 BILLONES Y 1 BILLON. ESTA DIFERENCIA ES CRECIENTE.
##    POR ELLO, EL ACERCAMIENTO AL PUESTO DE INETERES TIENE QUE SER MUY MUY CERCANO.

    #------------------------------<<<<<<<<<<<---------->>>>>>>>>----------------------------

##    EXPLICACION Y APRENDIZAJE DEL EJERCICIO:
##
##        EL PROGRAMA SE REALIZA BAJA LA PREMISA QUE TENGO TRES NUMEROS INICIALES, TRES VARIABLES CONOCIDAS
##        Y DETERMINADAS A LAS QUE SE LES LLAMA A, B Y C. EL CALCULO DE LA SUMA Y POSTERIOR REPETICION CON LOS ULTIMOS
##        3 VALORES "IMPRESOS" SE  REALIZA CON UNA CONNBINACION DE UN BUCLE WHILE Y UNA REASIGNACION DE VALORES
##        TAL QUE A PASA A SER LO QUE ERA ANTES B, B PASA SA SER LO QUE ANTES ERA C Y C PASA A SER LO QUE SE DENOMINA
##        SUMADOR (LA VARIALBE QUE GUARDA LA SUMA JUSTAMENTE).
##        UNA LISTA VACIA LLAMADA L ES LA QUE SE ENCARGA DE CAPTURAR EL VALOR DE INTERES ASI COMO SU POSICION.
##        UNA LISTA CREADA DE FORMA EXPRESS LLAMADA SUMA_LISTA SE USA PARA CAPTURAR LAS ULTIMAS CUATRO CIFRAS
##        DEL NUMERO QUE SE HALLA EN LA POSICION DE INTERES. CON ELLO, SE AHORRA TIEMPO DE COMPUTO AL TRABAJAR SIEMPRE
##        CON LAS ULTIMAS CUATRO CIFRAS DE CADA NUMERO (ESTO FUNCIONA GRACIAS A QUE LA SUMA SE REALIZA DIGITO A DIGITO
##        DE DERECHA A IZQUIERDA).
##
##        FUNCIONAMIENTO:
##            INICIA EL PROGRAMA, SE CREA UNA VARIABLE LLAMADA EJECUCION QUE TOMA EL VALOR 1.
##            SE DISPARA UN BUCLE WHILE QUE USA COMO ARGUMENTO LA VARIABLE EJECUCION.
##            LUEGO DE DISPARARSE EL WHILE LA PRIMERA VEZ, SE CREAN LAS VARIABLES A-B-C CON SUS VALORES INICIALES, LA LISTA
##            VACIA L, EL SUMADOR EN 0, EL CONTADOR EN EL VALOR CORRESPONDIENTE A LA POSICION DE LOS VALORES INICIADORES
##            Y SE CREA UNA LISTA LLAMADA L_A_B_C FORMADA CON LAS ASIGNACIONES DE LAS VARIABLES A, B Y C. ADEMAS, SE LE SOLICITA AL USUARIO
##            QUE INDIQUE EL PUESTO DEL VALOR QUE NECESITA CONOCER LAS ULTIMAS CUATRO CIFRAS. ESTO SE GUARDA EN LA VARIABLE PUESTO.
##
##            SE ENCUENTRA CON DOS NIVELES DE SENTENCIA CONDICIONAL IF.
##            EN EL PRIMERO, SE DISTINGUE SI LA VARIABLE PUESTO ES MENOR A UN CIERTO VALOR. DE SER TRUE, APARECE UN SEGUNDO NIVEL
##            DE SENTENCIA IF QUE PREGUNTA SE PUESTO COINCIDE CON BASICAMENTE LOS INICIADORES, EN CUYO CASO SE GUARDAN EN LA
##            LISTA L JUNTO A SU POSICION. DE SER FALSE SE EJECUTA UN ELSE QUE CONTIENE UN BUCLE WHILE QUE PERMITE A TRAES DE UN IF
##            BUSCAR EL VALOR DEL PUESTO EN CUESTION. UN VEZ LOCALIZADO, SE IMPRIMEN LAS ULTIMAS 4 CIFRAS A TRAVES DE UNA LISTA
##            EXPRESS LLAMADA RES Y UN PRINT QUE USA LA FUNCION LEN PARA IDENTIFICAR ESTOS 4 NUMEROS.
##            VOLVIENDO AL PRIMER NIVEL DE SENTENCIA IF, DE NO CUMPLIRSE EL PRIMER NIVEL, SE EJECUTE UN ELSE QUE CONTIENE DOS BUCLE WHILE.
##            EL PRIMERO ES A LOS FINES DE MOSTRAR UNA PARTE DE LA EJECUCION SI ES QUE EL USUARIO LO DESEA. NO OBSTANTE, EL IMPORTANTE
##            ES EL SEGUNDO.
##            PREVIO A LA EJECUCION DEL SEGUNDO WHILE, SE REINICIAN LOS VALORES DE A-B-C ASI COMO DEL SUMADOR Y DEL CONTADOR
##            (ESTO POR LA EJECUCION DEL PRIMER WHILE). AL EJECUTARSE EL SEGUNDO WHILE, JUNTO A UN IF SE ENCARGA DE BUSCAR
##            EL VALOR PEDIDO, CAPTURANDOLO EN LA LISTA L AL ENCONTRARLO. LUEGO, UNA LISTA EXPRESS LLAMADA SUMA_LISTA JUNTO A UN
##            IF ELSE SE ENCARGAN DE GARANTIZAR LA CAPTURA DE LAS ULTIMAS 4 CIFRAS, QUE SE MUESTRAN POR PANTALLA.
##            AL FINAL DE TODO SE EJECUTA UN PRINT QUE PREGUNTA SI EL USUARIO DESEA REPETIR O NO, TAL QUE INTRADUZCA 1 SI ES SI O 0 SI
##            ES NO. EN EL PRIMER CASO (ENTENDIENDO QUE SE DEBEN COLOCAR FILTROS PARA EVITAR QUE EL USUARIO USO UN NUMERO DIFERENTE A 1
##            O QUE CLAVE EL PROGRAMA INTRODUCIENDO UNA LETRA), EJECUCION SE MANTIENE CON UN 1 Y AL VOLVER EL BUCLE WHILE
##            SE EJECUTA DE NUEVO. EN EL SEGUNDO CASO, EL VALOR DE EJECUCION CAMBIA A 0 Y POR TANTO EL ARGUMENTO DE WHILE
##            SE VUELVE FALSE, TERMINANDO LA EJECUCION DEL PROGRAMA.
##         
##
##
##                    APRENDIZAJE.
##
##                    EL EJERCICIO DA UNA LECCION RESPECTO A UN PROBLEMA FRECUENTE EN LA COMPUTACION COMO ES EL TIEMPO DE EJECUCION.
##                    EN VIRTUD DE ESTO, SE APRENDIO QUE CADA AHORRA EN TIEMPO DE EJECUCIION ES UMPORTANTE.
##                    SI LA SUMA DE LAS ULTIMAS 4 CIFRAS ES SUFICIENTE PARA BUSCAR, NO TIENE SENTIDO HACER QUE EL PROGRAMA UTILICE
##                    LOS NUMEROS COMPLETOS.
##                    ESTO ULTIMO LLEVARA A QUE EL MISMO DEBA LIDIAR CON NUMEROS QUE CONSTAN DE CIENTOS DE MILES DE DIGITOS.
##                    ESTA LUCHA, DE HECHO, LA VEN REFLEJADA EN DOS LINEAS AL PRINCIPIO QUE HABLAN DE LA IMPORTACION
##                    DE UN METODO QUE PERMITE AMPLIAR EL NUMERO DE DIGITOS ACEPTADOS POR STR (4300 POR DEFECTO). LUEGO DE LAS MODIFICACIONES
##                    EXPLICADAS ANTES ESTAS DS LINEAS NO SON NECESARIA.
                    


