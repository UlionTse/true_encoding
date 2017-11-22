import re

def Tcode(response):
    if ' charset="' in response.text: # space
        pattern = re.compile('charset="(.*?)"',re.S)
        return re.findall(pattern,response.text)[0]
    
    elif ('charset=utf-8' or 'charset=UTF-8') in response.text:
        return 'utf-8'
    elif ('charset=gb2312' or 'charset=GB2312') in response.text:
        return 'GB2312'
    elif ((('charset=GBK' or 'charset=gbk') in response.text) or (response.encoding=='ISO-8859-1')):
        return 'GBK'
    elif ('charset=cp936' or 'charset=CP936') in response.text:
        return 'cp936'
    elif ('charset=ascii' or 'charset=ASCII') in response.text:
        return 'ASCII'
    else:
        return response.encoding
