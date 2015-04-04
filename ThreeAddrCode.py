class threeAddressCode:
	# Constructor for threeAddressCode object
	def __init__(self, ST):
		self.code = {'Main': []}
		self.instr = {'Main': -1}
		self.nextInstr = {'Main': 0}
		self.labels = {'Main' : {}}

		self.labelcount = 0;
		self.ST = ST

	# Function to print the symbol table
	def printSymbTbl(self):
		self.ST.printSymbTbl()

	# Find the next instruction 
	def getNextInstr(self):
		return self.nextInstr[self.ST.curr_funcname]

	# Move to next instruction
	def incInstr(self):
		currFunc = self.ST.curr_funcname
		self.instr[currFunc] = self.nextInstr[currFunc]
		self.nextInstr[currFunc] += 1 ;

	# Backpatch to avoid two pass code generation
	def backPatch(self, llist, loc):
		curr = self.ST.curr_funcname
		for position in llist:
			self.code[curr][position][2] = self.make_label(loc)

	# Get length of the current instruction
	def getLengthInstr(self, funcName):
		return self.instr[funcName]
	
	# Make new jump label
	def make_newlabel(self):
		temp1 = 'L_' + str(self.labelcount)
		self.labelcount += 1
		return temp1

	# Return label if it already exists else make new one and return it.
	def make_label(self,line):
		if self.labels[self.ST.curr_funcname].has_key(line) :
			return self.labels[self.ST.curr_funcname][line]
		else:
			temp1 = self.make_newlabel()
			self.labels[self.ST.curr_funcname][line] = temp1
			return temp1

	# Function to merge the lists (truelists and falselists)
	def merge(self, list1, list2):
		list3 = list(list1)
		list3.extend(list2)
		return list3

	# emit code for an instruction
	def emit(self, destReg, srcReg1, srcReg2, op):
		currScope = self.ST.curr_funcname
		self.incInstr()
		self.code[currScope].append([destReg, srcReg1, srcReg2, op])

	# Create a new three address code's quadruple
	def genNewTacFunc(self, funcName):
		self.instr[funcName] = -1
		self.nextInstr[funcName] = 0
		self.code[funcName] = []
		self.labels[funcName] = {}

	# Generate output
	def printTac(self):
		for key in self.code:
			numline = 0
			print key + ' :\n'
			for line in self.code[key] :
				if self.labels[key].has_key(numline):
					print '\n' + self.labels[key][numline] + ' :\n'
				print str(line[0]) + '\t' + str(line[1]) + '\t' + str(line[2]) + '\t' + str(line[3]) 
				numline += 1

    # Function to backpatch
    
		