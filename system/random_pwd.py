from random import choice
import string

def Genpassword(length=8,chars=string.letters+string.digits):
	return ''.join([choice(chars) for i in range(length)])

print Genpassword(9)