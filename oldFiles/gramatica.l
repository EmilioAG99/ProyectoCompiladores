%{
    #include <string.h>
    int numeroLinea=0;
%}
%option noyywrap
lm [A-Z]
lmin [a-z]
digito [0-9]
parenta "("
parentc ")"
llavea "{"
llavec "}"
cora  "["
corc  "]"
pc ";"
c ","
char  \"([^\\\"]|\\.)?\"
string  \"([^\\\"]|\\.)+\" 
numero {digito}+
id ({lm}|{lmin})({lm}|{lmin}|{digito})*
%%
abijor {printf("abijor \n");}
abif {printf("abif \n");}
abirray {printf("abirray \n");}
abistruct {printf("abistruct \n");}
abiend {printf("abiend \n");}
abimain {printf("abimain \n");}
abin {printf("abin \n");}
about {printf("about \n");}
abiworld {printf("abiword \n");}
"<" {printf("LT \n");}
">" {printf("GT \n");}
"<=" {printf("LET \n");}
">=" {printf("GET \n");}
"!=" {printf("DIFF \n");}
"=="  {printf("comparacion \n");}
"="   {printf("asignacion \n");}
"+"    {printf("agrega \n");}
"++"   {printf("incremento \n");}
"-"    {printf("quita \n");}
"--"   {printf("decremento \n");}
"*"   {printf("* \n");}
"/"   {printf("/ \n");}
"int"   {printf("int \n");}
"Float"  {printf("float \n");}
"Bool"  {printf("bool \n");}
"Char"  {printf("tipo char \n");}
"String" {printf("tipo string \n");}
{char}   {printf("char \n");}
{string}  {printf("string \n");}
else {printf("else \n");}
AND {printf("AND \n");}
return {printf("return \n");}
OR {printf("OR \n");}
{cora} printf("ca \n");
{corc} printf("cc \n");
{id} {printf("identificador \n");}
{parenta} printf("parenA \n");
{parentc} printf("parenC \n");
{llavea} printf("llaveA \n");
{llavec} printf("llaveC \n");
{c}     printf("coma \n");
{numero} {printf("numero \n");}
{pc} {printf("token ; \n");} 
"\n"  { numeroLinea++; }
%%
int main() {
     yyin=fopen("input.txt","r");
     yylex();
}