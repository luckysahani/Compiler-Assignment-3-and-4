#!/usr/bin/env python
import ply.yacc as yacc, sys
import subprocess
import ST2 as SymbolTable
import ThreeAddrCode as ThreeAddrCode
import pprint
from lexer import tokens

###########################
ST = SymbolTable.SymbTbl()
TAC = ThreeAddrCode.threeAddressCode(ST)
tempcount = 0
###########################

#------------------------------------------------------------------------------------
# The grammer rules start here.

def p_CompilationUnit(p):
	''' CompilationUnit : ProgramFile '''
	ST.Printsymbtbl()
	TAC.printTac()
	# pprint.pprint(TAC.code)
	# pprint.pprint(TAC.labels)

def p_OP_DIM(p):
	''' OP_DIM : LSQPAREN RSQPAREN '''

def p_TypeSpecifier(p):
	''' TypeSpecifier : TypeName
	| TypeName Dims '''

	if(len(p) == 2) :
		p[0] = p[1]
	else :
		p[0] = p[1] + '.' + str(p[2])
		# print p[0]

def p_TypeName(p):
	''' TypeName : PrimitiveType
	| QualifiedName '''

	p[0] = p[1]

def p_ClassNameList(p):
	''' ClassNameList : QualifiedName
        | ClassNameList COMMA QualifiedName '''

def p_PrimitiveType(p):
	''' PrimitiveType : BOOLEAN
	| CHAR
	| BYTE
	| SHORT
	| INT
	| LONG
	| FLOAT
	| DOUBLE
	| VOID 
	| STR '''

	p[0] = p[1]
	if(p[1] == 'boolean') :
		p[0] = 'bool'

def p_SemiColons(p):
	''' SemiColons : SEMICOLON
        | SemiColons SEMICOLON '''



def p_ProgramFile(p):
	''' ProgramFile : PackageStatement ImportStatements TypeDeclarations
	| PackageStatement                  TypeDeclarations
	|                  ImportStatements TypeDeclarations
	|                                   TypeDeclarations '''

def p_PackageStatement(p):
	''' PackageStatement : PACKAGE QualifiedName SemiColons '''

def p_TypeDeclarations(p):
	''' TypeDeclarations : TypeDeclarationOptSemi
	| TypeDeclarations TypeDeclarationOptSemi '''

def p_TypeDeclarationOptSemi(p):
	''' TypeDeclarationOptSemi : TypeDeclaration
        | TypeDeclaration SemiColons '''

def p_ImportStatements(p):
	''' ImportStatements : ImportStatement
	| ImportStatements ImportStatement '''

def p_ImportStatement(p):
	''' ImportStatement : IMPORT QualifiedName SemiColons
	| IMPORT QualifiedName DOT MULT SemiColons '''

def p_QualifiedName(p):
	''' QualifiedName : IDENTIFIER
	| QualifiedName DOT IDENTIFIER '''

	p[0] = {}
	if(len(p) == 2) :
		p[0]['Name'] = p[1]
	else :
		p[0]['Name'] = p[1]['Name'] + '.' + p[3]

def p_TypeDeclaration(p):
	''' TypeDeclaration : ClassHeader LCURPAREN FieldDeclarations RCURPAREN
	| ClassHeader LCURPAREN RCURPAREN '''
	ST.Change_scope()

def p_ClassHeader(p):
	''' ClassHeader : Modifiers ClassWord IDENTIFIER
	|           ClassWord IDENTIFIER '''

	if(len(p) == 4):
		p[0] = {'Modifiers' : p[1], 'ClassName' : p[3]}
	else :
		p[0] = {'Modifiers' : [], 'ClassName' : p[2]}

	ST.Add_scope(p[0]['ClassName'], 'Class',None)

def p_Modifiers(p):
	''' Modifiers : Modifier
	| Modifiers Modifier '''

	if(len(p) == 2) :
		p[0] = p[1]
	else :
		p[0] = p[1]
		p[0].append(p[2]);

def p_Modifier(p):
	''' Modifier : PUBLIC
	| PRIVATE
	| STATIC
	'''
	p[0] = list(p[1])

def p_ClassWord(p):
	''' ClassWord : CLASS '''

def p_FieldDeclarations(p):
	''' FieldDeclarations : FieldDeclarationOptSemi
		| FieldDeclarations FieldDeclarationOptSemi '''    


def p_FieldDeclarationOptSemi(p):
	''' FieldDeclarationOptSemi : FieldDeclaration
        | FieldDeclaration SemiColons '''

def p_FieldDeclaration(p):
	''' FieldDeclaration : FieldVariableDeclaration SEMICOLON
	| MethodDeclaration
	| ConstructorDeclaration
	| StaticInitializer
        | NonStaticInitializer
        | TypeDeclaration '''


def p_FieldVariableDeclaration(p):
	''' FieldVariableDeclaration : Modifiers TypeSpecifier VariableDeclarators
	|           TypeSpecifier VariableDeclarators '''
	if(len(p) == 3) :
		for var in p[2]['Names']:
			if not ST.Exists_curr_scope(var):
				ST.Add_identifier(var,p[1],-1)
			else :
				print "Variable " + var + " Already Declared"
				raise SyntaxError
	else :
		for var in p[3]['Names']:
			if not ST.Exists_curr_scope(var):
				if(not '.' in p[1]) :
					ST.Add_identifier(var,p[1],-1)
			else :
				print "Variable " + var + " Already Declared"
				raise SyntaxError

def p_VariableDeclarators(p):
	''' VariableDeclarators : VariableDeclarator
	| VariableDeclarators COMMA VariableDeclarator '''

	p[0] = {}
	p[0]['Type'] = p[-1]
	if len(p) == 2 :
		p[0]['Names'] = [p[1]['Name']]
		if(p[1].has_key('List2')) :
			p[0]['List2'] = p[1]['List2']
	else:
		p[0]['Names'] = p[1]['Names']
		p[0]['Names'].append(p[3]['Name'])

def p_VariableDeclarator(p):
	''' VariableDeclarator : DeclaratorName
	| DeclaratorName EQUAL VariableInitializer '''

	p[0] = {}
	p[0]['Name'] = p[1]['Name']

	if(p[-1] == ",") :
		p[0]['Type'] = p[-2]['Type']
	else :
		p[0]['Type'] = p[-1]

	if(len(p) == 4):
		if(p[0]['Type'] == p[3]['Type']) :
			if (not '.' in p[0]['Type']) :
				TAC.emit(p[0]['Name'],p[3]['Name'],'','=')
			else :
				p[0]['List2'] = p[3]['List2']
				TAC.emit(p[0]['Name'],p[3]['Name'],'','ALLOC')
		else:
			print "Error in VariableDeclarator of type of " + p[0]['Name']
			raise Exception

def p_VariableInitializer(p):
	''' VariableInitializer : Expression '''
	p[0] = p[1]


def p_MethodDeclaration(p):
	''' MethodDeclaration : Modifiers TypeSpecifier MethodDeclarator MethodBody
	|           TypeSpecifier MethodDeclarator MethodBody '''

	if(len(p) == 5):
		p[0] = {'Modifiers' : p[1], 'Type' : p[2], 'Name' : p[3]['Name'], 'ParamList' : p[3]['List']}
	else :
		p[0] = {'Modifiers' : {'NULL'}, 'Type' : p[1], 'Name' : p[2]['Name'], 'ParamList' : p[2]['List']}

	TAC.emit('','','','Endfunction')
	TAC.code[ST.curr_funcname][0][0] = ST.mainsymbtbl[ST.curr_funcname]['offset']
	ST.mainsymbtbl[ST.curr_funcname]['Parameters'] = p[0]['ParamList']
	ST.Change_scope()

def p_MethodDeclarator(p):
	''' MethodDeclarator : DeclaratorName LROUNPAREN ParameterList RROUNPAREN
	| DeclaratorName LROUNPAREN RROUNPAREN '''

	
	if(len(p) == 5) :
		p[0] = {'Name' : p[1]['Name'], 'List' : p[3]}
		TAC.genNewTacFunc(ST.Add_scope(p[0]['Name'], 'Function',p[-1]))
		TAC.emit('','','','BeginFunction')
		for param in p[3]:
			ST.Add_identifier(param['Name'],param['Type'],-1)
	else :
		p[0] = {'Name' : p[1]['Name'], 'List' : []}
		TAC.genNewTacFunc(ST.Add_scope(p[0]['Name'], 'Function',p[-1]))
		TAC.emit('','','','BeginFunction')



def p_ParameterList(p):
	''' ParameterList : Parameter
	| ParameterList COMMA Parameter '''

	if(len(p) == 2) :
		p[0] = [p[1]]
	else :
		p[0] = p[1]
		p[0].append(p[3])
	
def p_Parameter(p):
	''' Parameter : TypeSpecifier DeclaratorName '''
	p[0] = {'Type' : p[1], 'Name' : p[2]['Name']}

def p_DeclaratorName(p):
	''' DeclaratorName : IDENTIFIER
	| DeclaratorName OP_DIM '''
	p[0] = {}
	if(len(p) == 2):
		p[0]['Name'] = p[1]

def p_MethodBody(p):
	''' MethodBody : LCURPAREN LocalVariableDeclarationsAndStatements RCURPAREN
	| LCURPAREN RCURPAREN
	| SEMICOLON '''

	p[0] = p[1]

def p_ConstructorDeclaration(p):
	''' ConstructorDeclaration : Modifiers ConstructorDeclarator        Block
	|           ConstructorDeclarator        Block '''

def p_ConstructorDeclarator(p):
	''' ConstructorDeclarator : IDENTIFIER LROUNPAREN ParameterList RROUNPAREN
	| IDENTIFIER LROUNPAREN RROUNPAREN '''

def p_StaticInitializer(p):
	''' StaticInitializer : STATIC Block '''

def p_NonStaticInitializer(p):
	''' NonStaticInitializer : Block '''

def p_Block(p):
	''' Block : Bl LocalVariableDeclarationsAndStatements Br
	| Bl Br '''

	if(len(p) == 4) :
		p[0] = p[2]
	else :
		p[0] = {}

def p_Bl(p):
	''' Bl : LCURPAREN '''
	ST.Add_scope(ST.Gen_Temp(),'block',None)

def p_Br(p):
	''' Br : RCURPAREN '''
	ST.Change_scope()

def p_LocalVariableDeclarationsAndStatements(p):
	''' LocalVariableDeclarationsAndStatements : LocalVariableDeclarationOrStatement
	| LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement '''

	if(len(p) == 3) :
		p[0] = p[1]
		p[0]['loopEndList'] = TAC.merge(p[1].get('loopEndList', []), p[2].get('loopEndList', []))
		p[0]['loopBeginList'] = TAC.merge(p[1].get('loopBeginList', []), p[2].get('loopBeginList', []))
	else :
		p[0] = p[1]



def p_LocalVariableDeclarationOrStatement(p):
	''' LocalVariableDeclarationOrStatement : LocalVariableDeclarationStatement
	| Statement '''

	p[0] = p[1]

def p_LocalVariableDeclarationStatement(p):
	''' LocalVariableDeclarationStatement : TypeSpecifier VariableDeclarators SEMICOLON '''

	p[0] = {'Type' : p[1], 'Names' : p[2]['Names']}
	for identifier in p[2]['Names']:
		if ST.Exists_curr_scope(identifier) == False:
			if(not '.' in p[1]) :
				ST.Add_identifier(identifier,p[1],-1)
			else :
				ST.Add_identifier(identifier,p[1],p[2]['List2'])
		else :
			print "Variable " + identifier + " Already Declared"
			raise SyntaxError

def p_Statement(p):
	''' Statement : EmptyStatement Mark_quad
	| LabelStatement Mark_quad
	| ExpressionStatement SEMICOLON Mark_quad
	| JumpStatement Mark_quad
	| Block Mark_quad'''

	p[0] = {}
	Next = p[1].get('nextlist', [])
	p[0]['nextlist'] = Next
	
	p[0]['loopEndList'] = p[1].get('loopEndList',[]);
	p[0]['loopBeginList'] = p[1].get('loopBeginList',[]);

def p_Statement_1(p):
	''' Statement :  IterationStatement Mark_quad
					| SelectionStatement Mark_quad '''
	p[0] = {}
	Next = p[1].get('nextlist', [])
	p[0]['nextlist'] = Next
	if(len(p) == 3):
		TAC.backPatch(Next,p[2]['quad'])
	else :
		TAC.backPatch(Next,p[3]['quad'])

	p[0]['loopEndList'] = p[1].get('loopEndList',[]);
	p[0]['loopBeginList'] = p[1].get('loopBeginList',[]);

def p_Mark_quad(p):
	''' Mark_quad : '''
	p[0] = {'quad' : TAC.getNextInstr()}

def p_EmptyStatement(p):
	''' EmptyStatement : SEMICOLON '''

def p_LabelStatement(p):
	''' LabelStatement : IDENTIFIER COLON
        | CASE ConstantExpression COLON
	| DEFAULT COLON '''

def p_ExpressionStatement(p):
	''' ExpressionStatement : Expression '''
	p[0] = p[1]

def p_SelectionStatement(p):
	''' SelectionStatement : If LROUNPAREN Expression RROUNPAREN Mark_if Statement '''
	
	p[0] = {}
	if(p[3]['Type'] == 'bool') :
		p[0]['nextlist'] = p[5].get('falselist',[])
		p[0]['loopEndList'] = p[6].get('loopEndList', [])
		p[0]['loopBeginList'] = p[6].get('loopBeginList',[])
	else :
		print "Expression of if statement is not boolean"
		raise SyntaxError

	ST.Change_scope()

def p_SelectionStatement_2(p):
	''' SelectionStatement : If LROUNPAREN Expression RROUNPAREN Mark_if Statement ELSE Mark_else Statement '''
	p[0] = {}
	if(p[3]['Type'] == 'bool') :
		TAC.backPatch(p[5]['falselist'], p[8]['quad'])
		p[0]['nextlist'] = p[8]['nextlist']
		p[0]['loopEndList'] = p[6].get('loopEndList', [])
		p[0]['loopBeginList'] = p[6].get('loopBeginList',[])
	else :
		print "Expression of if statement is not boolean"
		raise SyntaxError

	ST.Change_scope()


def p_If(p):
	''' If : IF'''
	ST.Add_scope('if' + str(ST.gen_tempnum()), 'if' ,None)

def p_Mark_if(p):
	''' Mark_if : '''
	p[0] = {}
	p[0]['falselist'] = [TAC.getNextInstr()]
	TAC.emit(p[-2]['Name'],'',-1,'COND_GOTO')

def p_Mark_else(p):
	''' Mark_else : '''
	p[0] = {}
	p[0]['nextlist'] = [TAC.getNextInstr()]
	
	TAC.emit('','',-1,'GOTO')
	p[0]['quad'] = TAC.getNextInstr()

def p_IterationStatement_while(p):
	''' IterationStatement : WHILE Mark_quad LROUNPAREN Expression RROUNPAREN Mark_while Statement '''

	p[0] = {}
	p[0]['nextlist'] = []

	if(p[4]['Type'] != 'bool') :
		print "Expression of While statement is not boolean"
		raise SyntaxError

	TAC.backPatch(p[7]['loopBeginList'], p[2]['quad'])
	p[0]['nextlist'] = TAC.merge(p[7].get('loopEndList',[]), p[7].get('nextlist',[]))
	p[0]['nextlist'] = TAC.merge(p[6].get('falselist',[]), p[7].get('loopEndList',[]))



	TAC.emit ('','',TAC.make_label(p[2]['quad']), 'GOTO')


def p_Mark_while(p):
	''' Mark_while : '''

	p[0] = {}
	p[0]['falselist'] = [TAC.getNextInstr()]
	TAC.emit(p[-2]['Name'],'',-1,'COND_GOTO')

def p_IterationStatement_dowhile(p):
	''' IterationStatement : Do Mark_quad Statement WHILE LROUNPAREN Expression Mark_dowhile RROUNPAREN SEMICOLON '''

	if(p[6]['Type'] != 'bool') :
		print "Expression of While statement is not boolean"
		raise SyntaxError

	p[0] = {}
	p[0]['nextlist'] = []

	TAC.backPatch(p[3]['loopBeginList'], p[2]['quad'])
	# p[0]['nextlist'] = TAC.merge(p[7].get('loopEndList',[]), p[7].get('nextlist',[]))
	p[0]['nextlist'] = TAC.merge(p[2].get('falselist',[]), p[3].get('loopEndList',[]))
	TAC.emit (p[6]['Name'],'',TAC.make_label(p[2]['quad']), 'COND_GOTO_TR')


def p_Do(p):
	''' Do : DO '''
	p[0] = {}

def p_Mark_dowhile(p):
	''' Mark_dowhile : '''

	p[0] = {}
	p[0]['falselist'] = [TAC.getNextInstr()]

def p_IterationStatement_for(p):
	''' IterationStatement : Fr LROUNPAREN ForInit ForExpr Mark_for ForIncr RROUNPAREN Mark_quad Statement '''
	p[0] = {}
	p[0]['nextlist'] = []

	if(p[4]['Type'] != 'bool') :
		print "Expression of While statement is not boolean"
		raise SyntaxError

	TAC.backPatch(p[9]['loopBeginList'], p[5]['quad'])
	TAC.backPatch(p[4]['truelist'], p[8]['quad'])
	p[0]['nextlist'] = TAC.merge(p[4].get('falselist',[]), p[9].get('loopEndList',[]))
	TAC.emit ('','',TAC.make_label(p[5]['quad']),'GOTO')
	ST.Change_scope()


def p_Wh(p):
	''' Fr : FOR '''
	ST.Add_scope("for" + str(ST.gen_tempnum()), "for",None)
	tempcount += 1

def p_Mark_for(p):
	''' Mark_for : '''
	TAC.emit('','','','GOTO')
	p[0] = {'quad' : TAC.getNextInstr()}


def p_ForInit(p):
	''' ForInit : ExpressionStatements SEMICOLON 
	| LocalVariableDeclarationStatement 
	| SEMICOLON '''

def p_ForExpr(p):
	''' ForExpr : Mark_quad Expression SEMICOLON
	| Mark_quad SEMICOLON '''
	if(len(p) == 4) :
		p[0] = p[2]
		p[0]['falselist'] = [TAC.getNextInstr()]
		TAC.emit(p[2]['Name'], '', -1, 'COND_GOTO')
		p[0]['truelist'] = [TAC.getNextInstr()]
		p[0]['quad'] = p[1]['quad']

def p_ForIncr(p):
	''' ForIncr : ExpressionStatements  '''
	p[0] = {}
	TAC.emit('','',TAC.make_label(p[-2]['quad']),'GOTO')

def p_ExpressionStatements(p):
	''' ExpressionStatements : ExpressionStatement
	| ExpressionStatements COMMA ExpressionStatement '''

def p_JumpStatement(p):
	''' JumpStatement : BREAK            SEMICOLON '''

	p[0] = {}
	p[0]['loopEndList'] = [TAC.getNextInstr()]
	TAC.emit('','',-1,'GOTO')

def p_JumpStatement_1(p):
	''' JumpStatement : CONTINUE            SEMICOLON '''
	p[0] = {}
	p[0]['loopEndList'] = [TAC.getNextInstr()]
	TAC.emit('','',-1,'GOTO')


def p_JumpStatement_1(p):
	''' JumpStatement : RETURN Expression SEMICOLON
	| RETURN            SEMICOLON '''

	p[0] = {}
	if(len(p) == 4) :
		if(p[2]['Type'] == ST.mainsymbtbl[ST.curr_funcname]['ReturnType']):
			TAC.emit(p[2]['Name'],'','','RETURN')
		else :
			print "Return Type does not match"
			raise SyntaxError
	else :
		TAC.emit('','','','RETURN')
###############
###############

def p_PrimaryExpression(p):
	''' PrimaryExpression : QualifiedName '''
	p[0] = p[1]
	if((not ST.Exists_class(p[1]['Name'])) and ST.mainsymbtbl[ST.curr_class]['identifiers'].has_key(p[1]['Name'])) :
		temp = ST.Gen_Temp()
		TAC.emit(temp,'this',ST.Get_off(p[1]['Name']),'*+=')
		p[0]['Type'] = ST.mainsymbtbl[ST.curr_class]['identifiers'][p[1]['Name']]['Type']
		p[0]['Name'] = temp
	elif(ST.Exists(p[1]['Name']) and ST.Get_attr(p[1]['Name'],'Type') != None) :
		p[0]['Type'] = ST.Get_attr(p[1]['Name'],'Type')

def p_PrimaryExpression_nn(p):
	''' PrimaryExpression : NotJustName '''

	p[0] = p[1]
	if('.' in p[0]['Type'] and p[0].has_key('List')):
		if ST.Get_attr(p[1]['Name'],'Type') == p[0]['Type'] and len(ST.Get_attr(p[1]['Name'],'Arrwidth')) == len (p[1]['List']) :
			temp1 = ST.Get_attr(p[1]['Name'],'Arrwidth')
			numcn = 0
			temp2 = ''
			temp3 = ''
			for numele in  p[1]['List'] :
				if(numcn == 0):
					temp2 = ST.Gen_Temp()
					TAC.emit(temp2,'',p[1]['List'][numcn],'=')
					numcn += 1
				else :
					temp3 = ST.Gen_Temp()
					TAC.emit(temp3,temp1[numcn],temp2,'*')
					temp2 = ST.Gen_Temp()
					TAC.emit(temp2,temp3,p[1]['List'][numcn],'+')
					numcn += 1
			temp = p[1]['Type'].split('.')
			p[0]['Type'] = temp[0]
			p[0]['AType'] = p[1]['Type']
			p[0]['AName'] = p[1]['Name']
			p[0]['Name'] = temp2
			# TAC.emit(p[0]['Name'],p[0]['AName'],temp2,'+*=')
			# print p[1]['Type'] + ' Error'
		else :
			print "Error in Array"
			raise Exception
		# temp = p[1]['Type'].split('.')
		# p[0]['Type'] = temp[0]
		# print p[0]['Type'] + 'Hello'

def p_NotJustName(p):
	''' NotJustName : SpecialName
	| NewAllocationExpression
	| ComplexPrimary '''
	p[0] = p[1]

def p_ComplexPrimary(p):
	''' ComplexPrimary : LROUNPAREN Expression RROUNPAREN
	| ComplexPrimaryNoParenthesis '''
	if(len(p) == 2):
		p[0] = p[1]
	else :
		p[0] = p[2]

def p_ComplexPrimaryNoParenthesis_int(p):
	''' ComplexPrimaryNoParenthesis : INT_CONST '''
	p[0] = {}
	p[0]['Type'] = "int"
	p[0]['Name'] = ST.Gen_Temp()
	p[0]['value']  = p[1]
	# print p[0]['value']
	TAC.emit(p[0]['Name'],p[1],'','=')
	ST.inc_offset(p[0]['Type'])


def p_ComplexPrimaryNoParenthesis_temp(p):
	''' ComplexPrimaryNoParenthesis : FLOAT_CONST '''
	p[0] = {}
	p[0]['Type'] = "float"
	p[0]['Name'] = ST.Gen_Temp()
	TAC.emit(p[0]['Name'],p[1],'','=')
	ST.inc_offset(p[0]['Type'])

def p_ComplexPrimaryNoParenthesis_string(p):
	''' ComplexPrimaryNoParenthesis : STRING '''
	p[0] = {}
	p[0]['Type'] = "string"
	p[0]['Name'] = ST.Gen_Temp()
	ST.Add_string(p[0]['Name'],p[1])
	# ST.inc_offset(p[0]['Type'])


def p_ComplexPrimaryNoParenthesis_char(p):
	''' ComplexPrimaryNoParenthesis : CHAR_CONST '''
	p[0] = {}
	p[0]['Type'] = "char"
	p[0]['Name'] = ST.Gen_Temp()
	ST.Add_string(p[0]['Name'],p[1])
	# ST.inc_offset(p[0]['Type'])


def p_ComplexPrimaryNoParenthesis_bool(p):
	''' ComplexPrimaryNoParenthesis : BOOLEAN_CONST '''
	p[0] = {}
	p[0]['Type'] = "bool"
	p[0]['Name'] = ST.Gen_Temp()
	TAC.emit(p[0]['Name'],p[1],'','=')
	# ST.inc_offset(p[0]['Type'])


def p_ComplexPrimaryNoParenthesis_rem(p):
	''' ComplexPrimaryNoParenthesis : ArrayAccess
	| FieldAccess '''

	p[0] = p[1]

def p_ComplexPrimaryNoParenthesis_met(p): 
	''' ComplexPrimaryNoParenthesis : MethodCall '''
	p[0] = p[1]

def p_ArrayAccess(p):
	''' ArrayAccess : QualifiedName LSQPAREN Expression RSQPAREN '''
	if(p[3]['Type'] != 'int') :
		print "Index type must be integer"
		raise SyntaxError
	else :
		p[0] = {}
		p[0]['Name'] = p[1]['Name']
		if(ST.Exists(p[0]['Name'])) :
			p[0]['Type'] = ST.Get_attr(p[0]['Name'],'Type')
			p[0]['List'] = [p[3]['value']]
			# print p[0]['List']
		else :
			print "Error Array not defined"
			raise SyntaxError


def p_ArrayAccess_1(p):
	''' ArrayAccess : ComplexPrimary LSQPAREN Expression RSQPAREN '''
	if(p[3]['Type'] != 'int') :
		print "Index type must be integer"
		raise SyntaxError
	else :
		p[0] = {}
		p[0]['Name'] = p[1]['Name']
		p[0]['Type'] = p[1]['Type']
		# print p[3]['value']
		# print "Nothing"
		p[0]['List'] = p[1]['List']
		p[0]['List'].append(p[3]['value'])
		# print p[0]['List']



def p_FieldAccess(p):
	''' FieldAccess : NotJustName DOT IDENTIFIER
	| RealPostfixExpression DOT IDENTIFIER
        | QualifiedName DOT THIS
        | QualifiedName DOT CLASS
        | PrimitiveType DOT CLASS '''

def p_MethodCall(p):
	''' MethodCall : MethodAccess LROUNPAREN ArgumentList RROUNPAREN
	| MethodAccess LROUNPAREN RROUNPAREN '''
	p[0] = {}
	p[0]['Name'] = p[1]['Name']
	if(p[0]['Name'] == 'System.out.println') :
		if(len(p) == 5) :
			TAC.emit(p[3][0]['Name'],'',p[3][0]['Type'],'Print')
		else : 
			print ("No argument to print statement")
			raise SyntaxError
	# elif(p[0]['Name'] == 'System.in.')
	else :
		if(ST.mainsymbtbl[ST.curr_class]['Functions'].has_key(p[1]['Name'])) :
			p[0]['Type'] = ST.mainsymbtbl[ST.curr_class]['Functions'][p[1]['Name']]['Type']
			print p[0]['Type']
		else :
			print "No function defined by this name"
			raise SyntaxError
		if(len(p) == 5) :
			if(len(p[3]) != len(ST.mainsymbtbl[ST.curr_class + '.' +p[0]['Name']]['Parameters'])) :
				print "Number of Parameters are not same as defined"
				raise SyntaxError
			numele = 0
			for param in p[3]:
				print param['Type'] + ' Here'
				if(param['Type'] != ST.mainsymbtbl[ST.curr_class + '.' +p[0]['Name']]['Parameters'][numele]['Type']):
					print "Error in type of Parameters"
					raise SyntaxError
				numele += 1
				TAC.emit(param['Name'],'','','PARAM')
		TAC.emit('',numele,ST.curr_class + '.' +p[0]['Name'],'F_CALL')
		TAC.emit('','','','RetAdd')


def p_MethodAccess(p):
	''' MethodAccess : SpecialName '''

def p_MethodAccess(p) :
	''' MethodAccess : QualifiedName '''
	p[0] = p[1]


def p_SpecialName(p):
	''' SpecialName : THIS
	| SUPER
	| NULL '''

def p_ArgumentList(p):
	''' ArgumentList : Expression
	| ArgumentList COMMA Expression '''

	if(len(p) == 2) :
		p[0] = [p[1]]
	else :
		p[0] = p[1]
		p[0].append(p[3])

def p_NewAllocationExpression(p):
	''' NewAllocationExpression : PlainNewAllocationExpression
	| QualifiedName DOT PlainNewAllocationExpression '''
	p[0] = p[1]
	# print p[0]['Type']

def p_PlainNewAllocationExpression(p):
	''' PlainNewAllocationExpression : ArrayAllocationExpression '''
	p[0] = p[1]

def p_PlainNewAllocationExpression_1(p):
	''' PlainNewAllocationExpression : ClassAllocationExpression
    	| ArrayAllocationExpression LCURPAREN RCURPAREN
    	| ClassAllocationExpression LCURPAREN RCURPAREN
    	| ClassAllocationExpression LCURPAREN FieldDeclarations RCURPAREN '''

def p_ClassAllocationExpression(p):
	''' ClassAllocationExpression : NEW TypeName LROUNPAREN ArgumentList RROUNPAREN
	| NEW TypeName LROUNPAREN              RROUNPAREN '''

def p_ArrayAllocationExpression(p):
	''' ArrayAllocationExpression : NEW TypeName DimExprs Dims '''

def p_ArrayAllocationExpression_1(p):
	''' ArrayAllocationExpression : NEW TypeName DimExprs '''
	temp1 = ST.Gen_Temp()
	TAC.emit(temp1,ST.Get_size(p[2]),p[3]['Name'],'*')
	p[0] = {}
	p[0]['Name'] = temp1
	p[0]['Type'] = p[2] + '.' +str(p[3]['level'])
	p[0]['List2'] = p[3]['List2']
	# print p[0]['Type']

def p_ArrayAllocationExpression_2(p):
	''' ArrayAllocationExpression : NEW TypeName Dims '''


def p_DimExprs(p):
	''' DimExprs : DimExpr
	| DimExprs DimExpr '''
	p[0] = {}
	if(len(p) == 2) :
		p[0]['Name'] = ST.Gen_Temp()
		p[0]['level'] = 1
		p[0]['List2'] = [p[1]['value']]
		TAC.emit(p[0]['Name'],p[1]['Name'],'','=')
	else :
		p[0]['Name'] = ST.Gen_Temp()
		p[0]['level'] = p[1]['level'] + 1
		p[0]['List2'] = p[1]['List2']
		p[0]['List2'].append(p[2]['value'])
		TAC.emit(p[0]['Name'],p[1]['Name'],p[2]['Name'],'*')

def p_DimExpr(p):
	''' DimExpr : LSQPAREN Expression RSQPAREN '''
	p[0] = p[2]

def p_Dims(p):
	''' Dims : OP_DIM
	| Dims OP_DIM '''

	if(len(p) == 2) :
		p[0] = 1
	else :
		p[0] = p[1] + 1

def p_PostfixExpression(p):
	''' PostfixExpression : PrimaryExpression
	| RealPostfixExpression '''
	p[0] = p[1]

def p_RealPostfixExpression(p):
	''' RealPostfixExpression : PostfixExpression OP_INC
	| PostfixExpression OP_DEC '''

	TAC.emit(p[1]['Name'],p[1]['Name'],'1',p[2][0])
	p[0] = {}
	p[0]['Name'] = p[1]['Name']
	p[0]['Type'] = p[1]['Type']


def p_UnaryExpression(p):
	''' UnaryExpression : OP_INC UnaryExpression
	| OP_DEC UnaryExpression
	| LogicalUnaryExpression '''
	if(len(p) == 2) :
		p[0] = p[1]
	elif(len == 3) :
		TAC.emit(p[2]['Name'],p[2]['Name'],'1',p[1][0])
		p[0] = {}
		p[0]['Name'] = p[1]['Name']
		p[0]['Type'] = p[1]['Type']


def p_UnaryExpression_1(p):
	''' UnaryExpression : ArithmeticUnaryOperator CastExpression '''
	p[0] = {}
	temp1 = ST.Gen_Temp()
	if (p[1] == '-'):
		TAC.emit(temp1,p[2]['Name'],'-1','*')
	else :
		TAC.emit(temp1,p[2]['Name'],'','=')
	p[0]['Name'] = temp1
	p[0]['Type'] = p[2]['Type']
	ST.inc_offset(p[0]['Type'])

def p_LogicalUnaryExpression(p):
	''' LogicalUnaryExpression : PostfixExpression
	| LogicalUnaryOperator UnaryExpression '''
	if(len(p) == 2) :
		p[0] = p[1]

def p_LogicalUnaryOperator(p):
	''' LogicalUnaryOperator : '~'
	| NOT '''
	p[0] = p[1]

def p_ArithmeticUnaryOperator(p):
	''' ArithmeticUnaryOperator : PLUS
	| MINUS '''
	p[0] = p[1]

def p_CastExpression(p):
	''' CastExpression : UnaryExpression '''
	# | LROUNPAREN PrimitiveTypeExpression RROUNPAREN CastExpression
	# | LROUNPAREN ClassTypeExpression RROUNPAREN CastExpression
	# | LROUNPAREN Expression RROUNPAREN LogicalUnaryExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	if(p[1].has_key('AType')) :
		p[0]['Type'] = p[1]['Type']
		temp1 = ST.Gen_Temp()
		TAC.emit(temp1,p[1]['AName'],'','ADDFETCH')
		temp2 = ST.Gen_Temp()
		TAC.emit(temp2,p[1]['Name'],temp1,'+')
		p[0]['Name'] = ST.Gen_Temp()
		TAC.emit(p[0]['Name'],temp2,'','*=')


def p_PrimitiveTypeExpression(p):
	''' PrimitiveTypeExpression : PrimitiveType
        | PrimitiveType Dims '''

def p_ClassTypeExpression(p):
	''' ClassTypeExpression : QualifiedName Dims '''

def p_MultiplicativeExpression(p):
	''' MultiplicativeExpression : CastExpression
	| MultiplicativeExpression MULT CastExpression
	| MultiplicativeExpression DIV CastExpression
	| MultiplicativeExpression MOD CastExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type']) :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = p[3]['Type']
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type does not match while multiplying";
			raise SyntaxError

def p_AdditiveExpression(p):
	''' AdditiveExpression : MultiplicativeExpression
        | AdditiveExpression PLUS MultiplicativeExpression
	| AdditiveExpression MINUS MultiplicativeExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type']) :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = p[3]['Type']
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type does not match while adding";
			raise SyntaxError

def p_ShiftExpression(p):
	''' ShiftExpression : AdditiveExpression
        | ShiftExpression OP_SHL AdditiveExpression
        | ShiftExpression OP_SHR AdditiveExpression
        | ShiftExpression OP_SHRR AdditiveExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == 'int' and p[3]['Type'] == 'int') :
			temp1 = ST.Gen_Temp()
			p[0]['Type'] = 'int'
			p[0]['Name'] = temp1
			ST.inc_offset(p[0]['Type'])
			TAC.emit(temp1,p[1]['Name'],p[3]['Name'],p[2])
		else :
			print "Shift operator must have int expressions"
			raise SyntaxError

def p_RelationalExpression(p):
	''' RelationalExpression : ShiftExpression
        | RelationalExpression LESS ShiftExpression
	| RelationalExpression MORE ShiftExpression
	| RelationalExpression OP_LE ShiftExpression
	| RelationalExpression OP_GE ShiftExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type']) :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = 'bool'
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type must be same in comparision";
			raise SyntaxError

def p_EqualityExpression(p):
	''' EqualityExpression : RelationalExpression
        | EqualityExpression OP_EQ RelationalExpression
        | EqualityExpression OP_NE RelationalExpression '''
   	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type']) :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = "bool"
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type must be same in comparision";
			raise SyntaxError

def p_AndExpression(p):
	''' AndExpression : EqualityExpression
	| AndExpression '&' EqualityExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type'] and p[1]['Type'] == 'int') :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = 'int'
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type must be int for bitwise operation";
			raise SyntaxError


def p_ExclusiveOrExpression(p):
	''' ExclusiveOrExpression : AndExpression
	| ExclusiveOrExpression '^' AndExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type'] and p[1]['Type'] == 'int') :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = 'int'
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type must be int for bitwise operation";
			raise SyntaxError

def p_InclusiveOrExpression(p):
	''' InclusiveOrExpression : ExclusiveOrExpression
	| InclusiveOrExpression '|' ExclusiveOrExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type'] and p[1]['Type'] == 'int') :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = 'int'
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type must be int for bitwise operation";
			raise SyntaxError

def p_ConditionalAndExpression(p):
	''' ConditionalAndExpression : InclusiveOrExpression
	| ConditionalAndExpression OP_LAND InclusiveOrExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type'] and p[1]['Type'] == 'bool') :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = 'bool'
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type must be bool for logical operation";
			raise SyntaxError

def p_ConditionalOrExpression(p):
	''' ConditionalOrExpression : ConditionalAndExpression
	| ConditionalOrExpression OP_LOR ConditionalAndExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1]['Type'] == p[3]['Type'] and p[1]['Type'] == 'bool') :
			p[0]['Name'] = ST.Gen_Temp()
			p[0]['Type'] = 'bool'
			ST.inc_offset(p[0]['Type'])
			TAC.emit(p[0]['Name'],p[1]['Name'],p[3]['Name'],p[2])
		else:
			print "Type must be bool for logical operation";
			raise SyntaxError

def p_ConditionalExpression(p):
	''' ConditionalExpression : ConditionalOrExpression
	| ConditionalOrExpression Mark_quad Ques Mark_quad Expression Mark_quad Cln Mark_quad ConditionalExpression Mark_quad'''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		p[0]['Type'] = 'int'
		p[0]['Name'] = ST.Gen_Temp()
		TAC.code[ST.curr_funcname][p[2]['quad']][2] = TAC.make_label(p[8]['quad'])
		TAC.code[ST.curr_funcname][p[2]['quad']][0] = p[1]['Name']
		TAC.code[ST.curr_funcname][p[6]['quad']][0] = p[0]['Name']
		TAC.code[ST.curr_funcname][p[6]['quad']][1] = p[5]['Name']
		TAC.code[ST.curr_funcname][p[6]['quad'] + 1][2] = TAC.make_label(p[10]['quad'] + 1)
		TAC.emit(p[0]['Name'],'',p[9]['Name'],'=')

def p_Ques(p):
	''' Ques : QUES '''
	TAC.emit('','','','COND_GOTO')


def p_Cln(p):
	''' Cln : COLON '''
	TAC.emit('','','','=')
	TAC.emit('','','','GOTO')

def p_AssignmentExpression(p):
	''' AssignmentExpression : ConditionalExpression
	| UnaryExpression AssignmentOperator AssignmentExpression '''
	p[0] = {}
	if(len(p) == 2) :
		p[0] = p[1]
	else :
		if(p[1].has_key('AType')) :
			if(p[1]['Type'] == p[3]['Type']):
				p[0]['Type'] = p[3]['Type']
				p[0]['Name'] = p[1]['Name']
				# ST.inc_offset(p[0]['Type'])
				temp1 = ST.Gen_Temp()
				TAC.emit(temp1,p[1]['AName'],'','ADDFETCH')
				temp2 = ST.Gen_Temp()
				TAC.emit(temp2,p[1]['Name'],temp1,'+')
				TAC.emit(temp2,p[3]['Name'],'','*' + p[2])
			else :
				# print 'Hello'
				# print p[1]['Type']
				print "Error in AssignmentExpression"
				raise SyntaxError
		else :
			if(p[1]['Type'] == p[3]['Type']):
				p[0]['Type'] = p[3]['Type']
				p[0]['Name'] = p[1]['Name']
				# ST.inc_offset(p[0]['Type'])
				TAC.emit(p[1]['Name'],p[3]['Name'],'',p[2])
			else :
				print "Error in AssignmentExpression"
				raise SyntaxError

def p_AssignmentOperator(p):
	''' AssignmentOperator : EQUAL
	| ASS_MUL
	| ASS_ADD
	| ASS_SUB '''

	p[0] = p[1]

def p_Expression(p):
	''' Expression : AssignmentExpression '''
	p[0] = p[1]
	# print p[0]['value']


def p_ConstantExpression(p):
	''' ConstantExpression : ConditionalExpression '''

def p_error(p):
	print('error: {}'.format(p))
#---------------------------------------------------------------------------------------------------------

# Set up a logging object
import logging
logging.basicConfig(
	level = logging.DEBUG,
	filename = "parselog.txt",
	filemode = "w",
	format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()


#Building the parser
parser = yacc.yacc(debug=True)

if __name__ == '__main__':
   try:
		f = sys.argv[1]
		data = open(f).read()	
   except EOFError:
   		print 'Error in Parsing'
   if data:
		result = parser.parse(data,debug=log)
		# print result

#-----------------------------------------------------------------------------------------------------

# Convert the parselog to .dot file for graph generation
print("\n")
subprocess.call(['./dotgen.sh'])