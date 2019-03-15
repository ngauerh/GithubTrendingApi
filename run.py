import sys
from multiprocessing import Process
import schedule
import time

sys.path.append('../')

from repo_crawl import get_url as s1
from dev_crawl import get_url as s2
from repo_crawl import get_lang
from app import run as s3
from config import CRAWL_INTERVAL


def crawl():

    schedule.every(CRAWL_INTERVAL).hours.do(s1)
    schedule.every(CRAWL_INTERVAL).hours.do(s2)
    while True:
        schedule.run_pending()
        time.sleep(60*60)


def first_crawl():
    get_lang()
    s1()
    s2()


def run():
    first_crawl()
    p_list = list()
    p1 = Process(target=crawl, name='crawl')
    p_list.append(p1)
    p2 = Process(target=s3, name='s3')
    p_list.append(p2)

    for p in p_list:
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()