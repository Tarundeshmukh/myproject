class Intern:
	increment = 1
	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary
		self.increment = 1.4	
	def increase(self):
		self.salary = self.salary * Intern.increment
		
	@classmethod
	def change_increment(cls, amount):
		cls.increment = amount
	
	@classmethod
	def from_str(cls, emp_string):
		fname, lname, salary = emp_string.split("-")
		return cls(fname, lname, salary)
	
	@staticmethod
	def isopen(day):
		if day == "sunday":
			return False
		else: return True
		
class Programmer(Intern):
	def __init__(self, fname, lname, salary, proglang, exp):
		super().__init__(fname, lname, salary)
		self.proglang = proglang
		self.exp = exp
		
	def increase(self):
		self.salary = int(self.salary*(self.increment + 0.5))			
		return self.salary
				
z = Intern.from_str("Steve-Jobs-10000000") 		
x = Intern("Tarun", "Deshmukh", 15000)
y = Intern("Rani", "Rai", 10000)
tarun = Programmer("Tarun", "Deshmukh", 15000, "Python", "4 mon")

print(tarun.exp, "\n")
print(tarun.increase(), "\n")
print(Intern.isopen("saturday"))
#print(Intern.__dict__)
print(x.salary, "\n")
print(y.salary, "\n")
Intern.change_increment(3)
x.increase()
print("After increment:", x.salary, "\n")
#print(x.__dict__)		
print(z.salary, "\n")
print(z.fname)	
