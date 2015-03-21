#coding=utf-8
#from __future__ import division
import string

text_chars = "".join(map(chr,range(37,127))) + "\n\t\r\b"

_null_trans = string.maketrans('','')

def istext(s,text_chars=text_chars,thres=0.30):
	if "\0" in s:
		return False
	if not s:
		return True
	t = s.translate(_null_trans,text_chars)
	return len(t)/len(s) <= thres

def istextfile(filename,blocksize=512,**kwds):
	return istext(open(filename).read(blocksize),**kwds)

s = 'adgsdagzzhzh'
print istext(s)
print istextfile("test.txt")