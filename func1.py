"""def myfunction(newlist):
	print("List accessed in function: ", "id: ", id(newlist))
	return
mylist=[10,20,30,40,50]
print("List before passing to function: ", "id: ", id(mylist))
myfunction(mylist)"""


def myfunction(newList):
	newList.append(60)
	print("modified list inside function: ", newList)
	return	
mylist=[10,20,30,40,50]
print("list before passing the function: ", mylist)
myfunction(mylist)
print("list after passing the function: ", mylist)	


"""def checkmoney(money):
    if money<7000 :
        print("Ahem, can you rethink this number please?")
    elif money>10000:
        print("Wow sis! You are a queen")
    elif money in range(7000,10001):
        print("Cool, thanks sis! {} rupees will certainly help.".format(money))

    return

sis=1699
checkmoney(sis)"""
