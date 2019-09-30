import urllib.request
import xml.etree.ElementTree as ET
import datetime

def build_verbs():
    list = [str(datetime.datetime.today()), 'Today News', 'Business News', 'Agenda', 'India', 'USA', 'America', 'Boris Johnson', 'Trump', 'Trump Tower', 'Stock Market', 'Delhi', 'Modi', 
    'Amit Shah', 'Modi Shah', 'PlayStattion New', 'New Games', 'Cricket', 'Premium League', 'Alexa Tricks', 'Google Home Tricks', 'Pakistan', 'Judo', 
    'Obama', 'Iran', 'Oil Price', 'Gold Price', 'Silver Price', 'BitCoin', 'BitCoin Price', 'Pound to US Dollar', 'Pound to Euro', 'Jobs Market', 'Etherium', 
    'Crypto Currency', 'Magnum', 'Property Prices', 'Property Market', 'Movies this week', 'Banking Sector', 'Auto Sector', 'Recession', 'BBC News', 
    'Travel', 'Travel deals this month', 'Bollywood movies', 'Now Showing', 'Money', 'Finance', 'Sports', 'Page 3', 'Showcase', 'Media', 'Microsoft', 
    'Google', 'New Era', 'Drum beats', 'Baseball', 'Match of the day', 'World news', 'BBC World', 'MSN', 'Bing', 'Letter Z', 'Postoffice', 'Random number']
    
    sources = ['https://trends.google.com/trends/trendingsearches/daily/rss?geo=US',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=GB',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=IN',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=DE',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=FR',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=CA',
        'https://trends.google.com/trends/trendingsearches/daily/rss?geo=MY']

    for src in sources:
        contents = urllib.request.urlopen(src).read()
        root = ET.ElementTree(ET.fromstring(contents)).getroot()
        for tag in root.iterfind('channel/item/title'):
            list.append(tag.text)

    print(len(list), list)
        
    verbs = ",".join(list);
    print(f'Verbs String:: {verbs}')
    with open('verbs.html', 'w', encoding="utf-8") as f:
        print('Writing verbs to verbs.html')
        f.write(verbs)
        
    with open('verbs.html','r') as f:
        cos = f.read()
        print('verbs.html:: ' + cos)

if __name__ == '__main__':
    build_verbs()
