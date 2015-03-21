#coding=utf-8\
import string,struct
little = 'asfdg'
big = little.upper()
little = big.lower()
print big,little
test = 'one two three'
print test.capitalize()
print test.title()

'''result:
ASFDG asfdg
One two three
One Two Three
'''

notrans = string.maketrans('','')
def containAny(strs,strset):
	return len(strset) != len(strset.translate(notrans,strs))
def iscapitalized(s):
	return s == s.capitalize() and containAny(s,string.letters)

test = 'Asbi12435 @'
print iscapitalized(test)

baseformat = "5s 3x 8s 8s"
theline = 'fifthitsmyloveoomyloveooyesyes~yesyes~yesyes~'

l,s1,s2 = struct.unpack(baseformat,theline[:struct.calcsize(baseformat)])
print l,s1,s2

numremain = len(theline) - struct.calcsize(baseformat)
format = "%s %ds" % (baseformat,numremain)
l,s1,s2,t = struct.unpack(format,theline)
print l,s1,s2,t
'''result:
5s 3x 8s 8s 7s
fifth myloveoo myloveoo yesyes~
'''
cuts = [8,14,20,26,30]
pieces = [theline[i:j] for i,j in zip([0]+cuts,cuts+[None])]
print pieces