import urllib.request
import xml.etree.ElementTree as ET

def build_verbs():
    list = []
    sources = ['https://trends.google.com/trends/trendingsearches/daily/rss?geo=US',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=GB',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=IN',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=DE']

    for src in sources:
        contents = urllib.request.urlopen(src).read()
        root = ET.ElementTree(ET.fromstring(contents)).getroot()
        for tag in root.iterfind('channel/item/title'):
            list.append(tag.text)

    print(len(list), list)
        
    with open('verbs.html', 'a') as f:
        f.write(",".join(list)+',')
        
    with open('verbs.html','r') as f:
        cos = f.read()
        print('file:: ' + cos)

if __name__ == '__main__':
    build_verbs()
