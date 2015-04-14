import string,re

s = 'hello I will find u.'
rs = s.replace('ll','ss')

letter = ''' Dear $customer,
I hope you are having a great time.
If you do not find room $room.'''
letter_T = string.Template(letter)
print letter_T.substitute({'customer':'smith','room':309})

def make_xlat(*args,**kwds):
	adict=dict(*args,**kwds)
	rx = re.compile('|'.join(map(re.excape,adict)))
	def one_xlat(match):
		return adict[match.group(0)]
	def xlat(text):
		return rx.sub(one_xlat,text)
	return xlat

