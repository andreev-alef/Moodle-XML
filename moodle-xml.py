import xml.etree.ElementTree as ET

tree = ET.parse("c:/Users/a.andreev/Downloads/вопросы-УЗД_11_2021-ТЕСТЫ УЗИ органов женского малого таза-20220111-1639.xml")
root = tree.getroot()

#<question type="multichoiceset">
for question in root.iter('question'):
    if question.attrib['type'] == 'multichoiceset':
        for answer in question.iter('answer'):
            if (float(answer.attrib['fraction']) != 100) & (float(answer.attrib['fraction']) != 0):
                answer.attrib['fraction']= '100'
                answer.set('update', 'no')
                
tree.write('!вопросы-УЗД_11_2021-ТЕСТЫ УЗИ органов женского малого таза-20220111-1639.xml', encoding="UTF-8", xml_declaration=True, method='xml')