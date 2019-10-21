Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List creating and searching
>>> end = False
>>> names = []
>>> for x in range(0,10):
	aname = input("enter first name:")
	names.append(aname)
	while not end:
		search = input("enter search name")
		if search == ("End"):
			end = True
			elif search in names:
				
SyntaxError: invalid syntax
>>> print(search, "was found")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(search, "was found")
NameError: name 'search' is not defined
>>> 
