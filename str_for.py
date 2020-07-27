def print_formatted(number):
    for number in range(1,n+1):
    	a = print(str(number).rjust(x, ' '), str(oct(number)[2:]).rjust(x, ' '), str(hex(number)[2:]).rjust(x, ' '), str(bin(number)[2:]).rjust(x, ' '))
    	return a 
    
if __name__ == '__main__':
    n = int(input())
    x = len(bin(n)[2:])
    print_formatted(n)
    
    
    """n = int(input())
spacing = len(bin(n)[2:])

for i in range(1,n+1):
    print(str(i).rjust(spacing, ' '),str(oct(i)[1:]).rjust(spacing, ' '),str(hex(i)[2:].upper()).rjust(spacing, ' '),str(bin(i)[2:]).rjust(spacing, ' '))"""
