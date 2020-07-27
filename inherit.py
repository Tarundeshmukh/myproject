class Quadrilateral:
	def __init__(self,a,b,c,d):
		self.side1=a
		self.side2=b
		self.side3=c
		self.side4=d
	def perimeter(self):
		p=self.side1+self.side2+self.side3+self.side4
		print("perimeter: ",p)

class Rectangle(Quadrilateral):
	def __init__(self,a,b,c=None,d=None):
		super().__init__(a,b,c,d)
		self.side1=self.side3
		self.side2=self.side4	

q1 = Quadrilateral(10,20,30,40)
q1.perimeter()

r1 = Rectangle(1,2,3,4)
r1.perimeter()				
