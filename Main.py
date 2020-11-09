import requests
from bs4 import BeautifulSoup
import httplib2
import os


def downloader(list_links, coun):
    route = 'D://JoyCreator/'
    for i in range(len(list_links)):
        h = httplib2.Http()
        content = h.request(list_links[i])
        type_file = list_links[i][list_links[i].rfind('.') + 1:]
        name = open(f'{route}{coun}.{type_file}', 'wb')
        coun += 1
        name.write(content[1])
        name.close()


try:
    os.mkdir('D://JoyCreator')
except FileExistsError:
    pass

counter = 1
list_of_links = []
for num_page in range(1, 10765):
    print(f'{num_page}/10764')
    page = requests.get(f'http://joyreactor.cc/best/{num_page}')
    text = page.content
    page.close()
    soup = BeautifulSoup(text, features='html.parser')
    posts_on_page = soup.find('div', {'id': 'post_list'})
    for p in posts_on_page:
        images = p.find_all('div', {'class': 'image'})
        for i in images:
            link_image = i.find_all('img')
            for l in link_image:
                list_of_links.append(l['src'])
    downloader(list_of_links, counter)
    counter += len(list_of_links)