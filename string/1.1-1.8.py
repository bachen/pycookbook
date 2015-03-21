#coding=utf-8
import sets,operator,re,sets,itertools,string

s1 = sets.Set('asbuflkafoijiasff')
s2 = sets.Set('jionalvnneiklsadehnvwd')
print ' '.join(s1 & s2)

s = 'test'
result = [ i*2 for i in s]
print ''.join(result)

#ASCII
print ord('a')
print chr(97)
#Unicode
print ord(u'\u0020')
print repr(unichr(32))
print map(ord,'ciao')
print ''.join(map(chr,range(74,78)))

obj1 = u'test123__中午'
obj2 = 123
def isAString(anobj):
	return isinstance(anobj,basestring)
print isAString(obj1)
print isAString(obj2)

def isStringLike(anobj):
	try:
		anobj + ''
	except:
		return False
	else:
		return True

#对齐
print '|','hello'.ljust(20),'|','hello'.rjust(20,'+'),'|','hello'.center(20,'-'),'|'

s = '      te te      '
print '|',s.rstrip(),'|',s.lstrip(),'|',s.strip(),'|'
s = 'xyusa yst yxyxy'
print '|'+ s.strip('xy') + '|'
#result: |usa yst |

pieces = ['aas','asd','acd']
ls = reduce(operator.add,pieces,'')
print ls

#reverse
s = 'testtest'
rs = s[::-1]
r = list(s)
r.reverse()
print rs,r
s = 'my name is eris.'
rs = ' '.join(s.split()[::-1])
print rs
revs = re.split(r'(\s+)',s) #split to a list of words
print revs
revs.reverse()
revs = ''.join(revs)
print revs
revstring = ''.join(reversed(s))
print revstring

aset = sets.Set(['a','b','s'])
print aset
seq = 'dcb'
def containsAny1(seq,aset):
	for c in seq:
		if c in aset:
			print c
			return True
	return False
print containsAny1(seq,aset)
def containsAny2(seq,aset):
	return bool(set(aset).intersection(seq))
print containsAny2(seq,aset)
def containsAny3(seq,aset):
	for item in itertools.ifilter(aset.__contains__,seq):
		return True
	return False
print containsAny3(seq,aset)

notrans = string.maketrans('','')
strset = 'adcs'
astr = 'das'
def containsAny(astr,strset):
	return len(strset) != len(strset.translate(notrans,astr))
def containsAll(astr,strset):
	return not strset.translate(notrans,astr)
print containsAll(astr,strset)
print containsAny(astr,strset)

