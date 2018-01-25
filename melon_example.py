import requests
import re

response = requests.get("https://www.melon.com/chart/index.htm")

# with open('melon.html', 'wt', encoding='utf8') as f:
#     f.write(response.text)

source = open("melon.html", "rt", encoding='utf8').read()
# print(source)

PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)

result_1 = PATTERN_DIV_RANK01.search(source)

PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

# print(result_1.group())

result = PATTERN_A_CONTENT.search(result_1.group())

print(result.group(1))

#search다음엔 패턴, 그리고 어디서찾을지 순서
#
# match_list = P1. finditer(source)
#
# for i in match_list:
#     print(i, group())
#     break

