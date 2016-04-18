import urllib
import urllib2
import re


class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    def replace(self, x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()


class ZhiHu:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        self.tool = Tool()

    def getPage(self):
        try:
            url = self.baseUrl
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"the error is ",e.reason
                return None

    # def getAuthor(self):
    #     author = self.getPage()
    #     pattern = re.compile('<a class="author-link.*?>(.*?)</a>', re.S)
    #     result = re.search(pattern, author)
    #     if result:
    #
    #         return result.group(1).strip()
    #     else:
    #         return None

    def getContent(self, page):
        pattern = re.compile('<div class="zm-editable-content clearfix.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print u"------------------------------------------------------------------------------------------------------------------------------------\n"
            print self.tool.replace(item)


baseURL = 'https://www.zhihu.com/question/35256075#answer-31872995'
zhihu = ZhiHu(baseURL)
zhihu.getContent(zhihu.getPage())


