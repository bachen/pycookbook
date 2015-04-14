#coding=utf-8
import re
'''
．表示任意字符
［］用来匹配一个指定的字符类别，所谓的字符类别就是你想匹配的一个字符集，对于字符集中的字符可以理解成或的关系。
^ 如果放在[]内字符集的开头，则表示取非的意思。[^5]表示除了5之外的其他字符。而如果^不在字符串的开头，则表示它本身。
$ 匹配字符串结尾或换行符之前
\ 取消所有元字符
| 表示 或 

具有重复功能的元字符：
* 对于前一个字符重复0到无穷次
+ 对于前一个字符重复1到无穷次
？对于前一个字符重复0到1次
{m,n} 对于前一个字符重复次数在为m到n次，其中，{0,} = *,{1,} = , {0,1} = ?
{m} 对于前一个字符重复m次

\d 匹配任何十进制数；它相当于类 [0-9]。
\D 匹配任何非数字字符；它相当于类 [^0-9]。
\s 匹配任何空白字符；它相当于类 [ fv]。
\S 匹配任何非空白字符；它相当于类 [^ fv]。
\w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
\W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。
'''
# re.search函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回，如果字符串没有匹配，则返回None
# 不在[]元字符内的^，表示在字符串中去匹配以ab开头；
# ^也可以用在多行模式匹配换行符之后：m=re.findall("^a\w+","abcdfa\na1b2c3",re.MULTILINE)
m = re.search("^ab+","afdfaaabb")
print m
m = re.search("ab+","afdfaaabb")
print m
# 在[]元字符内的^，表示除元字符内的任意字符
m = re.search("[^abc]","abcd")
print m
m = re.findall("^a\w+","abcdfa\na1b2c3",re.MULTILINE)
print m
# re.match 尝试从字符串的开始匹配一个模式，如：下面的例子匹配第一个单词。 
m = re.match(r"he","he is a policeman")
print m
m = re.match(r"he","she is a policeman")
print m
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s", text)
if m:
	print m.group(0), '\n', m.group(1)
else:
	print 'not match'

#re.match与re.search的区别：
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
#而re.search匹配整个字符串，直到找到一个匹配, 则返回。

#{m},用来表示前面正则表达式的m次copy，如"a{5}"，表示匹配5个”a”,即"aaaaa"
#{m,n}?,表示尽可能少的匹配
print re.findall("a{2,4}?","aaaaaaaaaaa")

#re.sub的函数原型为：re.sub(pattern, repl, string, count),count
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print re.sub(r'\s+', '-', text,0)