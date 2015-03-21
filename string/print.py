thefile = file('test.txt','w')
sometext = 'the text'
print >> thefile,sometext
thefile.write(sometext)
thefile.close()

print r"thie is a original\
string..."

print u'Hello\u0020World'

s = "I'm a string"
results = [ i*2 for i in s]
print results