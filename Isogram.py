Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def is_isogram(string):
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		count = 0
		for word in string:
			if letter == word.lower():
				count +=1
		if count > 1:
			return False
	return True
