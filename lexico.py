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
t_CHAR_VALOR = r"\"([^\\\"]|\\.)?\""
t_STRING_VALOR = r"\"([^\\\"]|\\.)+\" "
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

diccionario = {}
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
   
    if asignacionSimple == 1:
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
        if tok.type == "NUMERO" or  tok.type == "FLOAT_VALOR" or tok.type == "CHAR_VALOR" or tok.type == "STRING_VALOR" or tok.type == "TRUE" or tok.type == "FALSE":
            valorAuxiliar = str(tok.value)
            if(diccionario.get(llaveAuxiliar) is None):
                diccionario[llaveAuxiliar]={tipoAuxiliar:valorAuxiliar}
                asignacionSimple = 0
            else:  sys.exit("Repeticion de declaracion con nombre {0} en linea {1}".format(llaveAuxiliar, int((numeroLinea/2)+1)))
        if tok.type == "C" or  tok.type == "PARENTC":
            diccionarioFunciones[llaveAuxiliar]={tipoAuxiliar:"NULL"} 
            asignacionSimple = 0
    elif reasigna == 1 and tok.type != "ASIG" :
        if tok.type == "PC":
          lista = list(diccionario[llaveAuxiliar].keys())
          if(valorReasignar!=""):
            diccionario[llaveAuxiliar]={lista[0]:valorReasignar}
          valorReasignar= ""
          reasigna = 0
        if tok.type == "P":
            valorReasignar= ""
            reasigna = 0
        if tok.type == "PARENTC":
            valorReasignar =""
            reasigna = 0
        if(reasigna != 0):
            valorReasignar = valorReasignar + str(tok.value)
        else: valorReasignar =""
    elif asignacionArreglo == 1:
        if (tok.type == "INT" or tok.type == "CHAR"  or tok.type == "STRING"  or tok.type == "FLOAT"  or tok.type == "BOOL"):
            tipoAuxiliar = str(tok.type)
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
        if tok.type == "NUMERO":
            sizeArray = str(tok.value)
            diccionario[llaveAuxiliar]={tipoAuxiliar:sizeArray}
            asignacionArreglo = 0
    elif asignacionEstructura == 1:
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
            diccionario[llaveAuxiliar]={"ESTRUCTURA":"NULL"}
            asignacionEstructura = 0
    elif declaraEstructura == 1:
        if tok.type == "ID" and diccionario.get(str(tok.value)) is None:
          llaveAuxiliar = str(tok.value)
          diccionario[llaveAuxiliar]={tipoAuxiliar:"NUEVAESTRUCTURA"}
          declaraEstructura = 0
        if tok.type == "ID":
            tipoAuxiliar = str(tok.value)
    elif tok.type == "ID" :
        llaveAuxiliar = str(tok.value)
        reasigna =1
               
    print(tok.type)
print(diccionario)
print(diccionarioFunciones)