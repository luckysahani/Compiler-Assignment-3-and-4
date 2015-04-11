#!/usr/bin/env python
#####################################
# lexer.py
# This file tokenize a java file
# namely  identifier | keyword | separator | operator | literal | comment
#####################################

## List of all tokens

#importing libraries
import ply.lex as lex
from ply.lex import TOKEN
import sys

#definations of different regex


code_str = ""
token_str = ""


reserved = {
  'string' : 'STR',
  'abstract' : 'ABSTRACT' ,
  'continue' : 'CONTINUE' , 
  'goto'  : 'GOTO' ,
  'package' : 'PACKAGE' ,
  'switch'  : 'SWITCH' ,
  'assert'  : 'ASSERT' ,
  'default' : 'DEFAULT' ,
  'if'  : 'IF' ,
  'private' : 'PRIVATE' ,
  'this'  : 'THIS' ,
  'boolean' : 'BOOLEAN' ,
  'do'  : 'DO' ,
  'implements'  : 'IMPLEMENTS' ,
  'protected' : 'PROTECTED' ,
  'throw' : 'THROW' ,
  'break' : 'BREAK' ,
  'double' : 'DOUBLE' ,
  'import'  : 'IMPORT' ,
  'public'  : 'PUBLIC' ,
  'throws': 'THROWS' ,
  'byte'  : 'BYTE' ,
  'else'  : 'ELSE' ,
  'instanceof'  : 'INSTANCEOF' ,
  'return'  : 'RETURN' ,
  'transient' : 'TRANSIENT' ,
  'case'  : 'CASE' ,
  'extends' : 'EXTENDS' ,
  'int' : 'INT' ,
  'short' : 'SHORT' ,
  'try' : 'TRY' ,
  'catch' : 'CATCH' ,
  'final' : 'FINAL' ,
  'interface' : 'INTERFACE' ,
  'static'  : 'STATIC' ,
  'void'  : 'VOID' ,
  'char'  : 'CHAR' ,
  'finally' : 'FINALLY' ,
  'long'  : 'LONG' ,
  'strictfp'  :  'STRCITFP' ,
  'volatile'  : 'VOLATILE' ,
  'class' : 'CLASS' ,
  'float' : 'FLOAT' ,
  'native' : 'NATIVE' ,
  'super' : 'SUPER' ,
  'while' : 'WHILE' ,
  'const' : 'CONST' ,
  'for' : 'FOR' ,
  'new' : 'NEW' , 
  'synchronized' : 'SYNCHRONIZED',
  'enum' : 'ENUM'
}


seperator = {
  ':' : 'COLON',
  ';' : 'SEMICOLON',
  ',' : 'COMMA' ,
  '.' : 'DOT' ,
  '(' : 'LROUNPAREN' ,
  ')' : 'RROUNPAREN' ,
  '{' : 'LCURPAREN' ,
  '}' : 'RCURPAREN' ,
  '[' : 'LSQPAREN' ,
  ']' : 'RSQPAREN' 
}

tokens = [ 'WHITESPACE',
           'IDENTIFIER',
           'BOOLEAN_CONST',
           'FLOAT_CONST',
           'INT_CONST',
           'CHAR_CONST',
           'STRING',
           'NULL',
           'KEYWORD',
           'SEPERATOR',
           'OPERATOR',
           'LITERAL',
           'COMMENT','OP_LOR', 'OP_LAND',
        'OP_EQ', 'OP_NE', 'OP_GE', 'OP_LE',
        'OP_SHL', 'OP_SHR', 'OP_SHRR',

        'ASS_MUL', 'ASS_DIV', 'ASS_MOD',
        'ASS_ADD', 'ASS_SUB', 'ASS_SHL', 'ASS_SHR', 'ASS_SHRR',
        'ASS_AND', 'ASS_OR', 'ASS_XOR','QUES',

        'OP_INC', 'OP_DEC', 
        'ELLIPSIS',
        'PLUS',
        'MINUS',
        'AND',
        'EQUAL',
        'LESS',
        'MORE',
        'DIV',
        'MULT',
        'MOD',
        'NOT'

           ] + list(reserved.values()) + list(seperator.values())



## COMMENT REGEX
ml_comment_regex = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
sl_comment_regex = r'(//.*)'
comment_regex = ml_comment_regex + r'|' + sl_comment_regex

## INTEGER REGEX
decimal_regex = r'([1-9]_+[0-9][0-9_]*[0-9][lL]?)' + r'|'+ r'((0)|([1-9][0-9]*)[lL]?)' 
octal_regex = r'0_?[0-7][0-7_]*[0-7][lL]?' +r'|'+  r'0_?([0-7])[lL]?'
hexadecimal_regex = r'(0[xX][0-9a-fA-F][0-9a-fA-F_]*[0-9a-fA-F][lL]?)'+r'|'+'(0[xX][0-9a-fA-F])[lL]?'
binary_regex = r'(0[bB][01][01_]*[01][lL]?)' + r'|' + r'(0[bB][01][lL]?)' 
integer_regex = hexadecimal_regex + r'|' + octal_regex + r'|' + binary_regex + r'|' + decimal_regex

## FLOAT REGEX
digits = r'(([0-9][0-9_]*[0-9])|([0-9]))'
exp_regex = r'([eE][\+\-]?)' + digits
decimalfloat_regex_1 = digits + r'\.' + digits + r'?(' + exp_regex + r')?[fFdD]?' 
decimalfloat_regex_2 = r'\.' + digits + r'(' + exp_regex + r')?[fFdD]?' 
decimalfloat_regex_3 = digits + r'(' + exp_regex + r')[fFdD]?' 
decimalfloat_regex_4 = digits + r'(' + exp_regex + r')?[fFdD]' 
decimalfloat_regex = decimalfloat_regex_1 + r'|' + decimalfloat_regex_2 + r'|' + decimalfloat_regex_3 + r'|' + decimalfloat_regex_4

## CHAR LITERAL REGEX
octal_esc = r"[0-3]?[0-7][0-7]?"
unary_esc = r"u[0-9a-fA-F][0-9a-fA-F][0-9a-fA-F][0-9a-fA-F]"
char_regex = r"\'([^\']|(\\(n|f|r|b|t|\'|\"|\\|"+ octal_esc +"|" + unary_esc + ")))\'"


## STRING LITERAL REGEX
string_regex = r'\"([^\"\\]|(\\(n|f|r|b|t|\'|\"|\\|' + octal_esc + '|' + unary_esc + ')))*\"'

## OTHER LITERALS REGEX
boolean_regex = r'(true)|(false)|(TRUE)|(FALSE)'
null_regex = r'null'

literal_regex = boolean_regex + r'|' + char_regex


#@TOKEN(literal_regex)
#def t_LITERAL(t):
#    return t

@TOKEN(decimalfloat_regex)
def t_FLOAT_CONST(t):
    return t

@TOKEN(integer_regex)
def t_INT_CONST(t):
    return t

@TOKEN(char_regex)
def t_CHAR_CONST(t):
    return t

@TOKEN(string_regex)
def t_STRING(t):
    return t

@TOKEN(boolean_regex)
def t_BOOLEAN_CONST(t):
    return t

@TOKEN(null_regex)
def t_NULL(t):
    return t

def t_WHITESPACE(t):
    r'[ \t\f]'

def t_IDENTIFIER(t):
    r'[a-zA-Z$_][a-zA-Z$_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

@TOKEN(comment_regex)
def t_COMMENT(t):
    a = 1
    # No return value. Token discarded

def t_SEPERATOR(t):
    r'[:;,\.\(\)\{\}\[\]]'
    t.type = seperator.get(t.value,'SEPERATOR')   # Check for seperators
    return t


t_OP_LOR = r'\|\|'
t_OP_LAND = '\&\&'

t_OP_EQ = '=='
t_OP_NE = '!='
t_OP_GE = '>='
t_OP_LE = '<='

t_OP_SHL = '<<'
t_OP_SHR = '>>'
t_OP_SHRR = '>>>'

t_ASS_MUL = r'\*='
t_ASS_DIV = '/='
t_ASS_MOD = '%='
t_ASS_ADD = r'\+='
t_ASS_SUB = '-='
t_ASS_SHL = '<<='
t_ASS_SHR = '>>='
t_ASS_SHRR = '>>>='
t_ASS_AND = '\&='
t_ASS_OR = r'\|='
t_ASS_XOR = '\^='

t_OP_INC = r'\+\+'
t_OP_DEC = r'\-\-'

t_ELLIPSIS = r'\.\.\.'

t_PLUS = '\+'
t_MINUS = '\-'
t_AND = '\&'
t_EQUAL = '='
t_LESS = '<'
t_MORE = '>'
t_DIV = '/'
t_MULT = '\*'
t_MOD = '%'
t_NOT = '!'
t_QUES = '\?'
# def t_OPERATOR(t):
#     r'(>|<|=|\&|\+|\-|\/)'
#     return t

    # def t_OPERATOR(t):
    # r'(>>>=|>>=|<<=|>>|<<|>>>|>=|<=|>|<|==|=|\&\&|\&=|\&|{\+\-\|\&}{2}|[\+\-\*/\&\|\^\%\!]=|[\+\-\*/\&\|\^\%\!\~\?\:])'
    # return t

def t_newline(t):
    r'[\n\r]'
    t.lexer.lineno += len(t.value)
    # global code_str
    # global token_str
    # print code_str + "\t\t//" + token_str
    # code_str = ""
    # token_str = ""

# A string containing ignored characters (spaces and tabs)
#t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1) 

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
#lexer.input("hardik bansal TRUE 0x123  1.00E-05 '.'/* hardik */")

#Tokenize
#lexer.input((open('sample.java','r')).read())
# lexer.input((open(sys.argv[1],'r')).read())

# while True:
#     tok = lexer.token()
#     if not tok: break      
#    # print tok
#     code_str += tok.value
#     if(tok.type != "WHITESPACE"):
#         token_str += tok.type + " "


