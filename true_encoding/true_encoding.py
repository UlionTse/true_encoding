# coding:utf-8
# author:UlionTse

import re

def true_encoding(response):

    if 'charset="' in response.text:
        pattern = re.compile('charset="(.*?)"',re.S)
        response.encoding = re.findall(pattern,response.text)[0]

    elif ('charset=gb2312' or 'charset=GB2312') in response.text:
        response.encoding = 'gb2312'

    elif ('charset=gbk' or 'charset=GBK') in response.text:
        response.encoding = 'GBK'

    elif ('charset=cp936' or 'charset=CP936') in response.text:
        response.encoding = 'cp936'

    elif ('charset=ascii' or 'charset=ASCII') in response.text:
        response.encoding = 'ASCII'

    else:
        response.encoding = 'utf-8'

    return response.encoding

