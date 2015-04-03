import pprint

class SymbTbl:
	def __init__(self):
		self.mainsymbtbl = {
			'ScopeName' : 'Main',
			'Type' : 'function',
			'ReturnType' : 'undefined',
			'ParentScope' : 'Main',
			'Functions' : {}
			'Strings' : {}
		}
		self.scopelist = [self.mainsymbtbl]
		self.tempvarcnt = 0;

	#functions to debug the code
	def Printsymbtbl(self):
		pprint.pprint(self.scopelist)

	#function to get the current scopelist
	def GetCurrentScopeName(self):
		return self.scopelist[-1]['ScopeName']


	def Check_identifier(self, identifier, index):
		if index == -1 :
			return None
		temp_scope = self.scopelist[index]

		if temp_scope['identifiers'].has_key(identifier):
			return temp_scope['identifiers'][identifier]
		else:
			return self.Check_identifier(identifier, index-1)

	#function to check whether given identifier is present or not
	def Find_identifier(self, identifier):
		index = len(self.scopelist) - 1
		return self.Check_identifier(identifier, index);

	

	#function to add a scope
	def Add_scope(self, scopeName, Type):
		curr_scope = self.scopelist[-1]
		temp_scope = {
			'ScopeName' : curr_scope['ScopeName']+ '.'+ scopeName,
			'ParentScope' : curr_scope['ScopeName'],
			'ReturnType' : 'undefined',
			'Functions' : {},
			'Type' : Type,
			'identifiers' : {},
			'Strings' : {},
			'Ifcount' : 0
		}
		self.scopelist.append(temp_scope)
		return temp_scope['ScopeName']

	#function to add an identifier
	def Add_identifier(self, identifier, Type):
		curr_scope = self.scopelist[-1];
		if Type in ['function', 'callback', 'String']:
			width = 4
		elif Type == 'int':
			width = 4
		elif Type in ['char', 'bool']:
			width = 1
		elif Type in ['float', 'double']:
			width = 8
		else:
			width = -1
		
		temp_obj = { 
			'Width' : width,
			'Type' : Type
		}

		if not curr_scope['identifiers'].has_key(identifier):
			curr_scope['identifiers'][identifier] = temp_obj

	def Add_attr(self, identifier, attr, attr_value):
		entry = self.Find_identifier(identifier)
		entry[attr] = attr_value

	def Add_attr_scope(self, attr, attr_value):
		curr_scope = self.scopelist[-1][attr] = attr_value

	def Get_attr_scope(self, attr):
		return self.scopelist[-1][attr]

	def Get_attr(self, identifier, attr):
		entry = self.Find_identifier(identifier)
		return entry[attr]

	def Exists(self, identifier):
		if(self.Find_identifier(identifier) == None):
			return False
		else:
			return True

	def Exists_curr_scope(self, identifier):
		curr_scope = self.scopelist[-1]
		if (curr_scope.has_key(identifier)) :
			return True
		else :
			return False

	def Del_scope(self, scopeName):
		del self.scopelist[-1]

	def Gen_Temp(self):
		v = "t_"+ str(self.tempvarcnt);
		self.tempvarcnt = self.tempvarcnt + 1;
		return v

	def Add_string(self, name, strval):
		self.scopelist[-1]['Strings'][name] = strval
