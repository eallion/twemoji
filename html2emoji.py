# usage: python3 html2emoji.py xxxxxx.txt > output.json
# copy html from https://www.emojiall.com/zh-hans/categories/A <div class="page_emoji_list"> to xxxxxx.txt

import json
import sys
from bs4 import BeautifulSoup

html_file = sys.argv[1] 

with open(html_file) as f:
    soup = BeautifulSoup(f, 'html.parser')

emojis = []
for card in soup.find_all('div', class_='emoji_card'):
    emoji = card.find('a', class_='emoji_font')
    name = card.find('a', class_='emoji_name')
    emojis.append({
        "icon": emoji.text, 
        "text": str(name.text)
    })

print(json.dumps(emojis, ensure_ascii=False, indent=2))