class person:
	counter=0
	def __init__(self, a='Tarun', b ='Male'):
		self.name=a
		self.gender=b
		person.counter=person.counter+1
	def ShowInfo(self):
		print("Name: ", self.name)
		print("Gender: ", self.gender)
	@classmethod
	def ShowCount(cls):
		print("Number of objects created so far:",cls.counter)			
