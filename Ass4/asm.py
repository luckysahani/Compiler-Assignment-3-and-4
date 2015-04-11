import pprint
class asm:
	def __init__(self, symbolTable, threeAddressCode):
		self.assembly_code = {}
		self.ST = symbolTable
		self.currFunc = ''
		self.TAC = threeAddressCode
		self.resetReg()
		self.stack = {}		# We have to variable name, value, type

	def resetReg(self):
		self.registors = {
		'$0' : 0,				#$0		# always contains zero
		'$at': None , 			#$1		# assembler temporary
		'$v0': None , 			#$2		# Values from expression evaluation and function results
		'$v1': None ,			#$3		# Same as above
		'$a0': None ,			#$4		# First four parameters for function call 
		'$a1': None ,			#$5		# Not preserved across function calls
		'$a2': None , 			#$6		#
		'$a3': None , 			#$7		#
		'$t0': None ,			#$8		# (temporaries) Caller saved if needed.
		'$t1': None ,			#$9		# Subroutines can use w/out saving.
		'$t2': None ,			#$10	# Not preserved across procedure calls
		'$t3': None ,			#$11	#
		'$t4': None ,			#$12	#
		'$t5': None ,			#$13	#
		'$t6': None ,			#$14	#
		'$t7': None ,			#$15	#
		'$s0': None , 			#$16	# (saved values) - Callee saved. 
		'$s1': None , 			#$17	# A subroutine using one of these must save original 
		'$s2': None , 			#$18	# and restore it before exiting.
		'$s3': None , 			#$19	# Preserved across procedure calls.
		'$s4': None , 			#$20	# 
		'$s5': None , 			#$21	# 
		'$s6': None , 			#$22	# 
		'$s7': None , 			#$23	#
		'$t8': None ,			#$24	# (temporaries) Caller saved if needed. Subroutines can use w/out saving.
		'$t9': None ,			#$25	# Not preserved across procedure calls.
		'$k0': None , 			#$26	# reserved for use by the interrupt/trap handler
		'$k1': None , 			#$27	# 
		'$gp': None , 			#$28	# Global pointer. Points to the middle of the 64K block of memory in the static data segment.
		'$sp': None , 			#$29	# stack pointer 
		'$fp': None , 			#$30	# frame pointer, preserved across procedure calls
		'$ra': None ,			#s31	# return address
		}
		self.regUsed = []
		self.regFree = ['$t0','$t1']
		self.regAssignedVar = {}
		self.varInfo = {}
		self.tempoffset = 0


	def function_call(self,function):
		self.currFunc = function
		self.assembly_code[function] = []

	def addInstr(self,instr):
		self.assembly_code[self.currFunc].append(instr)

	def flushReg(self,reg):
		self.regFree.append(reg)
		self.addInstr(['sw',reg,'-'+str(self.varInfo[self.regAssignedVar[reg]]['Offset'])+'($fp)',''])
		self.varInfo[self.regAssignedVar[reg]]['Reg'] = None

	def getReg(self,var):
		if(self.varInfo.has_key(var)) :
			if(not self.varInfo[var]['Reg'] == None):
				reg = self.varInfo[var]['Reg']
			else:
				if(self.regFree):
					reg = self.regFree.pop(0)
				else :
					lastUsedReg = self.regUsed.pop(0)
					self.flushReg(lastUsedReg)
					reg = lastUsedReg
				self.addInstr(['lw',reg,'-'+str(self.varInfo[var]['Offset'])+'($fp)',''])
			self.regUsed.append(reg)
			self.regAssignedVar[reg] = var
			self.varInfo[var]	['Reg'] = reg
		else :
			self.varInfo[var] = {'Reg' : None, 'Memory' : None, 'Offset' : None}
			if(self.regFree):
				reg = self.regFree.pop(0)
			elif(not self.regFree):
				lastUsedReg = self.regUsed.pop(0)
				self.flushReg(lastUsedReg)
				reg = lastUsedReg
				# reg = self.registors[lastUsedReg]
			self.regUsed.append(reg)
			self.regAssignedVar[reg] = var
			self.varInfo[var]['Reg'] = reg
			self.varInfo[var]['Offset'] = self.ST.infovar[self.currFunc][var]['offset']
			pprint.pprint(self.varInfo[var])
		return reg

	def prints(self):
		for key in self.assembly_code :
			for lines in self.assembly_code[key]:
				print str(lines[0]) + '\t' + str(lines[1]) + ',\t' + str(lines[2]) + '\t' + str(lines[3]) 

