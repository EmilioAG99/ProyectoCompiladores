import ply.lex as lex
import re
import codecs
import os
import sys
global numeroLinea 
numeroLinea = 0
tokens = [ 'PARENTA', 'PARENTC','LLAVEA','LLAVEC', 'CORA','CORC', 
'PC', 'C', 'NUMERO', 'LT', 'GT','LTE','GTE', 'NE','COMP', 'ASIG', 
'AGREGA', 'INCREMENTO','RESTA', 'DECREMENTO', 'MULT', 'DIV', 'ID',"CHAR_VALOR",
"STRING_VALOR", "FLOAT_VALOR", "P"
]
reservadas = {
    "char":"CHAR",
    "string" :"STRING",
    "abijor":"ABIJOR",
    "abif" : "ABIF",
    "abirray":"ABIRRAY",
    "abistruct":"ABISTRUCT",
    "abimain": "ABIMAIN",
    "abin":"ABIN",
    "about": "ABOUT",
    "abiworld": "ABIWORLD",
    "else":"ELSE",
    "int" : "INT",
    "float":"FLOAT",
    "bool":"BOOL",
    "and":"AND",
    "or": "OR",
    "true":"TRUE",
    "false":"FALSE",
    "void" :"VOID",
    "not" : "NOT",
    "return":"RETURN",
    "abideclara":"ABIDECLARA"
}
tokens = list(reservadas.values()) +tokens 

t_ignore = '\t '
t_AGREGA = r'\+'
t_INCREMENTO = r'\+\+'
t_RESTA = r'\-'
t_DECREMENTO = r'\-\-'
t_MULT= r'\*'
t_DIV = r'/'
t_P = r'\.'
t_ASIG = r'='
t_COMP= r'=='
t_NE = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_PARENTA = r'\('
t_PARENTC = r'\)'
t_CORA = r'\['
t_CORC = r'\]'
t_LLAVEA = r'\{'
t_LLAVEC = r'\}'
t_C = r','
t_PC= r';'
t_CHAR_VALOR = r'\'[a-zA-Z]\''
t_STRING_VALOR = r'\"([^\\\"]|\\.)+\"'
def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9]*'
	if t.value.upper() in reservadas.values():
		t.value = t.value.upper()
		t.type = t.value
	return t

def t_NUEVA_LINEA(t):
    r'\n+|\r+| (\r\n)+'
    t.lexer.lineno += len(t.value)
    global numeroLinea 
    numeroLinea +=1
    
def t_FLOAT_VALOR(t):
	r'[-]?(\d)+\.(\d+)'
	t.value = float(t.value)
	return t

def t_NUMERO(t):
	r'(\d)+'
	t.value = int(t.value)
	return t


def t_error (t):
    print ("caracter ilegal '%s'" % t.value[0])
    if not t: return
    t.lexer.skip(1)


archivo = './pruebas2.txt'
fp = codecs.open(archivo,'r','utf-8')
cadena  = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)
asignacionSimple = 0
asignacionArreglo = 0
asignacionEstructura = 0
reasigna=0
declaraEstructura = 0
bandFunciones = 0
llaveAuxiliar = ""
valorAuxiliar = ""
tipoAuxiliar =""
sizeArray = ""
valorReasignar =""
diccionario = {}
diccionarioFunciones ={}
while True:
    tok = analizador.token()
    if not tok : 
        break 
    else : 
        if (tok.type == "INT" or tok.type == "CHAR"  or tok.type == "STRING"  or tok.type == "FLOAT"  or tok.type == "BOOL")and asignacionSimple == 0 and  asignacionArreglo == 0:
            asignacionSimple = 1
            tipoAuxiliar = str(tok.type)
        elif tok.type == "ABIRRAY":
            asignacionArreglo = 1
        elif tok.type == "ABIDECLARA":
            declaraEstructura = 1
        elif tok.type == "ABISTRUCT":
            asignacionEstructura =1
        elif (tok.type == "INT" or tok.type == "CHAR"  or tok.type == "STRING"  or tok.type == "FLOAT"  or tok.type == "BOOL" or tok.type=="VOID"):
            tipoAuxiliar = str(tok.type)
   
    if asignacionSimple == 1:
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
        if tok.type == "NUMERO" or  tok.type == "FLOAT_VALOR" or tok.type == "CHAR_VALOR" or tok.type == "STRING_VALOR" or tok.type == "TRUE" or tok.type == "FALSE":
            valorAuxiliar = str(tok.value)
            if(tipoAuxiliar == "INT"):
                if(tok.type=="NUMERO"):
                    if(diccionario.get(llaveAuxiliar) is None):
                        diccionario[llaveAuxiliar]={tipoAuxiliar:{valorAuxiliar:int((numeroLinea/2)+1)}}
                        asignacionSimple = 0
                    else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                else: sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
            if(tipoAuxiliar == "CHAR"):
                if(tok.type=="CHAR_VALOR"):
                    if(diccionario.get(llaveAuxiliar) is None):
                        diccionario[llaveAuxiliar]={tipoAuxiliar:{valorAuxiliar:int((numeroLinea/2)+1)}}
                        asignacionSimple = 0
                    else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                else: 
                    sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
            if(tipoAuxiliar == "FLOAT"):
                if(tok.type=="FLOAT_VALOR"):
                    if(diccionario.get(llaveAuxiliar) is None):
                        diccionario[llaveAuxiliar]={tipoAuxiliar:{valorAuxiliar:int((numeroLinea/2)+1)}}
                        asignacionSimple = 0
                    else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                else: sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
            if(tipoAuxiliar == "STRING"):
                if(tok.type=="STRING_VALOR"):
                    if(diccionario.get(llaveAuxiliar) is None):
                        diccionario[llaveAuxiliar]={tipoAuxiliar:{valorAuxiliar:int((numeroLinea/2)+1)}}
                        asignacionSimple = 0
                    else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                else: sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
            if(tipoAuxiliar == "BOOL"):
                if(tok.type=="TRUE" or tok.type=="FALSE"):
                    if(diccionario.get(llaveAuxiliar) is None):
                        diccionario[llaveAuxiliar]={tipoAuxiliar:{valorAuxiliar:int((numeroLinea/2)+1)}}
                        asignacionSimple = 0
                    else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                else: sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
        if tok.type == "C" or  tok.type == "PARENTC":
            if(diccionarioFunciones.get(llaveAuxiliar) is None):
                diccionarioFunciones[llaveAuxiliar]={tipoAuxiliar:"NULL"} 
                asignacionSimple = 0
            else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
        if tok.type == "PARENTA":
            asignacionSimple = 0
            if(diccionarioFunciones.get(llaveAuxiliar) is None):
                diccionarioFunciones[llaveAuxiliar]={tipoAuxiliar:{"DECLARACIONFUNCION":int((numeroLinea/2)+1)}}
            else:sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
        if(reasigna != 0):
            valorReasignar = valorReasignar + str(tok.value)
    elif reasigna == 1 and tok.type != "ASIG" :
        if tok.type == "PC" :
          if(diccionario.get(llaveAuxiliar) is not None):
            lista = list(diccionario[llaveAuxiliar].keys())
          else:  sys.exit("variable {0} no declarada en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))       
          if  valorReasignar!= "":
            if(lista[0]== "INT"):
                numbers = [int(word) for word in valorReasignar.split() if word.isdigit()]
                if(len(numbers) !=0):
                    if(len(valorReasignar.split("*"))!=1 or len(valorReasignar.split("-"))!=1 or len(valorReasignar.split("+"))!=1 or len(valorReasignar.split("/"))!=1):
                        if (len(numbers)!=2):
                            
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                        else:diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                    else: diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                else: 
                    if(len(valorReasignar.split("."))!=1):
                        tipoVariableR = list(diccionario[llaveAuxiliar].keys())[0]
                        valorR = list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()])
                        if(tipoVariableR ==valorR[0]):
                            diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                        else: 
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))       
                    elif(len(valorReasignar.split("*"))!=1 or len(valorReasignar.split("-"))!=1 or len(valorReasignar.split("+"))!=1 or len(valorReasignar.split("/"))!=1):
                        if(len(valorReasignar.split("*"))!=1):
                            contadorLocal = 0
                            arregloBusqueda = valorReasignar.split("*")
                           
                            for valores in arregloBusqueda:
                                if(diccionario.get(valores.strip()) is not None):
                                   
                                    if(list(diccionario[valores.strip()].keys())[0] == lista[0]):
                                       
                                        contadorLocal+=1
                                    else:  sys.exit("Error semantico variable {0} en linea {1} no esta del mismo tipo".format(valores.strip(), int((numeroLinea/2)+1)))              
                                else: sys.exit(" variable {0} en linea {1} no esta declarada".format(valores.strip(), int((numeroLinea/2)+1)))              
                            if(contadorLocal ==2):
                                diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                            contadorLocal = 0
                        elif(len(valorReasignar.split("-"))!=1):
                            contadorLocal = 0
                            arregloBusqueda = valorReasignar.split("-")
                            
                            for valores in arregloBusqueda:
                                if(diccionario.get(valores.strip()) is not None):
                                  
                                    if(list(diccionario[valores.strip()].keys())[0] == lista[0]):
                                        
                                        contadorLocal+=1
                                    else:  sys.exit("Error semantico variable {0} en linea {1} no esta del mismo tipo".format(valores.strip(), int((numeroLinea/2)+1)))              
                                else: sys.exit(" variable {0} en linea {1} no esta declarada".format(valores.strip(), int((numeroLinea/2)+1)))              
                            if(contadorLocal ==2):
                                diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                            contadorLocal = 0
                        elif(len(valorReasignar.split("+"))!=1):
                            contadorLocal = 0
                            arregloBusqueda = valorReasignar.split("+")
                           
                            for valores in arregloBusqueda:
                                if(diccionario.get(valores.strip()) is not None):
                                    
                                    if(list(diccionario[valores.strip()].keys())[0] == lista[0]):
                                        
                                        contadorLocal+=1
                                    else:  sys.exit("Error semantico variable {0} en linea {1} no esta del mismo tipo".format(valores.strip(), int((numeroLinea/2)+1)))              
                                else: sys.exit(" variable {0} en linea {1} no esta declarada".format(valores.strip(), int((numeroLinea/2)+1)))              
                            if(contadorLocal ==2):
                                diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                            contadorLocal = 0
                        elif(len(valorReasignar.split("/"))!=1):
                            contadorLocal = 0
                            arregloBusqueda = valorReasignar.split("/")
                            
                            for valores in arregloBusqueda:
                                if(diccionario.get(valores.strip()) is not None):
                                    
                                    if(list(diccionario[valores.strip()].keys())[0] == lista[0]):
                                        
                                        contadorLocal+=1
                                    else:  sys.exit("Error semantico variable {0} en linea {1} no esta del mismo tipo".format(valores.strip(), int((numeroLinea/2)+1)))              
                                else: sys.exit(" variable {0} en linea {1} no esta declarada".format(valores.strip(), int((numeroLinea/2)+1)))              
                            if(contadorLocal ==2):
                                diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                            contadorLocal = 0
                    else:
                       if(valorReasignar.strip() in diccionario):
                                if(list(diccionario[valorReasignar.strip()].keys())[0] == list(diccionario[llaveAuxiliar].keys())[0]):
                                    diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                                else:sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))              
                       else:
                           sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))              
                        
            elif (lista[0]== "STRING"):
                if(re.search('\"([^\\\"]|\\.)+\"', valorReasignar)):
                    diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                else:
                     if(len(valorReasignar.split("."))!=1):
                        tipoVariableR = list(diccionario[llaveAuxiliar].keys())[0]
                        valorR = list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()])
                        if(tipoVariableR ==valorR[0]):
                            diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                        else: 
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                     else: 
                            if(valorReasignar.strip() in diccionario):
                                if(list(diccionario[valorReasignar.strip()].keys())[0] == list(diccionario[llaveAuxiliar].keys())[0]):
                                    diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                                else: sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))              
                            else:
                                sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))              
            elif (lista[0]== "CHAR"):
                if(re.search('\"([^\\\"]|\\.)?\"', valorReasignar)):
                    diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                else:
                     if(len(valorReasignar.split("."))!=1):
                        tipoVariableR = list(diccionario[llaveAuxiliar].keys())[0]
                        valorR = list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()])
                        if(tipoVariableR ==valorR[0]):
                            diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                        else: 
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))                     
                     else: 
                         if(valorReasignar.strip() in diccionario):
                            if(list(diccionario[valorReasignar.strip()].keys())[0] == list(diccionario[llaveAuxiliar].keys())[0]):
                                 diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                         else:
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))       
            elif (lista[0]== "FLOAT"):
                numbers = []
                if(len(valorReasignar.split("*"))!=1 or len(valorReasignar.split("-"))!=1 or len(valorReasignar.split("+"))!=1 or len(valorReasignar.split("/"))!=1):
                    for word in valorReasignar.split():
                        if(word!='*'and word!='+'and word!='-' and word!='/'):
                            if(diccionario.get(word) is not None):
                                if(list(diccionario[word].keys())[0] == "FLOAT"):
                                    numbers.append(1)
                                else:
                                      print(list(diccionario[word].keys())[0])
                                      sys.exit("Error semantico en variable {0} en linea {1}".format(word, int((numeroLinea/2)+1)))                                   
                                    
                            else:
                                if re.match('[-]?(\d)+\.(\d+)', word):
                                    numbers.append(float(word))
                                else:
                                     sys.exit("Error, variable {0} en linea {1} no encontrada o tipo de dato incorrecto".format(word, int((numeroLinea/2)+1)))                                   
                if(len(numbers) !=0):
                    if(len(valorReasignar.split("*"))!=1 or len(valorReasignar.split("-"))!=1 or len(valorReasignar.split("+"))!=1 or len(valorReasignar.split("/"))!=1):
                        if (len(numbers)!=2):
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                        else:diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                    else: diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                
                else: 
                    if(len(valorReasignar.split("."))!=1):
                        tipoVariableR = list(diccionario[llaveAuxiliar].keys())[0]
                        valorR = list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()])
                        if(tipoVariableR ==valorR[0]):
                            diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                        else: 
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))       
                    else:
                       if(diccionario[valorReasignar.strip()]):
                                if(list(diccionario[valorReasignar.strip()].keys())[0] == list(diccionario[llaveAuxiliar].keys())[0]):
                                    diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                                else:sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))              
                       else:
                           sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))                              
            elif (lista[0]== "BOOL"):
                if(valorReasignar.strip() == "true" or valorReasignar.strip() == "TRUE" or valorReasignar.strip() == "false"or valorReasignar.strip() == "FALSE"):
                    diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
                else:
                     if(len(valorReasignar.split("."))!=1):
                        tipoVariableR = list(diccionario[llaveAuxiliar].keys())[0]
                        valorR = list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()])
                        if(tipoVariableR ==valorR[0]):
                            diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                        else: 
                            sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
                     else: 
                            
                            if(valorReasignar.strip() in diccionario):
                                if(list(diccionario[valorReasignar.strip()].keys())[0] == list(diccionario[llaveAuxiliar].keys())[0]):
                                    diccionario[llaveAuxiliar]={lista[0]:list(list(diccionario[valorReasignar.split(".")[len(valorReasignar.split("."))-1].strip()].values())[0].keys())[0]}
                                else: sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))              
                            else:
                                sys.exit("Error semantico en variable {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))              
          valorReasignar= ""
          reasigna = 0
        if tok.type == "PARENTC":
            valorReasignar =""
            reasigna = 0
        if tok.type == "PARENTA" and valorReasignar=="":
            if(diccionarioFunciones.get(llaveAuxiliar) is None):
                diccionarioFunciones[llaveAuxiliar]={tipoAuxiliar:{"DECLARACIONFUNCION":int((numeroLinea/2)+1)}}
                valorReasignar =""
                reasigna = 0
            else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
        if(reasigna != 0):
            valorReasignar = valorReasignar + " " +str(tok.value)
        else: valorReasignar =""
    elif asignacionArreglo == 1:
        if (tok.type == "INT" or tok.type == "CHAR"  or tok.type == "STRING"  or tok.type == "FLOAT"  or tok.type == "BOOL"):
            tipoAuxiliar = str(tok.type)
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
        if tok.type == "NUMERO":
            sizeArray = str(tok.value)
            if(diccionario.get(llaveAuxiliar) is None):
                diccionario[llaveAuxiliar]={tipoAuxiliar:sizeArray}
            else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
            asignacionArreglo = 0
    elif asignacionEstructura == 1:
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
            if(diccionario.get(llaveAuxiliar) is None):
                diccionario[llaveAuxiliar]={"ESTRUCTURA":"NULL"}
                asignacionEstructura = 0
            else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
    elif declaraEstructura == 1:
        if tok.type == "ID" and diccionario.get(str(tok.value)) is None:
          llaveAuxiliar = str(tok.value)
          if(diccionario.get(llaveAuxiliar) is None):
            diccionario[llaveAuxiliar]={tipoAuxiliar:"NUEVAESTRUCTURA"}
            declaraEstructura = 0
          else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
        if tok.type == "ID":
            tipoAuxiliar = str(tok.value)
    elif tok.type == "ID" :
        llaveAuxiliar = str(tok.value)
        reasigna =1
        
               
    print(tok.type)
print(diccionario)
print(diccionarioFunciones)