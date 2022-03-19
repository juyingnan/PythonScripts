from html.parser import HTMLParser
import urllib
import re

urlText = []
#定义HTML解析器
class parseText(HTMLParser):
    def handle_data(self, data):
        if data != '/n':
            urlText.append(data)

def cdata_process(self, data):
    # 创建HTML解析器的实例
    lParser = parseText()
    rgx = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")
    m = rgx.search(data)
    test2 = m.group(1)
    # print( test2)

    # 把HTML文件传给解析器
    lParser.feed(test2)
    lParser.close()
    result = ""
    for string in urlText:
        result += string

    # print(result)
    return result

#创建HTML解析器的实例
lParser = parseText()

test='<![CDATA[My favorite farrier finally on the web, check him out <a href="http://t.co/OOqnTHLn" rel="nofollow" dir="ltr" data-expanded-url="http://www.AndrewElsbree.com" class="twitter-timeline-link" target="_blank" title="http://www.AndrewElsbree.com" ><span class="tco-ellipsis"></span><span class="invisible">http://www.</span><span class="js-display-url">AndrewElsbree.com</span><span class="invisible"></span><span class="tco-ellipsis"><span class="invisible">&nbsp;</span></span></a> -- the best for all disciplines, sound feet = happy horses!!!]]>'
rgx = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")
m = rgx.search(test)
test2=m.group(1)
#print( test2)

#把HTML文件传给解析器
lParser.feed(test2)
lParser.close()
result = ""
for string in urlText:
    result+=string

print(result)

aa = cdata_process(test)
print( aa)

