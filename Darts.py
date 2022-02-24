Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def score(x, y):
    r = (x**2+y**2)**0.5
    return (r<=1)*5+(r<=5)*4+(r<=10)*1
