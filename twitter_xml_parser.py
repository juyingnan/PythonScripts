import xml.etree.ElementTree as ET
import os
from html.parser import HTMLParser
import pickle

# loop directory
def List(rootDir):
    result = []
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        result.append(path)
    return result


# HTML PARSER
class parseText(HTMLParser):
    def handle_data(self, data):
        if data != '/n':
            urlText.append(data)


folder = "C:\\Users\\bunny\\Desktop\\pan16-author-profiling-training-dataset-english-2016-04-25\\"
file_list = List(folder)
document_matrix = []
info_matrix = []
for file in file_list:
    if (file.endswith("xml")):
        tree = ET.parse(file)
        root = tree.getroot()
        info = []
        tweet = []
        info.append(file)
        info.append(root.attrib)
        for child in root:
            info.append(child.attrib)
            for document in child:
                attrib = document.attrib

                if document.text != None:
                    urlText = []
                    lParser = parseText()
                    test = document.text

                    # html -> parser
                    lParser.feed(test)
                    lParser.close()
                    result = ""
                    for string in urlText:
                        result += string
                else:
                    result = ""

                attrib["content"] = result
                tweet.append(attrib)

        info_matrix.append(info)
        document_matrix.append((tweet))
# test part
# print (info_matrix)
# print(document_matrix)

#pickle
# pickle.dump(info_matrix, open("info_matrix.txt", "wb"))
# pickle.dump(document_matrix, open("document_matrix.txt", "wb"))

# format print part
f = open('output', 'w')
print("[", file=f)
for file in document_matrix:
    print("[", file=f)
    for twi in file:
        print(twi['id'], twi['url'], twi['content'].encode('utf-8'), file=f)
    print("]", file=f)
print("]", file=f)
