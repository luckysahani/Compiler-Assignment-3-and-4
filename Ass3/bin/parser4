#!/usr/bin/env python
import ply.yacc as yacc, sys
import subprocess
from lexer import tokens

#------------------------------------------------------------------------------------
# The grammer rules start here.

def p_CompilationUnit(p):
	''' CompilationUnit : ProgramFile '''

def p_OP_DIM(p):
	''' OP_DIM : LSQPAREN RSQPAREN '''

def p_TypeSpecifier(p):
	''' TypeSpecifier : TypeName
	| TypeName Dims '''

def p_TypeName(p):
	''' TypeName : PrimitiveType
	| QualifiedName '''

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
	| VOID '''

def p_SemiColons(p):
	''' SemiColons : SEMICOLON
        | SemiColons SEMICOLON '''



def p_ProgramFile(p):
	''' ProgramFile : PackageStatement ImportStatements TypeDeclarations
	| PackageStatement ImportStatements
	| PackageStatement                  TypeDeclarations
	|                  ImportStatements TypeDeclarations
	| PackageStatement
	|                  ImportStatements
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

def p_TypeDeclaration(p):
	''' TypeDeclaration : ClassHeader LCURPAREN FieldDeclarations RCURPAREN
	| ClassHeader LCURPAREN RCURPAREN '''

def p_ClassHeader(p):
	''' ClassHeader : Modifiers ClassWord IDENTIFIER Extends Interfaces
	| Modifiers ClassWord IDENTIFIER Extends
	| Modifiers ClassWord IDENTIFIER       Interfaces
	|           ClassWord IDENTIFIER Extends Interfaces
	| Modifiers ClassWord IDENTIFIER
	|           ClassWord IDENTIFIER Extends
	|           ClassWord IDENTIFIER       Interfaces
	|           ClassWord IDENTIFIER '''

def p_Modifiers(p):
	''' Modifiers : Modifier
	| Modifiers Modifier '''

def p_Modifier(p):
	''' Modifier : ABSTRACT
	| FINAL
	| PUBLIC
	| PROTECTED
	| PRIVATE
	| STATIC
	| TRANSIENT
	| VOLATILE
	| NATIVE
	| SYNCHRONIZED '''

def p_ClassWord(p):
	''' ClassWord : CLASS
	| INTERFACE '''

def p_Interfaces(p):
	''' Interfaces : IMPLEMENTS ClassNameList '''

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

def p_VariableDeclarators(p):
	''' VariableDeclarators : VariableDeclarator
	| VariableDeclarators COMMA VariableDeclarator '''

def p_VariableDeclarator(p):
	''' VariableDeclarator : DeclaratorName
	| DeclaratorName EQUAL VariableInitializer '''

def p_VariableInitializer(p):
	''' VariableInitializer : Expression
	| LCURPAREN RCURPAREN
        | LCURPAREN ArrayInitializers RCURPAREN '''

def p_ArrayInitializers(p):
	''' ArrayInitializers : VariableInitializer
	| ArrayInitializers COMMA VariableInitializer
	| ArrayInitializers COMMA '''

def p_MethodDeclaration(p):
	''' MethodDeclaration : Modifiers TypeSpecifier MethodDeclarator Throws MethodBody
	| Modifiers TypeSpecifier MethodDeclarator        MethodBody
	|           TypeSpecifier MethodDeclarator Throws MethodBody
	|           TypeSpecifier MethodDeclarator        MethodBody '''

def p_MethodDeclarator(p):
	''' MethodDeclarator : DeclaratorName LROUNPAREN ParameterList RROUNPAREN
	| DeclaratorName LROUNPAREN RROUNPAREN
	| MethodDeclarator OP_DIM '''

def p_ParameterList(p):
	''' ParameterList : Parameter
	| ParameterList COMMA Parameter '''

def p_Parameter(p):
	''' Parameter : TypeSpecifier DeclaratorName
        | FINAL TypeSpecifier DeclaratorName '''

def p_DeclaratorName(p):
	''' DeclaratorName : IDENTIFIER
        | DeclaratorName OP_DIM '''

def p_Throws(p):
	''' Throws : THROWS ClassNameList '''

def p_MethodBody(p):
	''' MethodBody : Block
	| SEMICOLON '''

def p_ConstructorDeclaration(p):
	''' ConstructorDeclaration : Modifiers ConstructorDeclarator Throws Block
	| Modifiers ConstructorDeclarator        Block
	|           ConstructorDeclarator Throws Block
	|           ConstructorDeclarator        Block '''

def p_ConstructorDeclarator(p):
	''' ConstructorDeclarator : IDENTIFIER LROUNPAREN ParameterList RROUNPAREN
	| IDENTIFIER LROUNPAREN RROUNPAREN '''

def p_StaticInitializer(p):
	''' StaticInitializer : STATIC Block '''

def p_NonStaticInitializer(p):
	''' NonStaticInitializer : Block '''

def p_Extends(p):
	''' Extends : EXTENDS TypeName
	| Extends COMMA TypeName '''

def p_Block(p):
	''' Block : LCURPAREN LocalVariableDeclarationsAndStatements RCURPAREN
	| LCURPAREN RCURPAREN '''

def p_LocalVariableDeclarationsAndStatements(p):
	''' LocalVariableDeclarationsAndStatements : LocalVariableDeclarationOrStatement
	| LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement '''

def p_LocalVariableDeclarationOrStatement(p):
	''' LocalVariableDeclarationOrStatement : LocalVariableDeclarationStatement
	| Statement '''

def p_LocalVariableDeclarationStatement(p):
	''' LocalVariableDeclarationStatement : TypeSpecifier VariableDeclarators SEMICOLON
        | FINAL TypeSpecifier VariableDeclarators SEMICOLON '''

def p_Statement(p):
	''' Statement : EmptyStatement
	| LabelStatement
	| ExpressionStatement SEMICOLON
        | SelectionStatement
        | IterationStatement
	| JumpStatement
	| GuardingStatement
	| Block '''

def p_EmptyStatement(p):
	''' EmptyStatement : SEMICOLON '''

def p_LabelStatement(p):
	''' LabelStatement : IDENTIFIER COLON
        | CASE ConstantExpression COLON
	| DEFAULT COLON '''

def p_ExpressionStatement(p):
	''' ExpressionStatement : Expression '''

def p_SelectionStatement(p):
	''' SelectionStatement : IF LROUNPAREN Expression RROUNPAREN Statement
        | IF LROUNPAREN Expression RROUNPAREN Statement ELSE Statement
        | SWITCH LROUNPAREN Expression RROUNPAREN Block '''

def p_IterationStatement(p):
	''' IterationStatement : WHILE LROUNPAREN Expression RROUNPAREN Statement
	| DO Statement WHILE LROUNPAREN Expression RROUNPAREN SEMICOLON
	| FOR LROUNPAREN ForInit ForExpr ForIncr RROUNPAREN Statement
	| FOR LROUNPAREN ForInit ForExpr         RROUNPAREN Statement '''

def p_ForInit(p):
	''' ForInit : ExpressionStatements SEMICOLON
	| LocalVariableDeclarationStatement
	| SEMICOLON '''

def p_ForExpr(p):
	''' ForExpr : Expression SEMICOLON
	| SEMICOLON '''

def p_ForIncr(p):
	''' ForIncr : ExpressionStatements '''

def p_ExpressionStatements(p):
	''' ExpressionStatements : ExpressionStatement
	| ExpressionStatements COMMA ExpressionStatement '''

def p_JumpStatement(p):
	''' JumpStatement : BREAK IDENTIFIER SEMICOLON
	| BREAK            SEMICOLON
        | CONTINUE IDENTIFIER SEMICOLON
	| CONTINUE            SEMICOLON
	| RETURN Expression SEMICOLON
	| RETURN            SEMICOLON
	| THROW Expression SEMICOLON '''

def p_GuardingStatement(p):
	''' GuardingStatement : SYNCHRONIZED LROUNPAREN Expression RROUNPAREN Statement
	| TRY Block Finally
	| TRY Block Catches
	| TRY Block Catches Finally '''

def p_Catches(p):
	''' Catches : Catch
	| Catches Catch '''

def p_Catch(p):
	''' Catch : CatchHeader Block '''

def p_CatchHeader(p):
	''' CatchHeader : CATCH LROUNPAREN TypeSpecifier IDENTIFIER RROUNPAREN
	| CATCH LROUNPAREN TypeSpecifier RROUNPAREN '''

def p_Finally(p):
	''' Finally : FINALLY Block '''

def p_PrimaryExpression(p):
	''' PrimaryExpression : QualifiedName
	| NotJustName '''

def p_NotJustName(p):
	''' NotJustName : SpecialName
	| NewAllocationExpression
	| ComplexPrimary '''

def p_ComplexPrimary(p):
	''' ComplexPrimary : LROUNPAREN Expression RROUNPAREN
	| ComplexPrimaryNoParenthesis '''

def p_ComplexPrimaryNoParenthesis(p):
	''' ComplexPrimaryNoParenthesis : INT_CONST
	| FLOAT_CONST
	| STRING
	| CHAR_CONST
	| BOOLEAN_CONST
	| ArrayAccess
	| FieldAccess
	| MethodCall '''

def p_ArrayAccess(p):
	''' ArrayAccess : QualifiedName LSQPAREN Expression RSQPAREN
	| ComplexPrimary LSQPAREN Expression RSQPAREN '''

def p_FieldAccess(p):
	''' FieldAccess : NotJustName DOT IDENTIFIER
	| RealPostfixExpression DOT IDENTIFIER
        | QualifiedName DOT THIS
        | QualifiedName DOT CLASS
        | PrimitiveType DOT CLASS '''

def p_MethodCall(p):
	''' MethodCall : MethodAccess LROUNPAREN ArgumentList RROUNPAREN
	| MethodAccess LROUNPAREN RROUNPAREN '''

def p_MethodAccess(p):
	''' MethodAccess : ComplexPrimaryNoParenthesis
	| SpecialName
	| QualifiedName '''

def p_SpecialName(p):
	''' SpecialName : THIS
	| SUPER
	| NULL '''

def p_ArgumentList(p):
	''' ArgumentList : Expression
	| ArgumentList COMMA Expression '''

def p_NewAllocationExpression(p):
	''' NewAllocationExpression : PlainNewAllocationExpression
        | QualifiedName DOT PlainNewAllocationExpression '''

def p_PlainNewAllocationExpression(p):
	''' PlainNewAllocationExpression : ArrayAllocationExpression
    	| ClassAllocationExpression
    	| ArrayAllocationExpression LCURPAREN RCURPAREN
    	| ClassAllocationExpression LCURPAREN RCURPAREN
    	| ArrayAllocationExpression LCURPAREN ArrayInitializers RCURPAREN
    	| ClassAllocationExpression LCURPAREN FieldDeclarations RCURPAREN '''

def p_ClassAllocationExpression(p):
	''' ClassAllocationExpression : NEW TypeName LROUNPAREN ArgumentList RROUNPAREN
	| NEW TypeName LROUNPAREN              RROUNPAREN '''

def p_ArrayAllocationExpression(p):
	''' ArrayAllocationExpression : NEW TypeName DimExprs Dims
	| NEW TypeName DimExprs
        | NEW TypeName Dims '''

def p_DimExprs(p):
	''' DimExprs : DimExpr
	| DimExprs DimExpr '''

def p_DimExpr(p):
	''' DimExpr : LSQPAREN Expression RSQPAREN '''

def p_Dims(p):
	''' Dims : OP_DIM
	| Dims OP_DIM '''

def p_PostfixExpression(p):
	''' PostfixExpression : PrimaryExpression
	| RealPostfixExpression '''

def p_RealPostfixExpression(p):
	''' RealPostfixExpression : PostfixExpression OP_INC
	| PostfixExpression OP_DEC '''

def p_UnaryExpression(p):
	''' UnaryExpression : OP_INC UnaryExpression
	| OP_DEC UnaryExpression
	| ArithmeticUnaryOperator CastExpression
	| LogicalUnaryExpression '''

def p_LogicalUnaryExpression(p):
	''' LogicalUnaryExpression : PostfixExpression
	| LogicalUnaryOperator UnaryExpression '''

def p_LogicalUnaryOperator(p):
	''' LogicalUnaryOperator : '~'
	| NOT '''

def p_ArithmeticUnaryOperator(p):
	''' ArithmeticUnaryOperator : PLUS
	| MINUS '''

def p_CastExpression(p):
	''' CastExpression : UnaryExpression
	| LROUNPAREN PrimitiveTypeExpression RROUNPAREN CastExpression
	| LROUNPAREN ClassTypeExpression RROUNPAREN CastExpression
	| LROUNPAREN Expression RROUNPAREN LogicalUnaryExpression '''

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

def p_AdditiveExpression(p):
	''' AdditiveExpression : MultiplicativeExpression
        | AdditiveExpression PLUS MultiplicativeExpression
	| AdditiveExpression MINUS MultiplicativeExpression '''

def p_ShiftExpression(p):
	''' ShiftExpression : AdditiveExpression
        | ShiftExpression OP_SHL AdditiveExpression
        | ShiftExpression OP_SHR AdditiveExpression
        | ShiftExpression OP_SHRR AdditiveExpression '''

def p_RelationalExpression(p):
	''' RelationalExpression : ShiftExpression
        | RelationalExpression LESS ShiftExpression
	| RelationalExpression MORE ShiftExpression
	| RelationalExpression OP_LE ShiftExpression
	| RelationalExpression OP_GE ShiftExpression
	| RelationalExpression INSTANCEOF TypeSpecifier '''

def p_EqualityExpression(p):
	''' EqualityExpression : RelationalExpression
        | EqualityExpression OP_EQ RelationalExpression
        | EqualityExpression OP_NE RelationalExpression '''

def p_AndExpression(p):
	''' AndExpression : EqualityExpression
        | AndExpression '&' EqualityExpression '''

def p_ExclusiveOrExpression(p):
	''' ExclusiveOrExpression : AndExpression
	| ExclusiveOrExpression '^' AndExpression '''

def p_InclusiveOrExpression(p):
	''' InclusiveOrExpression : ExclusiveOrExpression
	| InclusiveOrExpression '|' ExclusiveOrExpression '''

def p_ConditionalAndExpression(p):
	''' ConditionalAndExpression : InclusiveOrExpression
	| ConditionalAndExpression OP_LAND InclusiveOrExpression '''

def p_ConditionalOrExpression(p):
	''' ConditionalOrExpression : ConditionalAndExpression
	| ConditionalOrExpression OP_LOR ConditionalAndExpression '''

def p_ConditionalExpression(p):
	''' ConditionalExpression : ConditionalOrExpression
	| ConditionalOrExpression QUES Expression COLON ConditionalExpression '''

def p_AssignmentExpression(p):
	''' AssignmentExpression : ConditionalExpression
	| UnaryExpression AssignmentOperator AssignmentExpression '''

def p_AssignmentOperator(p):
	''' AssignmentOperator : EQUAL
	| ASS_MUL
	| ASS_DIV
	| ASS_MOD
	| ASS_ADD
	| ASS_SUB
	| ASS_SHL
	| ASS_SHR
	| ASS_SHRR
	| ASS_AND
	| ASS_XOR
	| ASS_OR '''

def p_Expression(p):
	''' Expression : AssignmentExpression '''

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