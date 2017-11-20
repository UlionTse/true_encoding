**crawl_requests**
==================

*Usage:*
--------
>>>import requests
>>>from true_encoding import true_encoding ##

>>>response = requests.get('https://python.org')
>>>response.encoding = true_encoding(response) ##
>>>content = response.text



