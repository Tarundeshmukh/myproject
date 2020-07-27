class Intern:
	increment = 1
	no_of_interns = 0
	 
	def __init__(self, fname, lname, salary):
		self.fname = fname
		self.lname = lname
		self.salary = salary
		Intern.no_of_interns += 1
			
	def increase(self):
		self.salary = self.salary * Intern.increment
		
	@classmethod
	def change_increment(cls, amount):
		cls.increment = amount
	
	@classmethod
	def from_str(cls, emp_string):
		fname, lname, salary = emp_string.split("-")
		return cls(fname, lname, salary)
	
	@property
	def email(self):
		if self.fname == None:
			return "Email not set"
		else:	
			return self.fname + "." + self.lname + "@email.com"
	
	@email.setter
	def email(self, given_email):
		name_list = given_email.split("@")[0].split(".")
		print(name_list)
		self.fname = name_list[0]
		self.lname = name_list[1]
		
	@email.deleter
	def email(self):
		self.fname = None
		self.lname = None
			
	@staticmethod
	def isopen(day):
		if day == "sunday":
			return False
		else: return True
	
if __name__ == "__main__":
	t1 = Intern("Tarun", "Deshmukh", 10000)
	t2 = Intern("Tanya", "Deshmukh", 15000)	
	
print(t1.email, "\n", t2.email)
t2.lname = "Rai"
print(t2.email)
t2.email = "Rai.Tanya@gmail.com"
print(t2.email)	
del t2.email
print(t2.email)
#t2.email = "destan@gmail.com"
