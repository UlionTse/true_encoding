# coding:utf-8
# author:UlionTse

import re


def Tcode(response):
    if 'charset="' in response.text:
        pattern = re.compile('charset="(.*?)"',re.S)
        return re.findall(pattern,response.text)[0]

    elif ('charset=gb2312' or 'charset=GB2312') in response.text:
        return 'GB2312'

    elif ('charset=gbk' or 'charset=GBK') in response.text:
        return 'GBK'

    elif ('charset=cp936' or 'charset=CP936') in response.text:
        return 'CP936'

    elif ('charset=ascii' or 'charset=ASCII') in response.text:
        return 'ASCII'
    else:
        return 'utf-8'

