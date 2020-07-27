import array
arr= array.array('i',[1, 2, 3, 1, 5])  
print("The new created array is: ", end = " ")
for i in range(0,5):
	print(arr[i], end = " ")
	
print("\r")	
print ("The index of 1st occurrence of 2 is : ",end="") 
print (arr.index(2)) 	
print("The popped element is: ", end = " ")
print(arr.pop(4))

print("The array after popping is: ", end = " ")
for i in range(0,4):
	print(arr[i], end = " ")

print("\r")
arr.remove(1)
print("The array after removing is: ", end = " ")
for i in range(0,3):
	print(arr[i], end = " ")
	
print("\r")	
arr.reverse()  
print ("The array after reversing is : ",end="") 
for i in range (0,3): 
    print (arr[i],end=" ") 			
