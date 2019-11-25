#pip install beautifulsoup4
#pip install lxml
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > beautifulsoup4 > install
#pycharm > File > Settings... > Project:... > ProjectInterPerter > + > lxml > install

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버웹툰 > 연애혁명 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=570503")
    soup = BeautifulSoup(data,"lxml")
    # print(soup)
    cartoon_titles = soup.find_all("td", attrs={"class":"title"})
    for cartoon_title in cartoon_titles:
        title = cartoon_title.find("a").text
        print(title)
