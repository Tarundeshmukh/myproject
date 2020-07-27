class Employee:
	def __init__(self,a,b):
		self.name=a
		self.salary=b
	def getName(self):
		return self.name
	def getSal(self):
		return self.salary

class Manager(Employee):
	def __init__(self,a,b,c):
		super().__init__(a,b)
		self.incentive=c
	def getSal(self):
		return self.salary+self.incentive
			
e1 = Employee("Tarun", 35000)
print("Total salary for {} is Rs. {}".format(e1.getName(), e1.getSal()))
m1 = Manager("Sia",25000,10000)
print("Total salary for {} is Rs. {}".format(m1.getName(), m1.getSal()))				
				
