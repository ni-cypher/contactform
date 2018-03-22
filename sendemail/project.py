class Project(object):
	def __init__(self,prjName,prjSalary,prjPlace,prjTime):
	 self.__prjName=prjName
	 self.__prjSalary=prjSalary
	 self.__prjPlace=prjPlace
	 self.__prjTime=prjTime

	@property
	def prjName(self):
	 return self.__prjName

	@property
	def prjSalary(self):
	 return self.__prjSalary

	@property
	def prjPlace(self):
	 return self.__prjPlace

	@property
	def prjTime(self):
	 return self.__prjTime

	@prjName.setter
	def prjName(self, value):
		self.___prjName=value


	@prjSalary.setter
	def prjSalary(self,value):
		self.__prjSalary=value

	@prjPlace.setter
	def prjPlace(self,value):
		self.___prjPlace=value

	@prjTime.setter
	def _prjTime(self,value):
		self.___prjTime=value

	@prjName.deleter
	def prjName(self):
		del self.___prjName

	@prjSalary.deleter
	def prjSalary(self):
		del self.___prjSalary

	@prjPlace.deleter
	def prjPlace(self):
		del self.___prjPlace

	@prjTime.deleter
	def prjTime(self):
		del self.___prjTime





