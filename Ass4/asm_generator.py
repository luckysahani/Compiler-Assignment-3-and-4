import asm as assembly
import parser_test as parser
import pprint

def getAssemblyCode(filename):
	ST,TAC = parser.parserFile(filename)
	paramcount = 0
	# ST.Printsymbtbl()
	# TAC.printTac()

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
					asm.addInstr(['sub','$fp','$sp',24+4*len(ST.mainsymbtbl[function]['Parameters'])])
					asm.storeParam(function)
					# func_stack_size = 272
					asm.addInstr(['sub','$sp','$fp',400])
			elif(op == 'Endfunction'):
				if(function == 'Main.HelloWorld.main'):
					asm.addInstr(['li','$v0','10',''])
					asm.addInstr(['syscall','','',''])
				else :
					asm.addInstr(['jr','$ra','',''])
			elif (op == '=a'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['li',reg1,x,''])
				asm.storeReg(z,0)
			elif (op == "=") :
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				asm.addInstr(['move',reg1,reg2,''])
				asm.storeReg(z,0)
			elif (op == '+'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				if (type(y)==int):
					asm.addInstr(['li','$s7',y,''])
					asm.addInstr(['add',reg1,reg2,'$s7'])
				else:
					reg3 = asm.getReg(y,2)
					asm.addInstr(['add',reg1,reg2,reg3])
				asm.storeReg(z,0)
			elif (op == '-'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				if (type(y)==int):
					asm.addInstr(['li','$s7',y,''])
					asm.addInstr(['sub',reg1,reg2,'$s7'])
				else:
					reg3 = asm.getReg(y,2)
					asm.addInstr(['sub',reg1,reg2,reg3])
				asm.storeReg(z,0)
			elif (op == '*'):
				reg1 = asm.getReg(z,0)
				reg3 = asm.getReg(y,2)
				if(not type(x) == int):
					reg2 = asm.getReg(x,1)
					asm.addInstr(['mult',reg2,reg3,''])
				else :
					asm.addInstr(['li','$s7',x,''])
					asm.addInstr(['mult','$s7',reg3,''])
				asm.addInstr(['mflo',reg1,'',''])
				asm.storeReg(z,0)
			elif (op == '/'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['div',reg2,reg3,''])
				asm.addInstr(['mflo',reg1,'',''])
				asm.storeReg(z,0)
			elif (op == '%'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['div',reg2,reg3,''])
				asm.addInstr(['mfhi',reg1,'',''])
				asm.storeReg(z,0)
			elif (op == '<'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['slt',reg1,reg2,reg3,''])
				asm.storeReg(z,0)
			elif (op == '>'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['sgt',reg1,reg2,reg3,''])
				asm.storeReg(z,0)
			elif (op == '<='):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['sle',reg1,reg2,reg3,''])
				asm.storeReg(z,0)
			elif (op == '>='):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['sge',reg1,reg2,reg3,''])
				asm.storeReg(z,0)
			elif(op == 'GOTO'):
				asm.addInstr(['j',y,'',''])
			elif (op == 'COND_GOTO'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['beq',reg1,'$0',y])
				asm.storeReg(z,0)
			elif (op == 'COND_GOTO_TR'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['bneq',reg1,'$0',y])
				asm.storeReg(z,0)
			elif (op == 'PARAM'):
				# param_reg = asm.getParamReg(z)
				reg1 = asm.getReg(z,0)
				paramcount += 4
				asm.addInstr(['sw',reg1,'-'+str(paramcount)+'($sp)',''])
			elif (op == 'F_CALL'):
				if(z == 'Print' and y == 'int'):
					reg = asm.getReg(x,1)
					asm.addInstr(['move','$a0',reg,''])
					asm.addInstr(['li','$v0','1',''])
					asm.addInstr(['syscall','','',''])
				else:
					asm.savePrevValues(100,paramcount)
					asm.addInstr(['jal',y,'',''])
				paramcount = 0
			elif (op == 'RETURN'):
				asm.addInstr(['move','$v0',asm.varInfo[z]['Reg'],''])
				asm.addInstr(['jr','$ra','',''])
			elif (op == 'FETCH'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['la',reg1,'-'+str(ST.infovar[asm.currFunc][x]['offset'])+'($fp)',''])
				asm.storeReg(z,0)
				# print ST.infovar[asm.currFunc][x]['offset']	
				# print 'Halsdmsalkmdlkm'
			elif (op == '=*'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				asm.addInstr(['sw',reg2,'0('+reg1+')',''])
				asm.storeReg(z,0)
			elif (op == '=arr'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				asm.addInstr(['lw',reg1,'0('+reg2+')',''])
				asm.storeReg(z,0)
			elif (op == 'LABEL'):
				asm.addInstr([z+':','','',''])


	pprint.pprint(asm.regAssignedVar)
	pprint.pprint(asm.assembly_code)
	asm.printAssembly()

getAssemblyCode('test/if.java')
