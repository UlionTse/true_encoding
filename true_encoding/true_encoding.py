import re

def encode_bug(self,res):
    if ((res.encoding == 'ISO-8859-1') or (res.encoding is None) or ('charset=gb2312' in res.text) or ('charset=GB2312' in res.text)):
        if (('charset=gb2312' in res.text) or ('charset=GB2312' in res.text)):#people.cn
            return 'gb2312'
        elif 'charset="' in res.text:
            pattern = re.compile('charset="(.*?)"', re.S)
            res.encoding = re.findall(pattern, res.text)[0]
            return res.encoding
        elif (('charset=utf-8' in res.text) or ('charset=UTF-8' in res.text)):
            return 'utf-8'
        elif (('charset=GBK' in res.text) or ('charset=gbk' in res.text)):
            return 'GBK'
        elif (('charset=cp936' in res.text) or ('charset=CP936' in res.text)):
            return 'cp936'
        else:
            return 'utf-8'
