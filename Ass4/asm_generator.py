import asm as assembly
import parser_test as parser
import pprint,sys

def getAssemblyCode(filename):
	ST,TAC = parser.parserFile(filename)
	paramcount = 4
	# ST.Printsymbtbl()
	# TAC.printTac()
	# pprint.pprint(ST.infovar)
	asm = assembly.asm(ST,TAC)
	pprint.pprint(TAC.code)
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
				if(function.split('.')[-1] == 'main'):
					main_size = 200
					asm.addInstr(['sub','$sp','$sp',main_size])
					asm.addInstr(['la','$fp',str(main_size)+'($sp)',''])
				else:
					# For functions other than main
					asm.addInstr(['sub','$fp','$sp',28+4*len(ST.mainsymbtbl[function]['Parameters'])])
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
			elif (op == '=s'):
				asm.addToString(z,x)
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
			elif (op == '||'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['or',reg1,reg2,reg3])
				asm.storeReg(z,0)
			elif (op == '&&'):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['and',reg1,reg2,reg3])
				asm.storeReg(z,0)
			elif (op == '=='):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['sub','$s7',reg2,reg3])
				asm.addInstr(['slt','$s6','$0','$s7'])
				asm.addInstr(['slt','$s5','$s7','$0'])
				asm.addInstr(['or',reg1,'$s6','$s5'])
				asm.addInstr(['li','$s7',1,''])
				asm.addInstr(['sub',reg1,'$s7',reg1])
				asm.storeReg(z,0)
			elif (op == '!='):
				reg1 = asm.getReg(z,0)
				reg2 = asm.getReg(x,1)
				reg3 = asm.getReg(y,2)
				asm.addInstr(['sub','$s7',reg2,reg3])
				asm.addInstr(['slt','$s6','$0','$s7'])
				asm.addInstr(['slt','$s5','$s7','$0'])
				asm.addInstr(['or',reg1,'$s6','$s5'])
				asm.storeReg(z,0)
			elif(op == 'GOTO'):
				asm.addInstr(['j',y,'',''])
			elif (op == 'COND_GOTO'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['beq',reg1,'$0',y])
				# asm.storeReg(z,0)
			elif (op == 'COND_GOTO_TR'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['bne',reg1,'$0',y])
				# asm.storeReg(z,0)
			elif (op == 'PARAMC'):
				off = ST.infovar[function][z]['offset']
				asm.addInstr(['la','$s0',str(-off)+'($fp)',''])
				asm.addInstr(['sw','$s0','-4($sp)','####'])
			elif (op == 'PARAM'):
				# param_reg = asm.getParamReg(z)
				reg1 = asm.getReg(z,0)
				paramcount += 4
				if('.' in ST.infovar[function][z]['type']):
					flag = False
					for param in ST.mainsymbtbl[function]['Parameters'] :
						if(param['Name'] == z and flag == False) :
							asm.addInstr(['lw','$s0',str(-ST.infovar[function][z]['offset'])+'($fp)','#'])
							flag = True
							break
					if(not flag):
						asm.addInstr(['la','$s0',str(-ST.infovar[function][z]['offset'])+'($fp)','#1'])
					asm.addInstr(['sw','$s0','-'+str(paramcount)+'($sp)',''])
				else :
					asm.addInstr(['sw',reg1,'-'+str(paramcount)+'($sp)',''])
			elif (op == 'F_CALL'):
				if(z == 'Print' and y == 'int'):
					reg = asm.getReg(x,1)
					asm.addInstr(['move','$a0',reg,''])
					asm.addInstr(['li','$v0','1',''])
					asm.addInstr(['syscall','','',''])
				elif( z == 'Print' and y == 'string'):
					# print "Here"
					asm.addInstr(['la','$a0',x,''])
					asm.addInstr(['li','$v0','4',''])
					asm.addInstr(['syscall','','',''])
				else:
					asm.savePrevValues(100,paramcount)
					asm.addInstr(['jal',y,'',''])
					asm.addInstr(['lw','$ra','12($fp)',''])
					asm.addInstr(['lw','$sp','4($fp)',''])
					asm.addInstr(['lw','$fp','8($fp)',''])
					reg1 = asm.getReg(z,0)
					asm.addInstr(['move',reg1,'$v0',''])
					asm.storeReg(z,0)

				paramcount = 4
			elif (op == 'F_CALLC'):
				asm.savePrevValues(100,paramcount)
				asm.addInstr(['jal',y,'',''])
				asm.addInstr(['lw','$ra','12($fp)',''])
				asm.addInstr(['lw','$sp','4($fp)',''])
				asm.addInstr(['lw','$fp','8($fp)',''])
				reg1 = asm.getReg(z,0)
				asm.addInstr(['move',reg1,'$v0',''])
				asm.storeReg(z,0)

				paramcount = 4
			elif (op == 'RETURN'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['move','$v0',reg1,''])
				asm.addInstr(['jr','$ra','',''])
			elif (op == 'FETCH'):
				reg1 = asm.getReg(z,0)
				flag = False
				# print ST.mainsymbtbl[function]['Parameters']
				# print z
				for param in ST.mainsymbtbl[function]['Parameters'] :
					if(param['Name'] == x and flag == False) :
						asm.addInstr(['lw',reg1,'-'+str(ST.infovar[asm.currFunc][x]['offset'])+'($fp)','#2'])
						flag = True
						break
				if(not flag):
					# print reg1
					asm.addInstr(['la',reg1,'-'+str(ST.infovar[asm.currFunc][x]['offset'])+'($fp)','#3'])
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
			elif (op == '*+='):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['lw','$s7','0($fp)',''])
				asm.addInstr(['li','$s6',y,''])
				asm.addInstr(['sub','$s7','$s7','$s6'])
				asm.addInstr(['lw',reg1,'0($s7)',''])
				asm.storeReg(z,0)
			elif (op == 'thisassign'):
				reg1 = asm.getReg(z,0)
				asm.addInstr(['lw','$s7','0($fp)',''])
				asm.addInstr(['li','$s6',y,''])
				asm.addInstr(['sub','$s7','$s7','$s6'])
				asm.addInstr(['sw',reg1,'0($s7)',''])
				# asm.storeReg(z,0)
			elif (op == '+*='):
				reg1 = asm.getReg(z,0)
				off = ST.infovar[function][x]['offset']
				asm.addInstr(['la','$s7',str(-off)+'($fp)',''])
				asm.addInstr(['li','$s6',y,''])
				asm.addInstr(['sub','$s7','$s7','$s6'])
				asm.addInstr(['lw',reg1,'0($s7)',''])
				asm.storeReg(z,0)
			elif (op == 'cvarass'):
				reg3 = asm.getReg(y,2)
				off = ST.infovar[function][z]['offset']
				asm.addInstr(['la','$s7',str(-off)+'($fp)',''])
				asm.addInstr(['li','$s6',x,''])
				asm.addInstr(['sub','$s7','$s7','$s6'])
				asm.addInstr(['sw',reg3,'0($s7)',''])



	# pprint.pprint(asm.regAssignedVar)
	# pprint.pprint(asm.assembly_code)
	asm.printAssembly()

getAssemblyCode(sys.argv[1])
