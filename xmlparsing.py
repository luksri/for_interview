import os
import xml.etree.ElementTree as et

tree = et.parse('sample.xml')

root = tree.getroot()

#for each in root:
 #   print(each.tag)
print(root)
for child in root:
    print(child)
    for element in child:
        print(element.tag+" "+element.text)


new_element = et.SubElement(root,'movie',attrib={'title':'kurukeshtra'})
new_element_type = et.SubElement(new_element,'type')
new_element_format = et.SubElement(new_element,'format')
new_element_rating = et.SubElement(new_element,'rating')
#new_element_stars = et.SubElement(new_element,'stars')
#new_element_description = et.SubElement(new_element,'description')

new_element_type.text = 'ancient'
new_element_format.text = 'cd'
new_element_rating.text = 'P'

tree.write('sample.xml')