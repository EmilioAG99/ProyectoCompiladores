import ply.yacc as yacc 
import os
import codecs
import re
from lexico import tokens
import sys 
from lexico import numeroLinea
from lexico import diccionario
from lexico import diccionarioFunciones
global banderaFuncion 
banderaFuncion = 0
global lineaFuncion 
lineaFuncion = 0
global contadorReturn 
contadorReturn = 0
global regresoFuncion 
regresoFuncion =""
def p_programa(p):
    ''' start : variablesGlobales declaracionEstructuras declaracionFuncion declaraMain '''
    print("inicio")
def p_variablesGlobales(p):
    '''variablesGlobales : ABIWORLD declaracionVariable PC variablesGlobales'''
    print("abiworld")
def p_variablesGlobales2(p):
    '''variablesGlobales : empty'''
def p_declaracionVariable(p):
    '''declaracionVariable : tipoDatos ID ASIG tipoValores 
                           | declaracionArreglo '''
    print("variable unica")
def p_declaracionVariable1(p):
    '''declaracionVariable : declaracionVariable C declaracionVariable'''
    print("Multiples variables")
def p_declaracionVariable2(p):
    '''declaracionVariable : empty'''
def p_tipoDatos(p):
    '''tipoDatos : INT
                 | CHAR
                 | STRING
                 | BOOL
                 | FLOAT
                 | VOID
                 '''
def p_tipoValores(p):
    '''tipoValores : NUMERO
                   | FLOAT_VALOR
                   | CHAR_VALOR
                   | STRING_VALOR
                   | TRUE
                   | FALSE'''
        
def p_declaracionArreglo(p):
    ''' declaracionArreglo : ABIRRAY tipoDatos ID ASIG CORA NUMERO CORC
                           | ABIRRAY tipoDatos ID ASIG CORA NUMERO CORC CORA NUMERO CORC
                           | ABIRRAY tipoDatos ID '''  
    print("ABIRRAY DETECTADO")
def p_declaracionEstructuras(p):
    ''' declaracionEstructuras : ABISTRUCT ID LLAVEA declaracionVariable LLAVEC PC declaracionEstructuras'''
    print("abistruct")
def p_declaracionEstructuras1(p):
    ''' declaracionEstructuras : empty'''
def p_declaracionFuncion(p):
    '''declaracionFuncion : tipoDatos ID PARENTA declaracionParametros PARENTC LLAVEA listaInst return LLAVEC declaracionFuncion'''
    print("SE ENCONTRO FUNCION")
    global banderaFuncion 
    banderaFuncion = 1
    print("citaaaaaaaaa",p[1])
def p_declaracionFuncion1(p):
    '''declaracionFuncion : empty'''
def p_declaracionParametros(p):
    '''declaracionParametros : tipoDatos ID'''
    print("encuentra Parametro")
def p_declaracionParametros1(p):
    '''declaracionParametros : declaracionParametros C declaracionParametros'''
    print("encuentra multiparametros")
def p_declaracionParametros2(p):
    '''declaracionParametros : empty'''
def p_declaraMain(p):
    '''declaraMain : ABIMAIN LLAVEA listaInst LLAVEC'''
    print("se encontro main")
def p_declaracionCiclo(p):
    '''declaracionCiclo : ABIJOR PARENTA inicializacion PC cond PC cambio PARENTC LLAVEA listaInst LLAVEC  declaracionCiclo'''
    print("se encontro el ciclo")
def p_declaracionCiclo1(p):
    '''declaracionCiclo : empty '''
def p_inicalizacion(p):
    '''inicializacion : INT ID ASIG NUMERO
                      | ID ASIG NUMERO'''
def p_cond(p):
    '''cond : ID operadores ID
            | ID operadores NUMERO '''
def p_operadores(p):
    ''' operadores : LT
                   | LTE
                   | GTE
                   | GT'''
def p_cambio(p):
    '''cambio :  ID ASIG ID AGREGA ID
              |  ID ASIG ID RESTA ID 
              |  ID ASIG ID AGREGA NUMERO
              |  ID ASIG ID RESTA NUMERO 
              |  ID INCREMENTO
              |  ID DECREMENTO'''
def p_declaracionIf(p):
    '''declaracionIf : ABIF  PARENTA condicion PARENTC LLAVEA  listaInst LLAVEC declaracionElse declaracionIf
                     | ABIF  PARENTA condicion PARENTC LLAVEA  listaInst LLAVEC declaracionIf
                    '''
    print("Se encontro el IF")
def p_declaracionIf1(p):
    '''declaracionIf : empty
                    '''
def p_declaracionElse(p):
    '''declaracionElse : ELSE LLAVEA listaInst LLAVEC '''
    print("se encontro el ELSE")
def p_condicion(p):
    '''condicion : ID  operadoresRel ID operadoresLogicos condicion
                 | ID  operadoresRel ID
                 | ID  
                 | tipoValores
                 | ID  operadoresRel tipoValores operadoresLogicos condicion
                 | ID  operadoresRel tipoValores  
                 | NOT ID  operadoresRel ID operadoresLogicos condicion
                 | NOT ID  operadoresRel ID
                 | NOT ID  operadoresRel tipoValores operadoresLogicos condicion
                 | NOT ID  operadoresRel tipoValores 
                 | ID  operadoresRel NOT ID operadoresLogicos condicion
                 | ID  operadoresRel NOT ID
                 | ID  operadoresRel NOT tipoValores operadoresLogicos condicion
                 | ID  operadoresRel NOT tipoValores
                 | NOT PARENTA condicion PARENTC '''
def p_operadoresLogicos(p):
    '''operadoresLogicos : AND
                         | OR'''
def p_operadoresRel(p):
    '''operadoresRel : LT
                     | LTE
                     | GT
                     | GTE
                     | NE
                     | COMP'''
def p_entradaDatos(p):
    '''entradaDatos : ABIN PARENTA ID PARENTC PC entradaDatos'''
def p_entradaDatos1(p):
    '''entradaDatos : empty'''
def p_salidaDatos(p):
    ''' salidaDatos : ABOUT PARENTA STRING_VALOR PARENTC salidaDatos PC
                    | ABOUT PARENTA listaSalida PARENTC  salidaDatos PC
                    | ABOUT PARENTA STRING_VALOR C listaSalida PARENTC PC salidaDatos'''
def p_salidaDatos1(p):
    ''' salidaDatos : empty'''
def p_listaSalida(p):
    '''listaSalida : ID C listaSalida
                   | ID'''

def p_operacionesBasicas(p):
    ''' operacionesBasicas : ID ASIG ID operadoresBasicos ID PC operacionesBasicas
                           | ID ASIG tipoValores operadoresBasicos ID PC operacionesBasicas
                           | ID ASIG tipoValores operadoresBasicos tipoValores PC operacionesBasicas
                           | ID ASIG ID operadoresBasicos tipoValores PC operacionesBasicas
                           | ID ASIG tipoValores PC operacionesBasicas
                           | ID ASIG ID P ID PC operacionesBasicas
                           | ID ASIG ID PC operacionesBasicas
                           | ID P ID PC operacionesBasicas
                           | ID ASIG ID CORA NUMERO CORC PC operacionesBasicas
                           | ID CORA NUMERO CORC ASIG ID CORA NUMERO CORC PC operacionesBasicas
                           | ID CORA NUMERO CORC ASIG tipoValores PC operacionesBasicas
                           | ID PARENTA listaValores PARENTC  PC operacionesBasicas
                           | ID ASIG ID PARENTA listaValores PARENTC  PC operacionesBasicas'''
    
    if(p[4]=="("):
        global banderaFuncion
        banderaFuncion = 1
        global lineaFuncion
        lineaFuncion = int((p.linespan(4)[0]  - (numeroLinea - 1))/2)
        if(diccionarioFunciones.get(p[3]) is None):
                sys.exit("No existe la funcion de la linea {0}".format(int((p.linespan(4)[0]  - (numeroLinea - 1))/2)))
        else:
            global regresoFuncion 
            regresoFuncion = list(diccionarioFunciones[p[3]].keys())[0]
            variableDeRegreso = list(diccionario[p[1]].keys())[0]
            if(regresoFuncion == variableDeRegreso):
                pass
            else:        sys.exit("Error semantico en linea {0}".format(int((p.linespan(4)[0]  - (numeroLinea - 1))/2)))
           
def p_operacionesBasicas1(p):
    ''' operacionesBasicas : empty'''
def p_listaValores(p): 
    '''listaValores : tipoValores
                    | ID
                    | listaValores C listaValores'''
def p_listaValores1(p): 
    '''listaValores : empty'''                   
def p_operadoresBasicos(p):
    '''operadoresBasicos : AGREGA
                         | RESTA
                         | MULT
                         | DIV'''
def p_declaraStruct(p):
    '''declaraStruct : ABIDECLARA ID ID PC declaraStruct'''
def p_declaraStruct1(p):
    '''declaraStruct : empty'''
def p_listaInstrucciones(p):
    '''listaInstrucciones :  entradaDatos salidaDatos declaraStruct declaracionVariable operacionesBasicas declaracionIf declaracionCiclo '''
def p_listaInst(p):
    '''listaInst : listaInstrucciones 
                 | listaInstrucciones listaInst '''
def p_listaInst1(p):
    '''listaInst : empty'''
global listaFinal
listaFinal =  []
def p_return(p):
    '''return : RETURN ID PC
              | RETURN PC'''
    global contadorReturn
    
    if(contadorReturn == 0):
        listaReturnFunciones = list(diccionarioFunciones.values())
        global listaFinal
        for elements in listaReturnFunciones:
            if(type(list(elements.values())[0]) == dict  ):
               listaFinal.append(elements)
            else: pass
    global regresoFuncion 
    if(p[2] ==";"):
        regresoFuncion =""
    else:regresoFuncion =p[2]
    
    if(list(listaFinal[contadorReturn].keys())[0] == "VOID"):
        if(regresoFuncion == ""):
            pass
        else: sys.exit("Error semantico en linea {0}".format(int((p.linespan(1)[0]  - (numeroLinea - 1))/2)))
    else: 
        if(list(diccionario[regresoFuncion].keys())[0]==list(listaFinal[contadorReturn].keys())[0]):
            pass
        else: sys.exit("Error semantico en linea {0}".format(int((p.linespan(1)[0]  - (numeroLinea - 1))/2)))
    contadorReturn +=1
def p_empty(p):
	'''empty :'''
	pass
 
def p_error(p):
    if(p!= None):
        sys.exit("Error de sintaxis en la linea {0}".format(int((p.lineno - (numeroLinea - 1))/2 ) ))
    else: 
        sys.exit("Error de sintaxis, no se encontro main")

fp = codecs.open("pruebas2.txt","r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print(result)