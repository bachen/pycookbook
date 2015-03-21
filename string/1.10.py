#coding=utf-8
import string

allchars = string.maketrans('','')
def makefilter(keep):
	#生成补集，即所有不在keep的字符集合		
	delete = allchars.translate(allchars,keep)
	def thefilter(s):
		#将所有在补集中的字符从s中删除
		return s.translate(allchars,delete)
	return thefilter
if __name__=='__main__':

	digits_only = makefilter(keep = 'casd')
	print digits_only('chris-Pin : 240-012')