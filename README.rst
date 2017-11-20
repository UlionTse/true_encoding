**crawl_requests**
==================

*Usage:*
--------
>>>import requests
<<<<<<< HEAD

>>>from true_encoding import Tcode ##

>>>res = requests.get('https://python.org')

>>>res.encoding = Tcode(res) ##

>>>content = res.text
=======

>>>from true_encoding import true_encoding ##

>>>response = requests.get('https://python.org')

>>>response.encoding = true_encoding(response) ##

>>>content = response.text
>>>>>>> fbe17a1e6995016a403e7353749554649412b8f9



