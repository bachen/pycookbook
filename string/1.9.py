import string

def translator(frm='',to='',delete='',keep=None):
	if len(to) == 1:
		to = to *len(frm)
	t = string.maketrans(frm,to)
	if keep is not None:
		allchars = string.maketrans('','')
		delete = allchars.translate(allchars,keep.translate(allchars,delete))
	def translate(s):
		return s.translate(t,delete)
	return translate

digits_only = translator(keep = string.digits)
print digits_only('CHris-Pin : 240-012')
digits_only = translator(frm = string.digits,to = '#')
print digits_only('CHris-Pin : 240-012')

def test_closure(name='',operators=None):
	if operators is not None:
		name = ' world'
	else:
		name = ' python'

	def oper(s):
		return s + name
	return oper

test1 = test_closure(operators='s')
print test1('hello')
test1 = test_closure()
print test1('hello')