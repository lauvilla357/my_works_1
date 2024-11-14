## SCPF Standar:
## https://scp-wiki.wikidot.com/
## SCPF Series:
## http://scp-int.wikidot.com/int-hub

import random

## Series: STANDAR, RU, KO, CN, FR, PL, ES, TH, JP, DE, IT, UA, PT, CS, ZH-TR, VN
##                      1             2      3      4      5    6     7      8     9   10   11 12   13    14      15       16    
## Lista de series SCPs:

lista_series=["STANDAR", "RU", "KO", "CN", "FR", "PL", "ES", "TH", "JP", "DE", "IT", "UA", "PT", "CS", "ZH-TR", "VN"]

print ("SCPs ya publicados:")

##-----------------------------------------------------
## LISTA DE SCPS YA PUBLICADOS:
lista_scp_publicados=[
        'ES4'
        ,'2472'
        ,'3095'
        ,'2297'
        ,'1243'
        ,'TH840'
        
        ]
for i in range(len(lista_scp_publicados)):
        print ("Video "+str(i+1)+"   ===>   SCP-"+lista_scp_publicados[i])

##-----------------------------------------------------
print ()
print ("PROXIMO SCP:")

## SOLO ESTANDAR:
##while 1:
##        proximo=random.randint(1,7000)
##        if str(proximo) in lista_scp_publicados:
##                pass
##        else:
##                print (proximo)
##                break
        
## CUALQUIER SERIE:
while 1:
        proximo_num=random.randint(1,7000)
        serie_num=random.randint(1,16)
        proximo_serie=lista_series[serie_num-1]
        
        siguiente_final=proximo_serie+str( proximo_num)

        if "STANDAR" in siguiente_final:
                if str(proximo_num) in lista_scp_publicados:
                        pass
                else:
                        print (str(proximo_num))
                        break
        else:
                proximo_num=random.randint(1,1000)
                siguiente_final=proximo_serie+str( proximo_num)
                if siguiente_final in lista_scp_publicados:
                        pass
                else:
                        print (siguiente_final)
                        break










