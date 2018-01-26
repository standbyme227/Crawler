import os
import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

# utils가 있는
PATH_MODULE = os.path.abspath(__file__)
print(f'path_module: \n{PATH_MODULE}')

# 프로젝트 컨테이너 폴더 경로
ROOT_DIR = os.path.dirname(PATH_MODULE)
print(f'root_dir: \n{ROOT_DIR}')

# data/ 폴더 경로
DATA_DIR = os.path.join(ROOT_DIR, 'data')
print(f'path_data_dir: \n{DATA_DIR}')

# Refactor (shift + fn + F6)



def get_top100_list(refresh_html=False):
    """
    실시간 차트 1~100위의 리스트 반환
    파일위치:
        data/chart_realtime.html
    :param refresh_html: True일 경우, 무조건 새 HTML파일을 사이트에서 받아와 덮어씀
    :return: 곡 정보 dict의 list
    """


    # 만약에 path_data_dir에 해당하는 폴더가 없을 경우 생성해준다
    os.makedirs(DATA_DIR, exist_ok=True)

    # 실시간 1~100위 웹페이지 주소
    url_chart_realtime = 'https://www.melon.com/chart/index.htm'

    # 실시간 1~100위 웹페이지 HTML을 data/chart_realtime.html 에 저장
    file_path = os.path.join(DATA_DIR, 'chart_realtime.html')
    try:
        # refresh_html매개변수가 True일 경우, wt모드로 파일을 열어 새로 파일을 다운받도록 함
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path, file_mode) as f:
            response = requests.get(url_chart_realtime)
            source = response.text
            f.write(source)
    # xt모드에서 있는 파일을 열려고 한 경우 발생하는 예외
    except FileExistsError:
        print(f'"{file_path}" file is already exists!')

    # 1. source변수에 위에 정의해놓은 file_path(data/chart_realtime.html)의
    #       파일 내용을 읽어온 결과를 할당
    f = open(file_path, 'rt')
    source = f.read()
    f.close()
    # 2. soup변수에 BeautifulSoup클래스 호출에 source를 전달해 만들어진 인스턴스를 할당
    #    soup = BeautifulSoup(source)
    soup = BeautifulSoup(source, 'lxml')
    # 3. BeautifulSoup을 사용해 HTML을 탐색하며 dict의 리스트를(result) 생성, 마지막에 리턴

    result = []
    for tr in soup.find_all('tr', class_=['lst50', 'lst100']):
        rank = tr.find('span', class_='rank').text
        title = tr.find('div', class_='rank01').find('a').text
        artist = tr.find('div', class_='rank02').find('a').text
        album = tr.find('div', class_='rank03').find('a').text
        song_id = tr.find('a', class_='song_info').get('href')
        url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
        # http://cdnimg.melon.co.kr/cm/album/images/101/28/855/10128855_500.jpg/melon/resize/120/quality/80/optimize
        # .* -> 임의 문자의 최대 반복
        # \. -> '.' 문자
        # .*?/ -> '/'이 나오기 전까지의 최소 반복
        p = re.compile(r'(.*\..*?)/')
        url_img_cover = re.search(p, url_img_cover).group(1)
        o = re.compile(r'.*?\'(.*).*?\'')
        song_id = re.search(o, song_id).group(1)
        result.append({
            'rank': rank,
            'title': title,
            'url_img_cover': url_img_cover,
            'artist': artist,
            'album': album,
            'song_id': song_id,
        })
    return result
    # print(result)



    song_id_list = []
    for tr in soup.find_all('tr', class_=['lst50', 'lst100']):
        song_id = tr.find('a', class_='song_info').get('href')
        o = re.compile(r'.*?\'(.*).*?\'')
        song_id = re.search(o, song_id).group(1)
        song_id_list.append({
            'song_id': song_id,
        })
    print (song_id_list)

    # url_song_info = 'http://www.melon.com/song/detail.htm?songId=30099927'





def get_song_detail(song_id, refresh_html=False):
    """
    song_id에 해당하는 곡 정보 dict를 반환
    위의 get_top100_list의 각 곡 정보에도 song_id가 들어가도록 추가
    http://www.melon.com/song/detail.htm?songId=30755375
    위 링크를 참조
    파일명
        song_detail_{song_id}.html
    :param song_id: Melon사이트에서 사용하는 곡의 고유 ID값
    :param refresh_html: 이미 다운받은 HTML데이터가 있을 때 기존 데이터를 덮어씌울지 여부
    :return: 곡 정보 dict
    """
    # 파일위치는 data/song_detail_{song_id}.html
    file_path = os.path.join(DATA_DIR, f'song_detail_{song_id}.html')
    try:
        file_mode = 'wt' if refresh_html else 'xt'
        with open(file_path, file_mode) as f:
            # url과 parameter구분해서 requests사용
            url = f'https://www.melon.com/song/detail.htm'
            params = {
                'songId': song_id,
            }
            response = requests.get(url, params)
            source = response.text
            file_length = f.write(source)
            if file_length < 10:
                raise ValueError('피알이 너무 짧습니다')
    except FileExistsError:
        print(f'"{file_path}" file is already exists!')
    except ValueError:
        os.remove(file_path)
        return

    source = open(file_path,'rt').read()


    # f = open(file_path, 'rt')
    # source = f.read()
    # f.close()

    soup = BeautifulSoup(source, 'lxml')

    song_info_list = []
    for div in soup.find_all('div', id=['conts']):
        info_title = div.find('h2', class_='title').text
        thumb_image = div.find('a', class_='image_typeAll').find('img').get('src')
        title = div.find('div', class_='song_name').strong.next_sibling.strip()
        # title = div.find('div', class_='song_name').get_text(strip= True)[2:]
        #title 부분은 내가 하지 못해서 선생님이 하신걸 적었기에, 다시해봐야한다.
        artist = div.find('a', class_='artist_name').text
        album_name = div.find('dl', class_='list').find('a').text
        release_day = div.find('dl',class_='list').find('dd').find_next_sibling('dd').text
        genre = div.find('dl', class_='list').find('dd').find_next_sibling('dd').find_next_sibling('dd').text
        flac = div.find('dl', class_='list').find('dd').find_next_sibling('dd').find_next_sibling('dd').find_next_sibling('dd').text
        comments_count = div.find('span', id='revCnt').text
        yesterday_rank = div.find('div', class_='chart').find('span', class_='num').text
        lyrics = div.find('div', id='d_video_summary').get_text()
        lyricist = div.find('div', class_='ellipsis artist').find('a').text
        composer = div.find('ul', class_='list_person clfix').find('li').find_next_sibling('li').find('a', class_="artist_name").text
        # arrangement = div.find('ul', class_='list_person clfix').find('li').find_next_sibling('li').find_next_sibling('li').find('a', class_="artist_name").text
        vod_thumb =  div.find('div', class_='section_movie').find('a').find('img').get('src')
        p = re.compile(r'(.*\..*?)/')
        thumb_image = re.search(p, thumb_image).group()
        p = re.compile(r'(.*\..*?)/')
        vod_thumb = re.search(p, vod_thumb).group()
        o = re.compile(r'((?!\s).)+(.*?)$', re.DOTALL)
        lyrics = re.search(o, lyrics).group()
        song_info_list.append({
            '곡정보': info_title,
            '앨범자켓': thumb_image,
            '곡명': title,
            '가수': artist,
            '앨범명': album_name,
            '발매일': release_day,
            '장르': genre,
            'FLAC': flac,
            '댓글수': comments_count,
            '어제의 차트순위': yesterday_rank,
            '가사': lyrics,
            '작사': lyricist,
            '작곡': composer,
            # '편곡': arrangement,
            '뮤비의 한 장면': vod_thumb,
            # 'artist': artist,
            # 'album': album,
            # 'song_id': song_id,
        })
    # return result
    pprint(song_info_list, indent=1)




    # url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
    # p = re.compile(r'(.*\..*?)/')
    # url_img_cover = re.search(p, url_img_cover).group(1)




    """
    song_id에 해당하는 곡 정보 dict를 반환
    위의 get_top100_list의 각 곡 정보에도 song_id가 들어가도록 추가
    url = f'http://www.melon.com/song/detail.htm?songId={song_id}'
    위 링크를 참조
    :param song_id: 곡 정보 dict
    :return:
    """