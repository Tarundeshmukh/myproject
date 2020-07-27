class car:
	def __init__(self, a=50):
		self.set_speed(a)
	def get_speed(self):
		return self._speed
	def set_speed(self,a):
		if a<=0 or a>=180:
			print("Speed needs to be between 0 and 180")
		else:
			self._speed=a				
