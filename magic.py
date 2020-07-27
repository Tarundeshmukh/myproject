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
	
	# dunder/magic methods	
	def __add__(self, other):
		return self.salary + other.salary
	
	def __repr__(self):
		return 'Intern({}, {}, {})'.format(self.fname, self.lname, self.salary)
		
	def __str__(self):
		return 'The name of intern is {}'.format(self.fname)			
tarun = Intern("Tarun", "Deshmukh", 15000)
rani = Intern("Rani", "Rai", 25000)

print(tarun + rani)
print(repr(tarun))
print(str(rani))
