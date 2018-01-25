import re
from bs4 import BeautifulSoup
from utils import get_top100_list


from bs4 import BeautifulSoup
import re

# source = open('melon.html', 'rt', encoding='utf8').read()
# soup = BeautifulSoup(source, 'lxml')

# for a in soup.find_all('a'):
#     print(a.get('href'))

# for td in soup.find_all('td'):
#     print(td)


# result = []
# for tr in soup.find_all('tr', class_='lst50'):
#     rank = tr.find('div', class_='wrap t_center').find('span').text
#     title = tr.find('div', class_='rank01').find('a').text
#     artist = tr.find('div', class_='rank02').find('a').text
#     album = tr.find('div', class_='rank03').find('a').text
#     url_img_cover = tr.find('a', class_ = 'image_typeAll').find('img').get('src')
#     # .* 임의문자 최대 반복
#     # \. '.'문자
#     # .*?/ '/'이나오기 전까지의 최소반복
#     p = re.compile(r'(.*\..*?)/')
#     url_img_cover = re.search(p, url_img_cover).group(1)
#
#     result.append({
#         'rank': rank,
#         'title': title,
#         'url_img_cover' : url_img_cover,
#         'articst' : artist,
#         'album' : album,
#     })
#
#     for item in result:
#         print(item)



# for tr in soup.find_all('tr', class_='lst50'):
#     title = tr.find('div', class_='rank01').find('a').text
#     print(title) #노래
#
#
# for tr in soup.find_all('tr', class_='lst50'):
#     artist = tr.find('div', class_='rank02').find('a').text
#     print(artist) #아티스트
#
# for tr in soup.find_all('tr', class_='lst50'):
#     album = tr.find('div', class_='rank03').find('a').text
#     print(album) #앨범


if __name__ == '__main__':
    result = get_top100_list()