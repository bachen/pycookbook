input = open('file.txt','rU')
for line in input:
	line.strip("\n")
	print line
input.close()