import requests




def save():
    response = requests.get('https://www.melon.com/chart/index.htm')
    source = response.text

    with open('melon.html', 'wt') as f:
        f.write(source)

if __name__ == '__main__':
    save()

