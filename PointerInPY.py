#SoulProject Template: PointerInPY
#GPL 3 used
#Please make sure to remove debugging lines, if tested.
#Import this as: import SoulPIPY
#Have fun, Save your time :) & Send patches!!
#Modify code to make thousands of variables if needed?
def ptr():
	global ptr 
def ptrfree():
	global ptr
	ptr = 0
	print("Memory of pointer has set to 0")
		
def ptradd():
	global ptradd
	ptradd = ptr
	if print(id(ptradd)) == print(id(ptr)):
		ptradd = +1
	else:
		pass
def ptrfix():
	global ptrfix
	global ptr
	ptrfix = 992
	if ptr == 0:
		ptr = ptrfix
		print("ptr restored to max memory limit")
	else:
		pass

