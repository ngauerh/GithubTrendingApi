import requests
from bs4 import BeautifulSoup
import time
from models import Languages
from config import GithubLanguages, SinceDate
from db_access import create_threading, create_languages, del_api

base_url = 'https://github.com/trending/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
}


def crawl(url, since, lang=None):
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    li_list = soup.find_all('li', {"class": "col-12 d-block width-full py-4 border-bottom"})
    for li in li_list:
        # 语言 language
        try:
            language = li.find('span', {"itemprop": "programmingLanguage"}).text.replace(' ', '').replace('\n', '')
        except Exception as e:
            language = ''

        # 仓库名
        a = li.h3.text.split('/')
        repo = a[1].replace(' ', '').replace('\n', '')

        # 仓库拥有着
        user = a[0].replace(' ', '').replace(' ', '').replace('\n', '')

        # 简介
        try:
            about = li.find_all('p', {'class': "col-9 d-inline-block text-gray m-0 pr-4"})[0].text.replace('\n', '').strip()
        except:
            about = ''

        # 链接
        link = 'https://github.com/' + li.h3.text.replace(' ', '').replace('\n', '')

        # star
        stars = li.find_all('a', {'class': "muted-link d-inline-block mr-3"})[0].text.replace(' ', '').replace('\n', '')

        # fork
        try:
            forks = li.find_all('a', {'class': "muted-link d-inline-block mr-3"})[1].text.replace(' ', '').replace('\n', '')
        except:
            forks = 0

        # 新增star
        try:
            new_stars = li.find('span', {'class': "d-inline-block float-sm-right"}).text.replace('\n', '').strip()
        except:
            new_stars = ''
        # 贡献者头像地址合集
        avatars = []
        ava = li.find_all('img', {'class': 'avatar mb-1'})
        for _ in ava:
            avatars.append(_.get('src'))

        api_info = {
            # 项目语言
            'language': language,
            # 项目名称
            'repo': repo,
            # 仓库拥有着
            'user': user,
            # 项目描述
            'about': about,
            # 项目地址
            'link': link,
            # star数
            'stars': stars,
            # fork数
            'forks': forks,
            # 新增star
            'new_stars': new_stars,
            # 头像合集
            'avatars': ", ".join(avatars),
            # 时间
            'sincedate': since,
        }

        print(api_info)
        create_threading(**api_info)
    del_api(lang, since)


# 获取所有语言
def get_lang(url):
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    lang_list = soup.find_all('span', {"class": "select-menu-item-text js-select-button-text js-navigation-open"})

    obj = []
    for lang in lang_list:
        obj.append(Languages(language=lang.string))
    create_languages(obj)


def get_url():
    crawl(base_url, 'default')
    for lang in GithubLanguages:
        for since in SinceDate:
            url = base_url + lang + '?' + 'since=' + since
            try:
                crawl(url, since, lang)
                time.sleep(5)
            except:
                continue


if __name__ == '__main__':
    # get_url()
    get_lang(base_url)

