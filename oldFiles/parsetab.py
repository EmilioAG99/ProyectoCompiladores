
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABIDECLARA ABIF ABIJOR ABIMAIN ABIN ABIRRAY ABISTRUCT ABIWORLD ABOUT AGREGA AND ASIG BOOL C CHAR CHAR_VALOR COMP CORA CORC DECREMENTO DIV ELSE FALSE FLOAT FLOAT_VALOR GT GTE ID INCREMENTO INT LLAVEA LLAVEC LT LTE MULT NE NOT NUMERO OR P PARENTA PARENTC PC RESTA RETURN STRING STRING_VALOR TRUE VOID start : variablesGlobales declaracionEstructuras declaracionFuncion declaraMain variablesGlobales : ABIWORLD declaracionVariable PC variablesGlobalesvariablesGlobales : emptydeclaracionVariable : tipoDatos ID ASIG tipoValores \n                           | declaracionArreglo declaracionVariable : declaracionVariable C declaracionVariabledeclaracionVariable : emptytipoDatos : INT\n                 | CHAR\n                 | STRING\n                 | BOOL\n                 | FLOAT\n                 | VOID\n                 tipoValores : NUMERO\n                   | FLOAT_VALOR\n                   | CHAR_VALOR\n                   | STRING_VALOR\n                   | TRUE\n                   | FALSE declaracionArreglo : ABIRRAY tipoDatos ID ASIG CORA NUMERO CORC\n                           | ABIRRAY tipoDatos ID ASIG CORA NUMERO CORC CORA NUMERO CORC\n                           | ABIRRAY tipoDatos ID  declaracionEstructuras : ABISTRUCT ID LLAVEA declaracionVariable LLAVEC PC declaracionEstructuras declaracionEstructuras : emptydeclaracionFuncion : tipoDatos ID PARENTA declaracionParametros PARENTC LLAVEA listaInst return LLAVEC declaracionFunciondeclaracionFuncion : emptydeclaracionParametros : tipoDatos IDdeclaracionParametros : declaracionParametros C declaracionParametrosdeclaracionParametros : emptydeclaraMain : ABIMAIN LLAVEA listaInst LLAVECdeclaracionCiclo : ABIJOR PARENTA inicializacion PC cond PC cambio PARENTC LLAVEA listaInst LLAVEC  declaracionCiclodeclaracionCiclo : empty inicializacion : INT ID ASIG NUMERO\n                      | ID ASIG NUMEROcond : ID operadores ID\n            | ID operadores NUMERO  operadores : LT\n                   | LTE\n                   | GTE\n                   | GTcambio :  ID ASIG ID AGREGA ID\n              |  ID ASIG ID RESTA ID \n              |  ID ASIG ID AGREGA NUMERO\n              |  ID ASIG ID RESTA NUMERO \n              |  ID INCREMENTO\n              |  ID DECREMENTOdeclaracionIf : ABIF  PARENTA condicion PARENTC LLAVEA  listaInst LLAVEC declaracionElse declaracionIf\n                     | ABIF  PARENTA condicion PARENTC LLAVEA  listaInst LLAVEC declaracionIf\n                    declaracionIf : empty\n                    declaracionElse : ELSE LLAVEA listaInst LLAVEC condicion : ID  operadoresRel ID operadoresLogicos condicion\n                 | ID  operadoresRel ID\n                 | ID  \n                 | tipoValores\n                 | ID  operadoresRel tipoValores operadoresLogicos condicion\n                 | ID  operadoresRel tipoValores  \n                 | NOT ID  operadoresRel ID operadoresLogicos condicion\n                 | NOT ID  operadoresRel ID\n                 | NOT ID  operadoresRel tipoValores operadoresLogicos condicion\n                 | NOT ID  operadoresRel tipoValores \n                 | ID  operadoresRel NOT ID operadoresLogicos condicion\n                 | ID  operadoresRel NOT ID\n                 | ID  operadoresRel NOT tipoValores operadoresLogicos condicion\n                 | ID  operadoresRel NOT tipoValores\n                 | NOT PARENTA condicion PARENTC operadoresLogicos : AND\n                         | ORoperadoresRel : LT\n                     | LTE\n                     | GT\n                     | GTE\n                     | NE\n                     | COMPentradaDatos : ABIN PARENTA ID PARENTC PC entradaDatosentradaDatos : empty salidaDatos : ABOUT PARENTA STRING_VALOR PARENTC salidaDatos PC\n                    | ABOUT PARENTA listaSalida PARENTC  salidaDatos PC\n                    | ABOUT PARENTA STRING_VALOR C listaSalida PARENTC PC salidaDatos salidaDatos : emptylistaSalida : ID C listaSalida\n                   | ID operacionesBasicas : ID ASIG ID operadoresBasicos ID PC operacionesBasicas\n                           | ID ASIG tipoValores operadoresBasicos ID PC operacionesBasicas\n                           | ID ASIG tipoValores operadoresBasicos tipoValores PC operacionesBasicas\n                           | ID ASIG ID operadoresBasicos tipoValores PC operacionesBasicas\n                           | ID ASIG tipoValores PC operacionesBasicas\n                           | ID ASIG ID P ID PC operacionesBasicas\n                           | ID ASIG ID PC operacionesBasicas\n                           | ID P ID PC operacionesBasicas\n                           | ID ASIG ID CORA NUMERO CORC PC operacionesBasicas\n                           | ID CORA NUMERO CORC ASIG ID CORA NUMERO CORC PC operacionesBasicas\n                           | ID CORA NUMERO CORC ASIG tipoValores PC operacionesBasicas\n                           | ID PARENTA listaValores PARENTC  PC operacionesBasicas\n                           | ID ASIG ID PARENTA listaValores PARENTC  PC operacionesBasicas operacionesBasicas : emptylistaValores : tipoValores\n                    | ID\n                    | listaValores C listaValoreslistaValores : emptyoperadoresBasicos : AGREGA\n                         | RESTA\n                         | MULT\n                         | DIVdeclaraStruct : ABIDECLARA ID ID PC declaraStructdeclaraStruct : emptylistaInstrucciones :  entradaDatos salidaDatos declaraStruct declaracionVariable operacionesBasicas declaracionIf declaracionCiclo listaInst : listaInstrucciones \n                 | listaInstrucciones listaInst listaInst : emptyreturn : RETURN ID PC\n              | RETURN PCempty :'
    
_lr_action_items = {'ABIWORLD':([0,23,],[3,3,]),'ABISTRUCT':([0,2,4,23,31,65,],[-112,6,-3,-112,-2,6,]),'INT':([0,2,3,4,5,7,10,11,18,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,47,48,49,58,60,64,65,67,69,72,74,75,76,84,86,92,96,98,103,108,109,110,113,114,116,126,127,129,132,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-112,-112,12,-3,12,-24,-5,-7,12,-112,12,12,-2,-6,-22,-112,12,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,12,-112,12,-105,-112,-23,-20,-112,-112,-95,-112,-112,-49,-112,-74,-75,12,-21,-106,-32,-104,-76,-77,154,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'CHAR':([0,2,3,4,5,7,10,11,18,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,47,48,49,58,60,64,65,67,69,72,74,75,76,84,86,92,96,98,103,108,109,110,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-112,-112,13,-3,13,-24,-5,-7,13,-112,13,13,-2,-6,-22,-112,13,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,13,-112,13,-105,-112,-23,-20,-112,-112,-95,-112,-112,-49,-112,-74,-75,13,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'STRING':([0,2,3,4,5,7,10,11,18,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,47,48,49,58,60,64,65,67,69,72,74,75,76,84,86,92,96,98,103,108,109,110,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-112,-112,14,-3,14,-24,-5,-7,14,-112,14,14,-2,-6,-22,-112,14,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,14,-112,14,-105,-112,-23,-20,-112,-112,-95,-112,-112,-49,-112,-74,-75,14,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'BOOL':([0,2,3,4,5,7,10,11,18,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,47,48,49,58,60,64,65,67,69,72,74,75,76,84,86,92,96,98,103,108,109,110,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-112,-112,15,-3,15,-24,-5,-7,15,-112,15,15,-2,-6,-22,-112,15,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,15,-112,15,-105,-112,-23,-20,-112,-112,-95,-112,-112,-49,-112,-74,-75,15,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'FLOAT':([0,2,3,4,5,7,10,11,18,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,47,48,49,58,60,64,65,67,69,72,74,75,76,84,86,92,96,98,103,108,109,110,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-112,-112,16,-3,16,-24,-5,-7,16,-112,16,16,-2,-6,-22,-112,16,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,16,-112,16,-105,-112,-23,-20,-112,-112,-95,-112,-112,-49,-112,-74,-75,16,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'VOID':([0,2,3,4,5,7,10,11,18,23,24,30,31,32,34,35,36,38,39,40,41,42,43,44,47,48,49,58,60,64,65,67,69,72,74,75,76,84,86,92,96,98,103,108,109,110,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-112,-112,17,-3,17,-24,-5,-7,17,-112,17,17,-2,-6,-22,-112,17,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,17,-112,17,-105,-112,-23,-20,-112,-112,-95,-112,-112,-49,-112,-74,-75,17,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'ABIMAIN':([0,2,4,5,7,19,21,23,31,65,74,110,130,],[-112,-112,-3,-112,-24,28,-26,-112,-2,-112,-23,-112,-25,]),'$end':([1,27,56,],[0,-1,-30,]),'ABIRRAY':([3,10,11,24,30,32,34,35,38,39,40,41,42,43,44,47,48,49,58,60,67,69,72,75,76,84,86,92,96,98,103,108,109,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[18,-5,-7,18,18,-6,-22,-112,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,18,-105,-112,-20,-112,-112,-95,-112,-112,-49,-112,-74,-75,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'PC':([3,8,10,11,24,32,34,38,39,40,41,42,43,44,54,60,75,81,87,88,90,94,104,106,111,113,118,119,120,127,128,129,150,152,153,166,167,169,172,173,179,192,193,197,199,202,228,242,243,251,],[-112,23,-5,-7,-112,-6,-22,-4,-14,-15,-16,-17,-18,-19,65,-79,-20,92,103,-112,-112,112,127,129,131,-21,138,147,148,-76,152,-77,177,-112,180,189,190,191,194,195,-78,216,217,221,222,-34,-33,-35,-36,258,]),'C':([3,8,10,11,24,30,32,34,35,36,37,38,39,40,41,42,43,44,47,48,49,52,53,58,60,62,64,67,69,72,73,75,76,78,80,84,86,92,96,98,102,103,108,109,113,114,116,122,123,124,125,126,127,129,138,141,147,148,151,152,168,171,174,175,177,178,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-112,24,-5,-7,-112,-112,24,-22,-112,-112,24,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,64,-29,-112,-79,-27,-112,-112,-105,-112,64,-20,24,89,91,-112,-95,-112,-112,-49,-112,-112,-74,-75,-21,-106,-32,-97,151,-96,-99,-104,-76,-77,-112,-112,-112,-112,-112,-112,-88,151,-86,-89,-112,151,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'ID':([6,9,10,11,12,13,14,15,16,17,20,24,26,32,34,35,38,39,40,41,42,43,44,47,48,49,51,58,60,61,67,68,69,70,72,75,76,77,84,86,89,91,92,94,96,98,99,100,102,103,108,109,113,114,116,117,126,127,129,132,136,137,138,139,141,142,143,144,145,146,147,148,151,152,154,157,158,159,160,161,162,163,165,168,174,175,176,177,179,180,183,186,187,189,190,191,194,195,198,204,205,206,207,213,214,215,216,217,218,219,221,222,223,224,225,226,227,229,232,233,234,235,236,237,239,244,245,253,256,257,258,259,262,264,265,266,267,272,],[22,25,-5,-7,-8,-9,-10,-11,-12,-13,29,-112,34,-6,-22,-112,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,62,-112,-79,71,-112,77,-105,80,-112,-20,85,87,-112,-95,80,80,-112,111,-112,-49,118,120,122,-112,-74,-75,-21,-106,-32,134,-104,-76,-77,155,164,166,85,169,122,-100,-101,-102,-103,172,85,85,122,-112,181,184,-68,-69,-70,-71,-72,-73,134,-88,-86,-89,196,85,-78,200,-112,208,210,85,85,85,85,85,-93,134,-66,-67,134,-82,-85,-87,85,85,-83,-84,85,241,242,-37,-38,-39,-40,-112,134,134,134,134,-90,-94,-92,-112,-48,260,-47,-112,85,-112,-91,268,270,-50,-112,-31,]),'LLAVEC':([10,11,24,30,32,34,35,37,38,39,40,41,42,43,44,46,47,48,49,57,58,60,67,69,75,76,84,86,92,93,96,98,103,108,109,112,113,114,116,126,127,129,131,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,203,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,261,262,263,266,267,272,],[-5,-7,-112,-112,-6,-22,-112,54,-4,-14,-15,-16,-17,-18,-19,56,-107,-75,-112,-108,-112,-79,-112,-105,-20,-112,-112,-95,-112,110,-112,-49,-112,-74,-75,-111,-21,-106,-32,-104,-76,-77,-110,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,229,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,266,-91,267,-50,-112,-31,]),'ABIF':([10,11,24,32,34,35,38,39,40,41,42,43,44,47,48,49,58,60,67,69,72,75,76,84,86,92,96,98,103,108,109,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-5,-7,-112,-6,-22,-112,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,-112,-105,-112,-20,-112,97,-95,-112,-112,-49,-112,-74,-75,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,97,-90,-94,-92,97,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'ABIJOR':([10,11,24,32,34,35,38,39,40,41,42,43,44,47,48,49,58,60,67,69,72,75,76,84,86,92,96,98,103,108,109,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-5,-7,-112,-6,-22,-112,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,-112,-79,-112,-105,-112,-20,-112,-112,-95,-112,115,-49,-112,-74,-75,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,115,-31,]),'ABIN':([10,11,24,32,34,35,38,39,40,41,42,43,44,47,48,49,58,60,67,69,72,75,76,84,86,92,96,98,103,108,109,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-5,-7,-112,-6,-22,50,-4,-14,-15,-16,-17,-18,-19,50,-75,-112,-112,-79,-112,-105,50,-20,-112,-112,-95,50,-112,-49,-112,-74,-75,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,50,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,50,-112,50,-91,-50,-112,-31,]),'ABOUT':([10,11,24,32,34,35,38,39,40,41,42,43,44,47,48,49,58,60,67,69,72,75,76,84,86,88,90,92,96,98,103,108,109,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-5,-7,-112,-6,-22,-112,-4,-14,-15,-16,-17,-18,-19,-112,-75,59,-112,-79,-112,-105,-112,-20,-112,-112,-95,59,59,-112,-112,-49,-112,-74,-75,-21,-106,-32,-104,-76,-77,-112,-112,-112,59,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'ABIDECLARA':([10,11,24,32,34,35,38,39,40,41,42,43,44,47,48,49,58,60,67,69,72,75,76,84,86,92,96,98,103,108,109,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,183,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,257,258,259,262,266,267,272,],[-5,-7,-112,-6,-22,-112,-4,-14,-15,-16,-17,-18,-19,-112,-75,-112,68,-79,-112,-105,-112,-20,-112,-112,-95,-112,-112,-49,68,-74,-75,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-112,-112,-91,-50,-112,-31,]),'RETURN':([10,11,24,32,34,38,39,40,41,42,43,44,47,48,49,57,58,60,67,69,72,75,76,82,84,86,92,96,98,103,108,109,113,114,116,126,127,129,138,147,148,152,168,174,175,177,179,189,190,191,194,195,198,213,214,215,216,217,218,219,221,229,236,237,239,244,245,256,258,262,266,267,272,],[-5,-7,-112,-6,-22,-4,-14,-15,-16,-17,-18,-19,-107,-75,-112,-108,-112,-79,-112,-105,-112,-20,-112,94,-112,-95,-112,-112,-49,-112,-74,-75,-21,-106,-32,-104,-76,-77,-112,-112,-112,-112,-88,-86,-89,-112,-78,-112,-112,-112,-112,-112,-93,-82,-85,-87,-112,-112,-83,-84,-112,-112,-90,-94,-92,-112,-48,-47,-112,-91,-50,-112,-31,]),'LLAVEA':([22,28,63,156,246,252,],[30,35,72,183,257,259,]),'ASIG':([25,34,85,149,155,181,241,],[33,45,99,176,182,201,253,]),'PARENTA':([29,50,59,85,97,115,118,136,],[36,61,70,102,117,132,141,165,]),'NUMERO':([33,55,83,99,101,102,117,137,140,141,142,143,144,145,146,151,157,158,159,160,161,162,163,165,176,182,186,187,201,204,205,206,207,220,223,224,225,226,227,232,233,234,235,264,265,],[39,66,95,39,121,39,39,39,170,39,-100,-101,-102,-103,39,39,39,-68,-69,-70,-71,-72,-73,39,39,202,39,39,228,39,-66,-67,39,238,243,-37,-38,-39,-40,39,39,39,39,269,271,]),'FLOAT_VALOR':([33,99,102,117,137,141,142,143,144,145,146,151,157,158,159,160,161,162,163,165,176,186,187,204,205,206,207,232,233,234,235,],[40,40,40,40,40,40,-100,-101,-102,-103,40,40,40,-68,-69,-70,-71,-72,-73,40,40,40,40,40,-66,-67,40,40,40,40,40,]),'CHAR_VALOR':([33,99,102,117,137,141,142,143,144,145,146,151,157,158,159,160,161,162,163,165,176,186,187,204,205,206,207,232,233,234,235,],[41,41,41,41,41,41,-100,-101,-102,-103,41,41,41,-68,-69,-70,-71,-72,-73,41,41,41,41,41,-66,-67,41,41,41,41,41,]),'STRING_VALOR':([33,70,99,102,117,137,141,142,143,144,145,146,151,157,158,159,160,161,162,163,165,176,186,187,204,205,206,207,232,233,234,235,],[42,78,42,42,42,42,42,-100,-101,-102,-103,42,42,42,-68,-69,-70,-71,-72,-73,42,42,42,42,42,-66,-67,42,42,42,42,42,]),'TRUE':([33,99,102,117,137,141,142,143,144,145,146,151,157,158,159,160,161,162,163,165,176,186,187,204,205,206,207,232,233,234,235,],[43,43,43,43,43,43,-100,-101,-102,-103,43,43,43,-68,-69,-70,-71,-72,-73,43,43,43,43,43,-66,-67,43,43,43,43,43,]),'FALSE':([33,99,102,117,137,141,142,143,144,145,146,151,157,158,159,160,161,162,163,165,176,186,187,204,205,206,207,232,233,234,235,],[44,44,44,44,44,44,-100,-101,-102,-103,44,44,44,-68,-69,-70,-71,-72,-73,44,44,44,44,44,-66,-67,44,44,44,44,44,]),'PARENTC':([36,39,40,41,42,43,44,52,53,62,64,71,73,78,79,80,102,105,107,122,123,124,125,133,134,135,141,151,171,178,184,185,188,208,209,210,211,212,230,231,240,247,248,249,250,254,255,268,269,270,271,],[-112,-14,-15,-16,-17,-18,-19,63,-29,-27,-112,81,-28,88,90,-81,-112,128,-80,-97,150,-96,-99,156,-53,-54,-112,-112,193,-98,-52,-56,212,-62,-64,-58,-60,-65,-51,-55,252,-61,-63,-57,-59,-45,-46,-41,-43,-42,-44,]),'AGREGA':([39,40,41,42,43,44,118,119,260,],[-14,-15,-16,-17,-18,-19,142,142,264,]),'RESTA':([39,40,41,42,43,44,118,119,260,],[-14,-15,-16,-17,-18,-19,143,143,265,]),'MULT':([39,40,41,42,43,44,118,119,],[-14,-15,-16,-17,-18,-19,144,144,]),'DIV':([39,40,41,42,43,44,118,119,],[-14,-15,-16,-17,-18,-19,145,145,]),'AND':([39,40,41,42,43,44,184,185,208,209,210,211,],[-14,-15,-16,-17,-18,-19,205,205,205,205,205,205,]),'OR':([39,40,41,42,43,44,184,185,208,209,210,211,],[-14,-15,-16,-17,-18,-19,206,206,206,206,206,206,]),'CORA':([45,75,85,118,196,],[55,83,101,140,220,]),'CORC':([66,95,121,170,238,],[75,113,149,192,251,]),'P':([85,118,],[100,139,]),'NOT':([117,157,158,159,160,161,162,163,165,204,205,206,207,232,233,234,235,],[136,186,-68,-69,-70,-71,-72,-73,136,136,-66,-67,136,136,136,136,136,]),'LT':([134,164,200,],[158,158,224,]),'LTE':([134,164,200,],[159,159,225,]),'GT':([134,164,200,],[160,160,227,]),'GTE':([134,164,200,],[161,161,226,]),'NE':([134,164,],[162,162,]),'COMP':([134,164,],[163,163,]),'ELSE':([229,],[246,]),'INCREMENTO':([241,],[254,]),'DECREMENTO':([241,],[255,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'variablesGlobales':([0,23,],[2,31,]),'empty':([0,2,3,5,23,24,30,35,36,47,49,58,64,65,67,72,76,84,88,90,92,96,102,103,110,138,141,147,148,151,152,177,183,189,190,191,194,195,216,217,221,229,244,257,258,259,267,],[4,7,11,21,4,11,11,48,53,48,60,69,53,7,11,48,86,98,60,60,109,116,125,69,21,86,125,86,86,125,60,86,48,86,86,86,86,86,86,86,86,98,98,48,86,48,116,]),'declaracionEstructuras':([2,65,],[5,74,]),'declaracionVariable':([3,24,30,67,],[8,32,37,76,]),'tipoDatos':([3,5,18,24,30,36,64,67,110,],[9,20,26,9,9,51,51,9,20,]),'declaracionArreglo':([3,24,30,67,],[10,10,10,10,]),'declaracionFuncion':([5,110,],[19,130,]),'declaraMain':([19,],[27,]),'tipoValores':([33,99,102,117,137,141,146,151,157,165,176,186,187,204,207,232,233,234,235,],[38,119,124,135,167,124,173,124,185,135,197,209,211,135,135,135,135,135,135,]),'listaInst':([35,47,72,183,257,259,],[46,57,82,203,261,263,]),'listaInstrucciones':([35,47,72,183,257,259,],[47,47,47,47,47,47,]),'entradaDatos':([35,47,72,92,183,257,259,],[49,49,49,108,49,49,49,]),'declaracionParametros':([36,64,],[52,73,]),'salidaDatos':([49,88,90,152,],[58,104,106,179,]),'declaraStruct':([58,103,],[67,126,]),'listaSalida':([70,89,91,],[79,105,107,]),'operacionesBasicas':([76,138,147,148,177,189,190,191,194,195,216,217,221,258,],[84,168,174,175,198,213,214,215,218,219,236,237,239,262,]),'return':([82,],[93,]),'declaracionIf':([84,229,244,],[96,245,256,]),'declaracionCiclo':([96,267,],[114,272,]),'listaValores':([102,141,151,],[123,171,178,]),'condicion':([117,165,204,207,232,233,234,235,],[133,188,230,231,247,248,249,250,]),'operadoresBasicos':([118,119,],[137,146,]),'inicializacion':([132,],[153,]),'operadoresRel':([134,164,],[157,187,]),'cond':([180,],[199,]),'operadoresLogicos':([184,185,208,209,210,211,],[204,207,232,233,234,235,]),'operadores':([200,],[223,]),'cambio':([222,],[240,]),'declaracionElse':([229,],[244,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> variablesGlobales declaracionEstructuras declaracionFuncion declaraMain','start',4,'p_programa','sintactico.py',19),
  ('variablesGlobales -> ABIWORLD declaracionVariable PC variablesGlobales','variablesGlobales',4,'p_variablesGlobales','sintactico.py',22),
  ('variablesGlobales -> empty','variablesGlobales',1,'p_variablesGlobales2','sintactico.py',25),
  ('declaracionVariable -> tipoDatos ID ASIG tipoValores','declaracionVariable',4,'p_declaracionVariable','sintactico.py',27),
  ('declaracionVariable -> declaracionArreglo','declaracionVariable',1,'p_declaracionVariable','sintactico.py',28),
  ('declaracionVariable -> declaracionVariable C declaracionVariable','declaracionVariable',3,'p_declaracionVariable1','sintactico.py',31),
  ('declaracionVariable -> empty','declaracionVariable',1,'p_declaracionVariable2','sintactico.py',34),
  ('tipoDatos -> INT','tipoDatos',1,'p_tipoDatos','sintactico.py',36),
  ('tipoDatos -> CHAR','tipoDatos',1,'p_tipoDatos','sintactico.py',37),
  ('tipoDatos -> STRING','tipoDatos',1,'p_tipoDatos','sintactico.py',38),
  ('tipoDatos -> BOOL','tipoDatos',1,'p_tipoDatos','sintactico.py',39),
  ('tipoDatos -> FLOAT','tipoDatos',1,'p_tipoDatos','sintactico.py',40),
  ('tipoDatos -> VOID','tipoDatos',1,'p_tipoDatos','sintactico.py',41),
  ('tipoValores -> NUMERO','tipoValores',1,'p_tipoValores','sintactico.py',44),
  ('tipoValores -> FLOAT_VALOR','tipoValores',1,'p_tipoValores','sintactico.py',45),
  ('tipoValores -> CHAR_VALOR','tipoValores',1,'p_tipoValores','sintactico.py',46),
  ('tipoValores -> STRING_VALOR','tipoValores',1,'p_tipoValores','sintactico.py',47),
  ('tipoValores -> TRUE','tipoValores',1,'p_tipoValores','sintactico.py',48),
  ('tipoValores -> FALSE','tipoValores',1,'p_tipoValores','sintactico.py',49),
  ('declaracionArreglo -> ABIRRAY tipoDatos ID ASIG CORA NUMERO CORC','declaracionArreglo',7,'p_declaracionArreglo','sintactico.py',52),
  ('declaracionArreglo -> ABIRRAY tipoDatos ID ASIG CORA NUMERO CORC CORA NUMERO CORC','declaracionArreglo',10,'p_declaracionArreglo','sintactico.py',53),
  ('declaracionArreglo -> ABIRRAY tipoDatos ID','declaracionArreglo',3,'p_declaracionArreglo','sintactico.py',54),
  ('declaracionEstructuras -> ABISTRUCT ID LLAVEA declaracionVariable LLAVEC PC declaracionEstructuras','declaracionEstructuras',7,'p_declaracionEstructuras','sintactico.py',57),
  ('declaracionEstructuras -> empty','declaracionEstructuras',1,'p_declaracionEstructuras1','sintactico.py',60),
  ('declaracionFuncion -> tipoDatos ID PARENTA declaracionParametros PARENTC LLAVEA listaInst return LLAVEC declaracionFuncion','declaracionFuncion',10,'p_declaracionFuncion','sintactico.py',62),
  ('declaracionFuncion -> empty','declaracionFuncion',1,'p_declaracionFuncion1','sintactico.py',68),
  ('declaracionParametros -> tipoDatos ID','declaracionParametros',2,'p_declaracionParametros','sintactico.py',70),
  ('declaracionParametros -> declaracionParametros C declaracionParametros','declaracionParametros',3,'p_declaracionParametros1','sintactico.py',73),
  ('declaracionParametros -> empty','declaracionParametros',1,'p_declaracionParametros2','sintactico.py',76),
  ('declaraMain -> ABIMAIN LLAVEA listaInst LLAVEC','declaraMain',4,'p_declaraMain','sintactico.py',78),
  ('declaracionCiclo -> ABIJOR PARENTA inicializacion PC cond PC cambio PARENTC LLAVEA listaInst LLAVEC declaracionCiclo','declaracionCiclo',12,'p_declaracionCiclo','sintactico.py',81),
  ('declaracionCiclo -> empty','declaracionCiclo',1,'p_declaracionCiclo1','sintactico.py',84),
  ('inicializacion -> INT ID ASIG NUMERO','inicializacion',4,'p_inicalizacion','sintactico.py',86),
  ('inicializacion -> ID ASIG NUMERO','inicializacion',3,'p_inicalizacion','sintactico.py',87),
  ('cond -> ID operadores ID','cond',3,'p_cond','sintactico.py',89),
  ('cond -> ID operadores NUMERO','cond',3,'p_cond','sintactico.py',90),
  ('operadores -> LT','operadores',1,'p_operadores','sintactico.py',92),
  ('operadores -> LTE','operadores',1,'p_operadores','sintactico.py',93),
  ('operadores -> GTE','operadores',1,'p_operadores','sintactico.py',94),
  ('operadores -> GT','operadores',1,'p_operadores','sintactico.py',95),
  ('cambio -> ID ASIG ID AGREGA ID','cambio',5,'p_cambio','sintactico.py',97),
  ('cambio -> ID ASIG ID RESTA ID','cambio',5,'p_cambio','sintactico.py',98),
  ('cambio -> ID ASIG ID AGREGA NUMERO','cambio',5,'p_cambio','sintactico.py',99),
  ('cambio -> ID ASIG ID RESTA NUMERO','cambio',5,'p_cambio','sintactico.py',100),
  ('cambio -> ID INCREMENTO','cambio',2,'p_cambio','sintactico.py',101),
  ('cambio -> ID DECREMENTO','cambio',2,'p_cambio','sintactico.py',102),
  ('declaracionIf -> ABIF PARENTA condicion PARENTC LLAVEA listaInst LLAVEC declaracionElse declaracionIf','declaracionIf',9,'p_declaracionIf','sintactico.py',104),
  ('declaracionIf -> ABIF PARENTA condicion PARENTC LLAVEA listaInst LLAVEC declaracionIf','declaracionIf',8,'p_declaracionIf','sintactico.py',105),
  ('declaracionIf -> empty','declaracionIf',1,'p_declaracionIf1','sintactico.py',109),
  ('declaracionElse -> ELSE LLAVEA listaInst LLAVEC','declaracionElse',4,'p_declaracionElse','sintactico.py',112),
  ('condicion -> ID operadoresRel ID operadoresLogicos condicion','condicion',5,'p_condicion','sintactico.py',115),
  ('condicion -> ID operadoresRel ID','condicion',3,'p_condicion','sintactico.py',116),
  ('condicion -> ID','condicion',1,'p_condicion','sintactico.py',117),
  ('condicion -> tipoValores','condicion',1,'p_condicion','sintactico.py',118),
  ('condicion -> ID operadoresRel tipoValores operadoresLogicos condicion','condicion',5,'p_condicion','sintactico.py',119),
  ('condicion -> ID operadoresRel tipoValores','condicion',3,'p_condicion','sintactico.py',120),
  ('condicion -> NOT ID operadoresRel ID operadoresLogicos condicion','condicion',6,'p_condicion','sintactico.py',121),
  ('condicion -> NOT ID operadoresRel ID','condicion',4,'p_condicion','sintactico.py',122),
  ('condicion -> NOT ID operadoresRel tipoValores operadoresLogicos condicion','condicion',6,'p_condicion','sintactico.py',123),
  ('condicion -> NOT ID operadoresRel tipoValores','condicion',4,'p_condicion','sintactico.py',124),
  ('condicion -> ID operadoresRel NOT ID operadoresLogicos condicion','condicion',6,'p_condicion','sintactico.py',125),
  ('condicion -> ID operadoresRel NOT ID','condicion',4,'p_condicion','sintactico.py',126),
  ('condicion -> ID operadoresRel NOT tipoValores operadoresLogicos condicion','condicion',6,'p_condicion','sintactico.py',127),
  ('condicion -> ID operadoresRel NOT tipoValores','condicion',4,'p_condicion','sintactico.py',128),
  ('condicion -> NOT PARENTA condicion PARENTC','condicion',4,'p_condicion','sintactico.py',129),
  ('operadoresLogicos -> AND','operadoresLogicos',1,'p_operadoresLogicos','sintactico.py',131),
  ('operadoresLogicos -> OR','operadoresLogicos',1,'p_operadoresLogicos','sintactico.py',132),
  ('operadoresRel -> LT','operadoresRel',1,'p_operadoresRel','sintactico.py',134),
  ('operadoresRel -> LTE','operadoresRel',1,'p_operadoresRel','sintactico.py',135),
  ('operadoresRel -> GT','operadoresRel',1,'p_operadoresRel','sintactico.py',136),
  ('operadoresRel -> GTE','operadoresRel',1,'p_operadoresRel','sintactico.py',137),
  ('operadoresRel -> NE','operadoresRel',1,'p_operadoresRel','sintactico.py',138),
  ('operadoresRel -> COMP','operadoresRel',1,'p_operadoresRel','sintactico.py',139),
  ('entradaDatos -> ABIN PARENTA ID PARENTC PC entradaDatos','entradaDatos',6,'p_entradaDatos','sintactico.py',141),
  ('entradaDatos -> empty','entradaDatos',1,'p_entradaDatos1','sintactico.py',143),
  ('salidaDatos -> ABOUT PARENTA STRING_VALOR PARENTC salidaDatos PC','salidaDatos',6,'p_salidaDatos','sintactico.py',145),
  ('salidaDatos -> ABOUT PARENTA listaSalida PARENTC salidaDatos PC','salidaDatos',6,'p_salidaDatos','sintactico.py',146),
  ('salidaDatos -> ABOUT PARENTA STRING_VALOR C listaSalida PARENTC PC salidaDatos','salidaDatos',8,'p_salidaDatos','sintactico.py',147),
  ('salidaDatos -> empty','salidaDatos',1,'p_salidaDatos1','sintactico.py',149),
  ('listaSalida -> ID C listaSalida','listaSalida',3,'p_listaSalida','sintactico.py',151),
  ('listaSalida -> ID','listaSalida',1,'p_listaSalida','sintactico.py',152),
  ('operacionesBasicas -> ID ASIG ID operadoresBasicos ID PC operacionesBasicas','operacionesBasicas',7,'p_operacionesBasicas','sintactico.py',155),
  ('operacionesBasicas -> ID ASIG tipoValores operadoresBasicos ID PC operacionesBasicas','operacionesBasicas',7,'p_operacionesBasicas','sintactico.py',156),
  ('operacionesBasicas -> ID ASIG tipoValores operadoresBasicos tipoValores PC operacionesBasicas','operacionesBasicas',7,'p_operacionesBasicas','sintactico.py',157),
  ('operacionesBasicas -> ID ASIG ID operadoresBasicos tipoValores PC operacionesBasicas','operacionesBasicas',7,'p_operacionesBasicas','sintactico.py',158),
  ('operacionesBasicas -> ID ASIG tipoValores PC operacionesBasicas','operacionesBasicas',5,'p_operacionesBasicas','sintactico.py',159),
  ('operacionesBasicas -> ID ASIG ID P ID PC operacionesBasicas','operacionesBasicas',7,'p_operacionesBasicas','sintactico.py',160),
  ('operacionesBasicas -> ID ASIG ID PC operacionesBasicas','operacionesBasicas',5,'p_operacionesBasicas','sintactico.py',161),
  ('operacionesBasicas -> ID P ID PC operacionesBasicas','operacionesBasicas',5,'p_operacionesBasicas','sintactico.py',162),
  ('operacionesBasicas -> ID ASIG ID CORA NUMERO CORC PC operacionesBasicas','operacionesBasicas',8,'p_operacionesBasicas','sintactico.py',163),
  ('operacionesBasicas -> ID CORA NUMERO CORC ASIG ID CORA NUMERO CORC PC operacionesBasicas','operacionesBasicas',11,'p_operacionesBasicas','sintactico.py',164),
  ('operacionesBasicas -> ID CORA NUMERO CORC ASIG tipoValores PC operacionesBasicas','operacionesBasicas',8,'p_operacionesBasicas','sintactico.py',165),
  ('operacionesBasicas -> ID PARENTA listaValores PARENTC PC operacionesBasicas','operacionesBasicas',6,'p_operacionesBasicas','sintactico.py',166),
  ('operacionesBasicas -> ID ASIG ID PARENTA listaValores PARENTC PC operacionesBasicas','operacionesBasicas',8,'p_operacionesBasicas','sintactico.py',167),
  ('operacionesBasicas -> empty','operacionesBasicas',1,'p_operacionesBasicas1','sintactico.py',185),
  ('listaValores -> tipoValores','listaValores',1,'p_listaValores','sintactico.py',187),
  ('listaValores -> ID','listaValores',1,'p_listaValores','sintactico.py',188),
  ('listaValores -> listaValores C listaValores','listaValores',3,'p_listaValores','sintactico.py',189),
  ('listaValores -> empty','listaValores',1,'p_listaValores1','sintactico.py',191),
  ('operadoresBasicos -> AGREGA','operadoresBasicos',1,'p_operadoresBasicos','sintactico.py',193),
  ('operadoresBasicos -> RESTA','operadoresBasicos',1,'p_operadoresBasicos','sintactico.py',194),
  ('operadoresBasicos -> MULT','operadoresBasicos',1,'p_operadoresBasicos','sintactico.py',195),
  ('operadoresBasicos -> DIV','operadoresBasicos',1,'p_operadoresBasicos','sintactico.py',196),
  ('declaraStruct -> ABIDECLARA ID ID PC declaraStruct','declaraStruct',5,'p_declaraStruct','sintactico.py',198),
  ('declaraStruct -> empty','declaraStruct',1,'p_declaraStruct1','sintactico.py',200),
  ('listaInstrucciones -> entradaDatos salidaDatos declaraStruct declaracionVariable operacionesBasicas declaracionIf declaracionCiclo','listaInstrucciones',7,'p_listaInstrucciones','sintactico.py',202),
  ('listaInst -> listaInstrucciones','listaInst',1,'p_listaInst','sintactico.py',204),
  ('listaInst -> listaInstrucciones listaInst','listaInst',2,'p_listaInst','sintactico.py',205),
  ('listaInst -> empty','listaInst',1,'p_listaInst1','sintactico.py',207),
  ('return -> RETURN ID PC','return',3,'p_return','sintactico.py',211),
  ('return -> RETURN PC','return',2,'p_return','sintactico.py',212),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',238),
]