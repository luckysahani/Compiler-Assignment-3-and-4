import asm as assembly
import parser_test as parser
import pprint

def getAssemblyCode(filename):
	ST,TAC = parser.parserFile(filename)
	# ST.Printsymbtbl()
	TAC.printTac()

	asm = assembly.asm(ST,TAC)
	# pprint.pprint(TAC.code)
	for function in TAC.code:
		asm.function_call(function)
		# things to do for main
		for threeAddress in TAC.code[function]:
			z = threeAddress[0] 
			x = threeAddress[1] 
			y = threeAddress[2] 
			op = threeAddress[3] 


			if (op == 'BeginFunction'):
				# main_size = z
				if(function == 'Main.HelloWorld.main'):
					main_size = 200
					asm.addInstr(['sub','$sp','$sp',main_size])
					asm.addInstr(['la','$fp',str(main_size)+'($sp)',''])
				else:
					# For functions other than main
					func_stack_size = 272
					asm.addInstr(['sub','$sp','$sp',func_stack_size])

			elif (op == '=a'):
				reg1 = asm.getReg(z)
				asm.addInstr(['li',reg1,x,''])
			elif (op == "=") :
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				asm.addInstr(['move',reg1,reg2,''])
			elif (op == '+'):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['add',reg1,reg2,reg3])
			elif (op == '-'):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['sub',reg1,reg2,reg3])
			elif (op == '*'):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['mult',reg2,reg3,''])
				asm.addInstr(['mflo',reg1,'',''])
			elif (op == '/'):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['div',reg2,reg3,''])
				asm.addInstr(['mflo',reg1,'',''])
			elif (op == '%'):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['div',reg2,reg3,''])
				asm.addInstr(['mfhi',reg1,'',''])
			elif (op == '<'):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['slt',reg1,reg2,reg3,''])
			elif (op == '>'):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['sgt',reg1,reg2,reg3,''])
			elif (op == '<='):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['sle',reg1,reg2,reg3,''])
			elif (op == '>='):
				reg1 = asm.getReg(z)
				reg2 = asm.getReg(x)
				reg3 = asm.getReg(y)
				asm.addInstr(['sge',reg1,reg2,reg3,''])
			elif (op == 'COND_GOTO'):
				reg1 = asm.getReg(z)
				asm.addInstr(['beq',reg1,'$0',y])
			elif (op == 'COND_GOTO_TR'):
				reg1 = asm.getReg(z)
				asm.addInstr(['bneq',reg1,'$0',y])
			elif (op == 'PARAM'):
				param_reg = asm.getParamReg(z)
			elif (op == 'F_CALL'):
				if(z == 'Print' and y == 'int'):
					reg = asm.getReg(x)
					asm.addInstr(['move','$a0',reg,''])
					asm.addInstr(['li','$v0','1',''])
					asm.addInstr(['syscall','','',''])
				else:
					asm.savePrevValues(100)
					asm.addInstr(['jal',y,'',''])
			elif (op == 'RETURN'):
				asm.addInstr(['move','$v0',asm.varInfo[z]['Reg'],''])
				asm.addInstr(['jr','$ra','',''])	

	pprint.pprint(asm.regAssignedVar)
	pprint.pprint(asm.assembly_code)
	asm.printAssembly()

getAssemblyCode('test/if.java')