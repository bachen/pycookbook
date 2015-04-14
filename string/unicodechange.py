unicodestring = u'hello world'
utf8string = unicodestring.encode('utf-8')
asciistring = unicodestring.encode('ascii')
isostring = unicodestring.encode('iso-8859-1')
utf16string = unicodestring.encode('utf-16')

s1 = unicode(utf8string,'utf-8')
s2 = unicode(asciistring,'ascii')
s3 = unicode(isostring,'iso-8859-1')
s4 = unicode(utf16string,'utf-16')

assert s1==s2==s3==s4