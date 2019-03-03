from xml.dom import minidom

file = minidom.parse('菜单.xml')
ingredients=file.getElementsByTagName('food')[0]
items=ingredients.getElementByTagName('name')
for item in items:
    num=item.getAttribute('')
print(file.hasChildNodes())
