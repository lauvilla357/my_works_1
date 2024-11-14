# Lautaro Villafañe
# lautarovillafane27@gmail.com
# +543513830721
# Córdoba, Argentina
#---------------------------------------------------------------------------
# Un tablero de ajedrez no es otra cosa que una matriz cuadrada.
# Si los cuadrados que componene el tablero tienen dos colores, uno
# puede representarse como 1 y el otro como 0, por dar un ejemplo.

####################################################################################################################################

from random import randint                # Importación de función random

print('\nHOLA USUARIO\nBIENVENIDO AL PROGRAMA:\nEVALUACION DE PROPUESTAS PARA PINTAR UN TABLERO DE AJEDREZ\n')
print('Comencemos.\nººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº')
ejecucion=1

while ejecucion:
    
    f=int(input('\nIndique el numero de filas de la matriz: '))
    
    if f%2==0:
        
        condiciones=0
        contador=0
        contador2=0
        matrices_vistas=[]
        contador_ingresado=int(input('\nIndique el número de propuestas a evaluar: '))
        print('\nCondiciones a cumplir:\n1) Igual número de casillas rojas y azules\n2) No hay dos filas con igual número de casillas rojas\n3) No hay dos columnas con igual número de casillas rojas\n')
        print('#####################################\nPintamos...')
        
        while (condiciones==0) and (contador<contador_ingresado):
        
            c=f                     # como es cuadrada, Nº filas = Nº columnas, y como es un tablero de ajedrez, f  y c son par

            matriz=[]
            for k in range(f):                                           # Código para la creación y visualización de la matriz:
                matriz.append([0]*c)
           
            for x in range(len(matriz)):               # Este codigo es para pintar de rojo la matriz.
                for y in range(len(matriz[x])):           # Básicamente, el sistema propone una configuración.
                    matriz[x][y]=randint(0,1)                            #<<<< AQUI ESTA LA CLAVE!!!!

            
         #----------------------------------------------------------------------------------- ESTA PARTE TESTEA LAS CONDICIONES DEL EJERCICIO
                    
            if not (matriz in matrices_vistas):                               # Esto garantiza que solo las matrices nuevas se evaluen, nada de repetidas
                
                c_roja=0
                for a in range(len(matriz)):
                    for b in range(len(matriz[a])):
                        if matriz[a][b]==1:                                              # Esta parte hace el conteo de las casillas rojas y azules, verificacion condicion 1
                            c_roja+=1
                if c_roja==f*c-c_roja:
                    condicion1='T'
                else:
                    condicion1='F'


                n_coinc=0
                for q in range(len(matriz)):
                    conr=0
                    for w in range(len(matriz[q])):
                        if matriz[q][w]==1:
                            conr+=1
                    for e in range(len(matriz)):
                        if e!=q:
                            conr_2=0
                            for r in range(len(matriz[e])):                                         # Este bloque de código chequea si se cumple condicion 2
                                if matriz[e][r]==1:                                                     # REVISADO Y LISTO PARA FILAS!
                                    conr_2+=1
                            if conr==conr_2:
                                n_coinc+=1
                if n_coinc==0:
                    condicion2='T'
                else:
                    condicion2='F'

                    
                nueva_matriz=[]
                for x in range(f):
                    nueva_matriz.append([0]*c)
                for i in range(len(matriz)):
                  for j in range(len(matriz[i])):                               # Este código "vuelca" el tablero original, o sea convierte columnas del original en filas del volcado
                    nueva_matriz[j][i]=matriz[i][j]                             


                n_coinc=0
                for q in range(len(nueva_matriz)):
                    conr=0
                    for w in range(len(nueva_matriz[q])):
                        if nueva_matriz[q][w]==1:
                            conr+=1
                    for e in range(len(nueva_matriz)):
                        if e!=q:
                            conr_2=0
                            for r in range(len(nueva_matriz[e])):                               # Este bloque de código chequea si se cumple condicion 3 o no (si, al volcar se trabaja como filas)
                                if nueva_matriz[e][r]==1:                                                           # REVISADO Y LISTO PARA COLUMNAS!
                                    conr_2+=1
                            if conr==conr_2:
                                n_coinc+=1
                if n_coinc==0:
                    condicion3='T'
                else:
                    condicion3='F'


                # Chequeo FINAL:
                condiciones_preliminar=(condicion1,condicion2,condicion3)
                if 'F' in condiciones_preliminar:
                    pass
                else:
                    condiciones=1
                    print('\nCONFIGURACION ACEPTABLE:\n')
                    for g in matriz:
                        print(g)

                contador+=1
                matrices_vistas.append(matriz)
                        
            else:
                pass
            
            contador2+=1
            
        #-----------------------------------------------------------------------------------
        
        print('\nEjecución terminada.\nIteraciones: '+str(contador2)+'\n'+'Iteraciones efectivas: '+str(contador))  # Se muestra por pantalla el número de iteraciones reales
                                                                                                                                                                        # y el número de iteraciones asociadas a matrices evaluadas
    else:
        print('\nNo se puede proceder.\nRecuerde que, como es un tablero de ajedrez, sus filas\ny columnas no pueden ser impares.\n') # Advertencia de que f y c son pares
      
    ejecucion=int(input('\n-------------------------------\n¿Desea repetir? si = 1, no = 0\n'))  # Esto decide si el while principal se repite o no, nos da la opcion de salir
    

#####################################################################################################################################

##    FUNCIONAMIENTO DEL PROGRAMA:
##
##        Lo primero que se hace es crear una matriz que tendrá igual número de filas y columnas, ya que un tablero de ajedrez es
##        una matriz cuadrada.
##        Utilizando el método random, se llena aleatoriamente la matriz con 1 y 0, donde 1 representa rojo y 0 representa azul.
##        En este punto, tenemos lo que sería una propuesta de como pintar el tablero.
##        Nos aseguramos de que solo matrices únicas se evaluen y no se repita esa evaluación, lo cual permite mejorar
##        la precisión del programa.
##
##        Ahora toca llevar a cabo un chequeo de las condiciones indicadas en el ejercicio, que se resumen de la siguiente manera: 1) mismo
##        número de casillas rojas y azules; 2) dos filas no puden contener el mismo número de casillas rojas; 3) dos columnas no pueden contener el
##        mismo número de casillas rojas.
##        
##        Para la condición 1, se cuenta con un bloque de código que recorre la matriz y suma la unidad a una variable cada vez que se encuentra
##        una casilla con 1. De esta manera, tenemos el número de casillas rojas en la matriz, tal que el producto entre las filas
##        y las columnas menos el número de casillas rojas da el número de casillas azules. Si ambos números son iguales, entonces
##        la condición 1 se cumple. En tal caso, una variable llamada condicion1 se llena con 'T'. De lo contrario, se llena con 'F'.
##        
##        Para la condición 2, se usa un bloque de código que se encarga de posicionarse en una fila, contar el número de casillas
##        rojas y luego recorre el resto de las filas, contando en cada una las casillas rojas, y comparando finalmente si coincide el número
##        con la cantidad encontrada en la fila objetivo. Al usar un bucle for in, la fila objetivo va cambiando, de manera de someter a
##        todas las filas al test. Una variable llamada n_coinc se inicializa con 0, previo a la ejecución de este for in, a la cual se le adiciona la
##        unidad cada vez que se encuentren coincidencias, o sea, igualdades en el número de casillas rojas de las filas.
##        Por último, si n_coinc se mantiene en 0 posterior a la ejecución del bucle, se carga la variable condicion2 con 'T', y con 'F' en caso
##        contrario.
##
##        La condición 3 se evalua abusando del procedimiento usado en la condición 2. Primero, se "vuelca" la matriz para convertir sus
##        columnas en filas, y literalmente se utiliza el mismo código que en la condición 2, salvo cuestiones como que a esta matriz volcada la
##        llamo nueva_matriz. Si no se encuentran coincidencias, la variable condicion3 se carga con 'T', y sino con 'F'.
##
##        Finalmente, se crea la tupla condiciones_preliminar con condicion1, condicion2 y condicion3. Con un if se pregunta si está presente
##        'F' en la tupla.  De estarlo, pasa de largo. De no estarlo, una variable llamada condiciones se carga con 1, se despliega un mensaje
##        que dirá "CONFIGURACION ACEPTABLE" y se publica la matriz que cumple con las 3 condiciones.
##
##        CABE RESALTAR QUE HAY UN BUCLE WHILE QUE SE ENCARGA DE ITERAR, EL CUAL SE CORTA SI LA MATRIZ BUSCADA SE ENCUENTRA,
##        O SI EL NUMERO DE ITERACIONES INDICADO POR CONSOLA SE ALCANZA.
##        OTRO WHILE, PRINCIPAL, PERMITE PREGUNTAR AL USUARIO SI QUIERE REPETIR LA OPERACION.
##        POR CONSOLA SE PIDE EL NUMERO DE ITERACIONES (PROPUESTAS DIGAMOS) Y EL NUMERO DE FILAS DE LA MATRIZ (TABLERO).



