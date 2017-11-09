Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> import re
>>>  re.findall('\w+@\w+\.com',y)
 
  File "<pyshell#2>", line 2
    re.findall('\w+@\w+\.com',y)
    ^
IndentationError: unexpected indent
>>> re.findall('\w+@\w+\.com',y)
['123@qq.com', 'aaa@163.com', 'bbb@126.com']
>>> y = 'tel:010-12345678 address:changanRoad'
>>> re.findall('\d{3}-\d{8}',y)
['010-12345678']
>>> y = 'tel:010-12345678 address:changanRoad other tall:1054-98765432'
>>> re.findall('\d{3,4}-\d{7,8}',y)
['010-12345678', '1054-98765432']
>>> y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> re.findall('\w@(?:qq|163|126).com',y)
['3@qq.com', 'a@163.com', 'b@126.com']
>>> re.findall('\w+@(?:qq|163|126).com',y)
['123@qq.com', 'aaa@163.com', 'bbb@126.com']
>>> 
