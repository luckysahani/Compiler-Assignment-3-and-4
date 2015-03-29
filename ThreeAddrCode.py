class threeAddressCode:
	def __init__(self, ST):
		self.code = {'Main': []}
		self.instr = {'Main': -1}
		self.nextInstr = {'Main': 0}

		self.ST = ST

	def printSymbTbl(self):
		self.ST.printSymbTbl()

	def getNextInstr(self):
		return self.nextInstr[self.ST.GetCurrentScopeName()]

	def incInstr(self):
		currScope = self.ST.GetCurrentScopeName()
		self.instr[currScope] = self.nextInstr[currScope]
		self.nextInstr[currScope] += 1 ;

	def backPatch(self, llist, loc):
		curr = self.ST.GetCurrentScopeName()
		for position in llist:
			self.code[curr][position][2] = loc

	def getLengthInstr(self, funcName):
		return self.instr[funcName]
	
	
	def merge(self, list1, list2):
		list3 = list(list1)
		list3.extend(list2)
		return list3
	#emit code for an instruction
	def emit(self, destReg, srcReg1, srcReg2, op):
		currScope = self.ST.GetCurrentScopeName()
		self.incInstr()
		self.code[currScope].append([destReg, srcReg1, srcReg2, op])

	def genNewTacFunc(self, funcName):
		self.instr[funcName] = -1
		self.nextInstr[funcName] = 0
		self.code[funcName] = []

    # Function to backpatch
    
		