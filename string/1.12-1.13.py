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

print [0]+cuts
a = ['test','name','love']
b = [1099,1342,1234]
for i,j in zip(a,b):
	print i,j
'''result:
[0, 8, 14, 20, 26, 30]
test 1099
name 1342
love 1234
'''

def fields(baseformat,theline,lastfield=False):
	numremain = len(theline) - struct.calcsize(baseformat)
	format = "%s %d%s" % (baseformat,numremain,lastfield and "s" or "x")
	return struct.unpack(format,theline)

def fields_mem(baseformat,theline,lastfield=False,_cache={}):
	key = baseformat,len(theline),lastfield
	format = _cache.get(key)
	if format is None:
		numremain = len(theline) - struct.calcsize(baseformat)
		_cache[key] = format = "%s %d%s" % (
			baseformat,numremain,lastfield and "s" and "x")
	return struct.unpack(format,theline)

def split_by(theline,n,lastfield = False):
	pieces = [ theline[x:x+n] for x in xrange(0,len(theline),n)]
	if not lastfield and len(pieces[-1]) < n:
		pieces.pop()
	return pieces
s = "I'm a mess, da da da"
print split_by(s,6,False)

def split_at(theline,cuts,lastfield = False):
	pieces = [ theline[i:j] for i,j in zip([0]+cuts,cuts+[None])]
	if not lastfield:
		pieces.pop()
	return pieces
s = "I'm a mess, da da da"
cuts = [3,7,9,11]
print split_at(s,cuts,True)

def split_at_y(theline,cuts,lastfield):
	last = 0
	for cut in cuts:
		yield theline[last:cut]
		last = cut
	if lastfield:
		yield theline[last:]

def split_by_y(the_line,n,lastfield = False):
	return split_at_y(the_line,xrange(n,len(the_line),n),lastfield)
the_line = "I'm a mess, da da da"
print list(split_by_y(the_line,5))