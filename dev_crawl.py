import requests
from bs4 import BeautifulSoup
import time
from config import GithubLanguages, SinceDate
from db_access import create_dev, del_dev

base_url = 'https://github.com/trending/developers/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
}


def crawl(url, since, lang):
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    users_list = soup.find_all('li', {"class": "d-sm-flex flex-justify-between border-bottom border-gray-light py-3"})
    for user in users_list:
        # 头像
        avatar = user.find('img', {"class": "rounded-1"}).get("src")

        user_ = user.find('h2', {"class": "f3 text-normal"})

        # 主页
        userlink = 'https://github.com' + user_.find('a').get('href')

        # 用户名
        username = ' '.join(user_.find('a').text.strip().split())

        # 人气仓库
        repo = user.find('span', {"class": "repo"}).text.strip()
        # 仓库简介
        repo_about = user.find('span', {"class": "repo-snipit-description css-truncate-target"}).text.strip()

        api_info = {
            'avatar': avatar,
            'username': username,
            'userlink': userlink,
            'repo': repo,
            'repo_about': repo_about,
            'lang': lang,
            'sincedate': since,

        }
        create_dev(**api_info)
    del_dev(lang, since)


def get_url():
    crawl(base_url, 'default', 'default')
    for lang in GithubLanguages:
        for since in SinceDate:
            url = base_url + lang + '?' + 'since=' + since
            try:
                crawl(url, since, lang)
                time.sleep(5)
            except:
                continue


if __name__ == '__main__':
    get_url()


