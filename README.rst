**true_encoding**
==================

*Usage:*
--------
>>> from true_encoding.debug import debug

>>> r = requests.get('http://www.dzwww.com/')
>>> print(r.text) ## Error: r.encoding == 'ISO-8859-1'

>>> r.encoding = debug(r)
>>> print(r.text) ## True: r.encoding == 'gb2312'

