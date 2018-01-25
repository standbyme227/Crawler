import requests
import os
import re


def get_top100_list(refresh_html=False):
    """
    실시간 차트 1~100위의 리스트 반환
    파일위치:
        현재 파일(모듈)의 위치를 사용한 상위 디렉토리 경로 (crawler디렉토리):
            os.path.dirname(os.path.abspath(__name__))
        1~50위:   data/chart_realtime_50.html
        51~100위: data/chart_realtime_100.html
    :return:
    """
# 프로젝트 컨테이너 폴더 경로
    path_module = os.path.abspath(__name__)
    print(f'path_module: {path_module}')

    root_dir = os.path.dirname(os.path.abspath(__name__))
    print(f'root_dir: {root_dir}')


# data/ 폴더 경로
    path_data_dir = os.path.join(root_dir, 'data')
    print(f'path_data_dir: {path_data_dir}')

    os.makedirs(path_data_dir, exist_ok=True)



# response = requests.get('https://www.melon.com/chart/index.htm')
#
# with open('/data/melon.html', 'w', "utf-8") as f:
#     f.write(response.text)
#
#
    # response = requests.get('https://www.melon.com/chart/index.htm')
    # source = response.text
    #
    # file_dir = os.path.join(path_data_dir, 'chart_realtime_50.html')
    # with open(file_dir, 'wt') as f:
    #     f.write(source)
    #
    # response = requests.get('https://www.melon.com/chart/index.htm#params%5Bidx%5D=51')
    # source = response.text
    #
    # file_dir = os.path.join(path_data_dir, 'chart_realtime_100.html')
    # with open(file_dir, 'wt') as f:
    #     f.write(source)
    url_chart_realtime_50 = 'https://www.melon.com/chart/index.htm'
    url_chart_realtime_100 = 'https://www.melon.com/chart/index.htm#params%5Bidx%5D=51'


    file_path = os.path.join(path_data_dir, 'chart_realtime_50.html')
    try :
        with open(file_path, 'xt') as f:
            response = requests.get(url_chart_realtime_50)
            source = response.text
            f.write(source)
    except FileExistsError:
        print(f'"{file_path}" file is already exists!')


    file_path = os.path.join(path_data_dir, 'chart_realtime_100.html')
    if not os.path.exist(file_path):
        response = requests.get(url_chart_realtime_100)
        source = response.text
        with open(file_dir, 'wt') as f:
            f.write(source)


    file_path = os.path.join(path_data_dir, 'chart_realtime_50.html')
    response = requests.get(url_chart_realtime_50)
    source = response.text
    with open(file_dir, 'wt') as f:
        f.write(source)

    file_path = os.path.join(path_data_dir, 'chart_realtime_100.html')
    response = requests.get(url_chart_realtime_100)
    source = response.text
    with open(file_dir, 'wt') as f:
        f.write(source)





# path_regex_dir = os.path.join(root_dir, 'regex')


# response = requests.get('https://www.melon.com/chart/index.htm')
# source = response.text
#
# file_dir = os.path.join(path_regex_dir, 'chart_realtime_50.html')
# with open(file_dir, 'wt') as f:
#     f.write(source)




# source = open('melon.html', 'r', "utf-8").read()
#
# print(source)



# 1~50, 50~100위 웹페이지 주소


# file_path = os.path.join(path_data_dir, 'abc.txt')
# print(f'file_path: {file_path}'





# def get_top100_list(refresh_html = False):
#
#
#     # cur_path = os.
#     # os.path.join(cur_path.'data')
#     # os.path.dirname(os.path.abspath(__name__))
#
#     path_module = os.path.abspath()
#
#
#     root_dir = os.path.dir(os.path.abspth(__name__))
#     path_date_dir = os.path.join(root_dir, 'data')
#     url_chart_realtime_50 = 'https://www.melon.com/chart/index.htm'
#     url_chart_realtime_100 = 'http://www.melon.com/chart/index.htm#params%5Bidx%5D=51'
#
#     file_path = os.path.join(path_date_dir, 'abc.txt')
#
#
#

    # file_path = os.path.join(path_date_dir, 'chart_realtime_50.html')
    # with open(file_path, 'wt') as f:
    #     response = requests.get(url_chart_realtime_50)
    #     source = response.text
    #     f.write(source)
    #
    # file_path = os.path.join(path_date_dir, 'chart_realtime_100.html')
    # with open(file_path, 'wt') as f:
    #     response = requests.get(url_chart_realtime_100)
    #     source = response.text

    #     f.write(source)
#
#
#     result = []
#     for tr in soup.find_all('tr', class_='lst50'):
#         rank = tr.find('div', class_='wrap t_center').find('span').text
#         title = tr.find('div', class_='rank01').find('a').text
#         artist = tr.find('div', class_='rank02').find('a').text
#         album = tr.find('div', class_='rank03').find('a').text
#         url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
#         # .* 임의문자 최대 반복
#         # \. '.'문자
#         # .*?/ '/'이나오기 전까지의 최소반복
#         p = re.compile(r'(.*\..*?)/')
#         url_img_cover = re.search(p, url_img_cover).group(1)
#
#         result.append({
#             'rank': rank,
#             'title': title,
#             'url_img_cover': url_img_cover,
#             'articst': artist,
#             'album': album,
#         })
#
#         # for item in result:
#         #     return(item)
#
#