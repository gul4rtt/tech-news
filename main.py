from types import NoneType
import requests
import itertools
from bs4 import BeautifulSoup

print(" ____  ____   ____   _____ _____ ____ _   _   _   _ _______        ______  ");
print("| __ )| __ ) / ___| |_   _| ____/ ___| | | | | \ | | ____\ \      / / ___| ");
print("|  _ \|  _ \| |       | | |  _|| |   | |_| | |  \| |  _|  \ \ /\ / /\___ \ ");
print("| |_) | |_) | |___    | | | |__| |___|  _  | | |\  | |___  \ V  V /  ___) |");
print("|____/|____/ \____|   |_| |_____\____|_| |_| |_| \_|_____|  \_/\_/  |____/ \n");
page = input("Digite o número da página que deseja ler os tópicos [ex: 1]: ");
print('\n----------------------------------------------------------------------------\n');

if(page == '0'):
    page = '1';

website = requests.get("https://www.bbc.com/portuguese/topics/c404v027pd4t/page/" + page);
content = BeautifulSoup(website.content, "html.parser");

news = content.find_all('span', attrs={'class': 'lx-stream-post__header-text'});
description = content.find_all('p', attrs={'class': 'qa-story-summary'});

for a, b in itertools.zip_longest(news, description):
    if(type(b) == NoneType):
        continue;

    print((a.text).upper());

    if(type(b) == NoneType):
        continue;

    print(b.text + '\n');
