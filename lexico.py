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
reasignacion = 0
llaveAuxiliar = ""
valorAuxiliar = ""
tipoAuxiliar =""
sizeArray = ""
valorReasignar =""
diccionario = {}
while True:
    tok = analizador.token()
    if not tok : 
        break 
    else : 
        if (tok.type == "INT" or tok.type == "CHAR"  or tok.type == "STRING"  or tok.type == "FLOAT"  or tok.type == "BOOL")and asignacionSimple == 0 and  asignacionArreglo == 0:
            asignacionSimple = 1
            tipoAuxiliar = str(tok.type)
            print("se encontro tipo"+ str(tok.type))
        elif tok.type == "ABIRRAY":
            asignacionArreglo = 1
            print("se encontro arreglo"+ str(tok.type))
        elif tok.type == "ABISTRUCT":
            asignacionEstructura =1
    """     elif tok.type == "ID":
            llaveAuxiliar = str(tok.value)
            reasignacion = 1
    if reasignacion == 1 and tok.value !=llaveAuxiliar and tok.type!="ASIG":
        if tok.type == "PARENTA":
             diccionario[llaveAuxiliar]={"FUNCION":valorReasignar}
             reasignacion = 0
        elif tok.type == "PC":
            lista = list(diccionario[llaveAuxiliar].keys())
            tipoDatos = lista[0]
            diccionario[llaveAuxiliar]={tipoDatos:valorReasignar}
            reasignacion = 0
        elif tok.type == "ID": 
            llaveAuxiliar = str(tok.value)
            diccionario[llaveAuxiliar]={"Estructura":"NULO"}
            reasignacion = 0
        valorReasignar = valorReasignar + str(tok.value) """
    if asignacionSimple == 1:
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
            print("nombre de variable "+str(tipoAuxiliar))
        if tok.type == "NUMERO" or  tok.type == "FLOAT_VALOR" or tok.type == "CHAR_VALOR" or tok.type == "STRING_VALOR" or tok.type == "TRUE" or tok.type == "FALSE":
            valorAuxiliar = str(tok.value)
            print("el valor a diccionario es "+ str(tok.value))
            diccionario[llaveAuxiliar]={tipoAuxiliar:valorAuxiliar} 
            print(diccionario)
            asignacionSimple = 0
        if tok.type == "C" or  tok.type == "PARENTC":
            diccionario[llaveAuxiliar]={tipoAuxiliar:"NULL"} 
            print(diccionario)
            asignacionSimple = 0
    if asignacionArreglo == 1:
        if (tok.type == "INT" or tok.type == "CHAR"  or tok.type == "STRING"  or tok.type == "FLOAT"  or tok.type == "BOOL"):
            tipoAuxiliar = str(tok.type)
        if tok.type == "ID":
            llaveAuxiliar = str(tok.value)
        if tok.type == "NUMERO":
            sizeArray = str(tok.value)
            diccionario[llaveAuxiliar]={tipoAuxiliar:sizeArray}
            print(diccionario)
            asignacionArreglo = 0
    print(tok.type)