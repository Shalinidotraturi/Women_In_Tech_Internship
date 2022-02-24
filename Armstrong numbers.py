Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def is_armstrong_number(number):
  number_text = str(number)
  count, size = 0, len(number_text)
    
  for i in number_text:
    count += int(i) ** size
      
  return count == number
