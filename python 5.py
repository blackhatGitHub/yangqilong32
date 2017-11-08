Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> inport re.match
SyntaxError: invalid syntax
>>> import re.match

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import re.match
ImportError: No module named match
>>> improt re
SyntaxError: invalid syntax
>>> import re
>>> line = 'Cat are smarter than dogs'
>>> matchobj = re.match(r'dogs',line,re.M|re.I)
>>> matchobj.group()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    matchobj.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> matchobj = re.match(r'cat',line,re.M|re.I)
>>> matchobj.group()
'Cat'
>>> matchobj = re.search(r'are',line,re.M|re.I)
>>> print matchobj.group
<built-in method group of _sre.SRE_Match object at 0x02052218>
>>> print matchobj.group()
are
>>> matchobj=re.serarch(r'^cat.*dogs$',line,re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    matchobj=re.serarch(r'^cat.*dogs$',line,re.M|re.I)
AttributeError: 'module' object has no attribute 'serarch'
>>>  matchobj = re.serarch(r'^cat.*dogs$',line,re.M|re.I)
 
  File "<pyshell#13>", line 2
    matchobj = re.serarch(r'^cat.*dogs$',line,re.M|re.I)
    ^
IndentationError: unexpected indent
>>> matchobj = re.serarch(r'^cat.*dogs$',line,re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    matchobj = re.serarch(r'^cat.*dogs$',line,re.M|re.I)
AttributeError: 'module' object has no attribute 'serarch'
>>> line = 'Cat are smarter than dogs'
>>> matchobj = re.serarch(r'^cat.*dogs$',line,re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    matchobj = re.serarch(r'^cat.*dogs$',line,re.M|re.I)
AttributeError: 'module' object has no attribute 'serarch'
>>> matchobj = re.serarch(r'^cat .* dogs$',line,re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    matchobj = re.serarch(r'^cat .* dogs$',line,re.M|re.I)
AttributeError: 'module' object has no attribute 'serarch'
>>> matchobj = re.serarch(r'^Cat.*dogs$',line,re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    matchobj = re.serarch(r'^Cat.*dogs$',line,re.M|re.I)
AttributeError: 'module' object has no attribute 'serarch'
>>> matchobj = re.serarch(r'^cat',line,re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    matchobj = re.serarch(r'^cat',line,re.M|re.I)
AttributeError: 'module' object has no attribute 'serarch'
>>> matchobj = re.serarch(r'cat',line,re.M|re.I)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    matchobj = re.serarch(r'cat',line,re.M|re.I)
AttributeError: 'module' object has no attribute 'serarch'
>>> matchobj = re.search(r'^cat.*dogs$',line,re.M|re.I)
>>> print matchobj.group
<built-in method group of _sre.SRE_Match object at 0x020521E0>
>>> pint matchobj.group()
SyntaxError: invalid syntax
>>> print matchobj.group()
Cat are smarter than dogs
>>> matchobj = re.search(r'^cat',line,re.M|re.I)
>>> print matchobj.group()
Cat
>>> line = 'Cat are dogs simary than'
>>> matchobj=re.search(r'dogs$',line,re.M|re.I)
>>> print matchobj.group()

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print matchobj.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> matchobj=re.search(r'than$',line,re.M|re.I)
>>> print matchobj.group()
than
>>> 
