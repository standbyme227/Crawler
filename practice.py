# import requests
# import re
#
# # response = requests.get("https://www.melon.com/chart/index.htm")
#
# # with open("melon.html", "w") as f:
# #     f.write(response.text)
#
# source = open("melon.html", "rt", encoding='utf8').read()
# # print(source)
#
#
#
#
#
#
#
# # PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
# #
# # PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
# #
# # match_list = PATTERN_DIV_RANK01.finditer(source)
# #
# # title_list = list()
# #
# # for i in match_list:
# #     result = PATTERN_A_CONTENT.search(i.group())
# #     title_list.append(result.group(1))
# #
# #
# # PATTERN_DIV_RANK02 = re.compile(r'<div class="ellipsis rank02">.*?</div>', re.DOTALL)
# #
# # found_list = PATTERN_DIV_RANK02.finditer(source)
# #
# # artist_list = list()
# # for i in found_list:
# #     result = PATTERN_A_CONTENT.search(i.group())
# #     artist_list.append(result.group(1))
# #
# #
# # PATTERN_DIV_RANK03 = re.compile(r'<div class="ellipsis rank03">.*?</div>', re.DOTALL)
# #
# # found_list_03 = PATTERN_DIV_RANK03.finditer(source)
# #
# # album_list = list()
# # for i in found_list_03:
# #     result = PATTERN_A_CONTENT.search(i.group())
# #     album_list.append(result.group(1))
# #
# # result_list = list(zip(title_list, artist_list, album_list))
# #
# # final_list = list()
# #
# # count = 1
# #
# # for i in result_list:
# #     result_dict = dict()
# #     result_dict["rank"] = count
# #     result_dict["title"] = i[0]
# #     result_dict["artist"] = i[1]
# #     result_dict["album"] = i[2]
# #     final_list.append(result_dict)
# #     count += 1
# #
# # for i in final_list:
# #     print(i)
#
#
#
#
#
#
# """
# [
#     {"rank": 1, "title": "제목", "artist": "가수", "album": "앨범이름"},
#     .
#     .
#     .
# ]
#
# """
#
# # p = re.compile(r'^<.*?{attribute_name}="(?P<value>.*?)?".*?>', re.DOTALL)
#
#  # ?P<value> 그룹에 이름 붙이기 ?P<이름>
#
#
#
#
#
# def get_tag_attribute(attribute_name, tag_string):
#
#     p = re.compile(r'^<.*?{attribute_name}="(?P<value>.*?)?".*?>'.format(
#         attribute_name = attribute_name), re.DOTALL)
#     m = re.search(p, tag_string)
#     if m :
#         print(m.group())
#         return m.group('value')
#     return ''
#
# result = get_tag_attribute('src', source)
# print(result)
#
#
#
# def get_tag_content(tag_string)
#     p = re.compile(r'<.*?>(?P<value>.*?)</.*?>')
#     m = re.search(p, tag_string)
#     if m:
#         return m.group('value')
#     return ''
#
#
#
#
#
#
#
# #     if True :
# #         match_contentA = re.compile(r'<.*?{attribute_name}="(.*?)?".*?')
# #         result_1 = match_contentA.search(tag_string)
# #         return result_1.group()
# #
# #
# # def get_tag_content(tag_string):
# #     if True :
# #         re.compile(r'tag_string')
#
#
#
#


import re

source = '''
<div class="first-div">
    <div class="second-div">
        <span class="span-content">ABCD</span>
    </div>
</div>'
'''


def get_tag_attribute(attribute_name, tag_string):
    """
    특정 tag문자열(tag_string)에서 attribute_name에 해당하는 속성의 값을 리턴하는 함수
    :param attribute_name: 태그가 가진 속성명
    :return: 속성이 가진 값
    """
    p_first_tag = re.compile(r'^.*?<.*?>', re.DOTALL)
    first_tag = re.search(p_first_tag, tag_string).group()

    # 문자열 포맷에 이름 붙이고, format()에서 키워드인수로 전달
    p = re.compile(r'^.*?<.*?{attribute_name}="(?P<value>.*?)".*?>'.format(
        attribute_name=attribute_name
    ), re.DOTALL)
    m = re.search(p, first_tag)
    if m:
        return m.group('value')
    return ''


result = get_tag_attribute('class', source)
print(result)


def get_tag_content(tag_string):
    """
    특정 tag문자열(tag_string)이 가진 내용을 리턴
    tag문자열이 스스로 열고 닫는 태그 (ex: img태그)일 경우엔 공백을 반환
    :param tag_string:
    :return:
    """
    p = re.compile(r'<.*?>(?P<value>.*)</.*?>', re.DOTALL)
    m = re.search(p, tag_string)
    if m:
        return m.group('value')
    return ''


result2 = get_tag_content(source)
print(result2)