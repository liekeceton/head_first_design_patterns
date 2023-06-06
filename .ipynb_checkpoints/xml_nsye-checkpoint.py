#Reading and parsing XML files

import xml.etree.ElementTree

try:
    tree = xml.etree.ElementTree.parse('nyse.xml')
except FileNotFoundError:
    print('File not found')
except xml.etree.ElementTree.ParseError:
    print('There was an error with parsing the element tree')
except:
    print('Something went wrong')
    
root = tree.getroot()
print('COMPANY \t\t\t\t LAST   CHANGE  MIN     MAX \n ----------------------------------------------------------------------')

for stock in root:
    print(F"{stock.text}")
    print(F"\t\t\t\t\t{stock.attrib['last']}\t{stock.attrib['change']}\t{stock.attrib['min']}\t{stock.attrib['max']}", sep='')