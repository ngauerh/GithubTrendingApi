import sys
from multiprocessing import Process
import schedule
import time

sys.path.append('../')

from repo_crawl import get_url as s1
from dev_crawl import get_url as  s3
from app import run as s2
from config import CRAWL_INTERVAL


def crawl():

    schedule.every(CRAWL_INTERVAL).hours.do(s1)

    while True:
        schedule.run_pending()
        time.sleep(60*60)


def dev_crawl():

    schedule.every(CRAWL_INTERVAL).hours.do(s3)

    while True:
        schedule.run_pending()
        time.sleep(60*60)


def run():
    p_list = list()
    p1 = Process(target=crawl, name='crawl')
    p_list.append(p1)
    p2 = Process(target=s2, name='s2')
    p_list.append(p2)
    p3 = Process(target=s3, name='s3')
    p_list.append(p3)

    for p in p_list:
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()