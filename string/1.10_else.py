import sets

class Keeper(object):
	def __init__(self,keep):
		self.keep = sets.Set(map(ord,keep))

	def __getitem__(self,n):
		if n not in self.keep:
			return None
		return unichr(n)
	def __call__(self,s):
		return unicode(s).translate(self)

makefilter = Keeper

if __name__ == '__main__':
	test = makefilter('asdfg')
	print test('yesterday once more')