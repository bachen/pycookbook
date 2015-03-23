def reindent(s,numSpaces):
	leading_space = numSpaces * ' '
	lines = [ leading_space + line.strip() for line in s.splitlines()]
	return "\n".join(lines)

x = '''
 I'm testing, my function,
    I'm not sure whether it is OK.
   let us see the result.
'''
print reindent(x,5)

def addSpace(s,numAdd):
	white = " " * numAdd
	return white + white.join(s.splitlines(True))
def numSpaces(s):
	return [len(line) - len(line.lstrip()) for line in s.splitlines()]
def delSpaces(s,numDel):
	if numDel > min(numSpaces(s)):
		raise ValueError, "Error: removing more spaces than there are ! "
	return "\n".join([ line[numDel:] for line in s.splitlines()])

def undent(s):
	return delSpaces(s,min(numSpaces(s)))
print addSpace(undent(x),2)