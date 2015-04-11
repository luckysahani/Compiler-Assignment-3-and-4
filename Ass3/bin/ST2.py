import pprint

class SymbTbl:
	def __init__(self):
		self.mainsymbtbl = {
			'Main':{
				'ScopeName' : 'NULL',
				'Type' : 'function',
				'ReturnType' : 'undefined',
				'ParentScope' : 'Main',
				'Functions' : {},
				'Strings' : {}
			}
		}
		self.curr_scope = 'Main';
		self.curr_funcname = 'None'
		self.curr_class = 'None'
		self.tempvarcnt = 0;
		self.temp = 0;

	#functions to debug the code
	def Printsymbtbl(self):
		pprint.pprint(self.mainsymbtbl)

	#function to get the current scopelist
	def GetCurrentScopeName(self):
		return self.curr_scope

	def Get_off(self, identifier):
		# print identifier
		off = 0
		for elem in self.mainsymbtbl[self.curr_class]['identifiers']:
			print elem
			if(elem == identifier) :
				return off
			else :
				off += self.mainsymbtbl[self.curr_class]['identifiers'][elem]['Width']

	def Check_identifier_class(self, identifier, scopeName):
		# print scopeName
		if scopeName == self.curr_class:
			return None
		temp_scope = self.mainsymbtbl[scopeName]

		if temp_scope['identifiers'].has_key(identifier):
			return temp_scope['identifiers'][identifier]
		else:
			return self.Check_identifier_class(identifier, temp_scope['ParentScope'])
	
	def Find_identifier_class(self, identifier):
		return self.Check_identifier_class(identifier, self.curr_scope);

	def Check_identifier(self, identifier, scopeName):
				# print identifier
		if scopeName == 'Main':
			return None
		temp_scope = self.mainsymbtbl[scopeName]

		if temp_scope['identifiers'].has_key(identifier):
			return temp_scope['identifiers'][identifier]
		else:
			return self.Check_identifier(identifier, temp_scope['ParentScope'])

	#function to check whether given identifier is present or not
	def Find_identifier(self, identifier):
		return self.Check_identifier(identifier, self.curr_scope);

	#function to add a scope
	def Add_scope(self, scopeName, Type, ReturnType):
		temp_scope = {
			'ScopeName' : self.curr_scope+ '.'+ scopeName,
			'ParentScope' : self.curr_scope,
			'Type' : Type,
			'identifiers' : {},
			'Strings' : {},
			'Ifcount' : 0,
			'offset' : 0
		}
		if(Type == "Class"):
			temp_scope['Functions'] = {}
			self.curr_class = temp_scope['ScopeName']
			self.curr_funcname = self.curr_class
		if(Type == "Function") :
			temp_scope['ReturnType'] = ReturnType
			temp_scope['Function'] = temp_scope['ScopeName']
			self.curr_funcname = temp_scope['ScopeName']
			self.mainsymbtbl[self.curr_class]['Functions'][scopeName] = {'Name' : scopeName, 'Type' : temp_scope['ReturnType']}
		elif(Type == 'if') :
			temp_scope['Function'] = temp_scope['ScopeName']
		self.mainsymbtbl[temp_scope['ScopeName']] = temp_scope
		self.curr_scope = temp_scope['ScopeName']
		return temp_scope['ScopeName']

	#function to add an identifier
	def Add_identifier(self, identifier, Type, Arrwidth):
		Curr_scope = self.mainsymbtbl[self.curr_scope];
		if Type in ['function', 'callback', 'String']:
			width = 4
		elif Type == 'int':
			width = 4
		elif Type in ['char', 'bool']:
			width = 1
		elif Type in ['float', 'double']:
			width = 8
		elif Arrwidth != -1 :
			width = 4
		else:
			width = 0
		
		if(self.curr_funcname != 'None'):
			self.mainsymbtbl[self.curr_funcname]['offset'] += width 

		temp_obj = { 
			'Width' : width,
			'Type' : Type
		}

		if(Arrwidth != -1):
			# print Arrwidth
			temp_obj['Arrwidth'] = Arrwidth

		if not Curr_scope['identifiers'].has_key(identifier):
			Curr_scope['identifiers'][identifier] = temp_obj
		else :
			print "identifier already present"

	def Add_attr(self, identifier, attr, attr_value):
		entry = self.Find_identifier(identifier)
		entry[attr] = attr_value

	def Add_attr_scope(self, attr, attr_value):
		self.mainsymbtbl[self.curr_scope][attr] = attr_value

	def Get_attr_scope(self, attr):
		return self.mainsymbtbl[self.curr_scope][attr]

	def Get_attr(self, identifier, attr):
		entry = self.Find_identifier(identifier)
		return entry[attr]

	def Exists(self, identifier):
		if(self.Find_identifier(identifier) == None):
			return False
		else:
			return True

	def Exists_class(self, identifier):
		if(self.Find_identifier_class(identifier) == None):
			return False
		else:
			return True

	def Exists_curr_scope(self, identifier):
		Curr_scope = self.mainsymbtbl[self.curr_scope]
		if (Curr_scope['identifiers'].has_key(identifier)) :
			return True
		else :
			return False

	def Change_scope (self) :
		if(self.mainsymbtbl[self.curr_scope]['Type'] == 'Function') :
			self.curr_funcname = self.curr_class
		self.curr_scope = self.mainsymbtbl[self.curr_scope]['ParentScope']
		return self.curr_scope

	def Change_func (self) :
		self.curr_funcname = None

	def Gen_Temp(self):
		v = "t_"+ str(self.tempvarcnt);
		self.tempvarcnt = self.tempvarcnt + 1;
		return v

	def Add_string(self, name, strval):
		self.mainsymbtbl[self.curr_scope]['Strings'][name] = strval

	def inc_offset(self,Type):
		if Type == 'int':
			width = 4
		elif Type in ['char', 'bool']:
			width = 1
		elif Type in ['float', 'double']:
			width = 8
		else:
			width = 0
		print Type

		self.mainsymbtbl[self.curr_funcname]['offset'] += width

	def gen_tempnum(self) :
		self.temp += 1
		return self.temp

	def Get_size(self,Type) :
		if Type in ['function', 'callback', 'string']:
			width = 4
		elif Type == 'int':
			width = 4
		elif Type in ['char', 'bool']:
			width = 1
		elif Type in ['float', 'double']:
			width = 8
		else:
			width = 0
		return width