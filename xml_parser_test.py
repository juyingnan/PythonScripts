from xml.dom import minidom
xmldoc = minidom.parse('test.xml')

instancelist = xmldoc.getElementsByTagName('instance')
print(len(instancelist))
for instance in instancelist:
    print(instance.attributes['id'].value)

answerlist = xmldoc.getElementsByTagName('answer')
print(len(answerlist))
for answer in answerlist:
    print(answer.attributes['senseid'].value)

contextlist = xmldoc.getElementsByTagName('context')
print(len(contextlist))
for context in contextlist:
    print(context.firstChild.nodeValue)