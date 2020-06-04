import urllib.request
import xml.etree.ElementTree as ET
import datetime

def build_stack():
    contents = None
    with open('stack.txt','r') as f:
        contents = f.readlines()
    stack = [x.strip() for x in contents] 
    
    sources = [
        'https://stackoverflow.com/feeds/tag/.net',
        'https://stackoverflow.com/feeds/tag/python',
        'https://stackoverflow.com/feeds/tag/angular',
        'https://stackoverflow.com/feeds/tag/asp.net',
        'https://stackoverflow.com/feeds/tag/javascript'
        ]

    for src in sources:
        contents = urllib.request.urlopen(src).read()
        root = ET.ElementTree(ET.fromstring(contents)).getroot()
        ns = {"ns":"http://www.w3.org/2005/Atom"}
        for tag in root.findall('ns:entry/ns:title', ns):
            stack.append(tag.text)

    stack = list(dict.fromkeys(stack))
    print(f'Final Stack:: {stack}')
    
    contents = "\n".join(stack);
    print(f'Stack String:: {contents}')
    with open('stack.txt', 'w', encoding="utf-8") as f:
        print('Writing stack to stack.txt')
        f.write(contents)
        
    with open('stack.txt','r') as f:
        cos = f.read()
        print('stack.txt:: ' + cos)
        
if __name__ == '__main__':
    build_stack()
