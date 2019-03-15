from sqlalchemy import desc
from models import *
import datetime

session = DBSession()


def create_threading(**kwargs):
    try:
        session.add(Api(repo=kwargs['repo'], language=kwargs['language'], user=kwargs['user'], about=kwargs['about'],
                        link=kwargs['link'], stars=kwargs['stars'], forks=kwargs['forks'], avatars=kwargs['avatars'],
                        new_stars=kwargs['new_stars'], sincedate=kwargs['sincedate']
                        ))
        session.flush()
    except Exception as e:
        print(str(e))
        session.rollback()


def create_dev(**kwargs):
    try:
        session.add(DevApi(avatar=kwargs['avatar'], username=kwargs['username'], userlink=kwargs['userlink'],
                           repo=kwargs['repo'], repo_about=kwargs['repo_about'], sincedate=kwargs['sincedate'],
                           lang=kwargs['lang']
                        ))
        session.flush()
    except Exception as e:
        print(str(e))
        session.rollback()


def del_api(*args):
    if not args[0]:
        api = session.query(Api).filter(Api.sincedate == args[1]).order_by(desc(Api.id)).all()
    else:
        api = session.query(Api).filter(Api.language == args[0], Api.sincedate == args[1]).order_by(desc(Api.id)).all()
    for i in api:
        tt = (datetime.datetime.now() - i.update_time).total_seconds()
        if tt > 1000:
            session.delete(i)
    session.flush()


def del_dev(*args):
    if not args[0]:
        api = session.query(DevApi).filter(DevApi.sincedate == args[1]).order_by(desc(DevApi.id)).all()
    else:
        api = session.query(DevApi).filter(DevApi.lang == args[0], DevApi.sincedate == args[1]).order_by(desc(DevApi.id)).all()
    for i in api:
        tt = (datetime.datetime.now() - i.update_time).total_seconds()
        if tt > 1000:
            session.delete(i)
    session.flush()


def create_languages(text):
    session.bulk_save_objects(text)


def get_api(*args):
    res = {"success": False, "count": 0, "msg": ""}
    if len(args) == 1:
        api = session.query(Api).filter_by(sincedate=args[0]).order_by(desc(Api.id)).all()
    else:
        api = session.query(Api).filter_by(language=args[0], sincedate=args[1]).order_by(desc(Api.id)).all()
    rr = []
    for i in api:
        zz = {
            # 仓库名称
            'repo': i.repo,
            # 语言
            'language': i.language,
            # 仓库拥有着
            'user': i.user,
            # 项目描述
            'about': i.about,
            # 项目地址
            'link': i.link,
            # star数
            'stars': i.stars,
            # fork数
            'forks': i.forks,
            # 新增star
            'new_stars': i.new_stars,
            # 头像合集
            'avatars': i.avatars.split(', '),

        }
        rr.append(zz)
    if not api:
        res["msg"] = "请求错误"
        return res
    res["success"] = True
    res["msg"] = rr
    res["count"] = len(rr)
    return res


def get_dev(*args):
    res = {"success": False, "count": 0, "msg": ""}
    if len(args) == 1:
        api = session.query(DevApi).filter_by(sincedate=args[0]).order_by(desc(DevApi.id)).all()
    else:
        api = session.query(DevApi).filter_by(lang=args[0], sincedate=args[1]).order_by(desc(DevApi.id)).all()
    rr = []
    for i in api:
        zz = {
            'username': i.username,
            'avatar': i.avatar,
            'userlink': i.userlink,
            'repo': i.repo,
            'repo_about': i.repo_about,
            }
        rr.append(zz)
    if not api:
        res["msg"] = "请求错误"
        return res
    res["success"] = True
    res["msg"] = rr
    res["count"] = len(rr)
    return res


def get_languages():
    res = {"success": False, "count": 0, "msg": ""}
    try:
        lang = session.query(Languages).order_by(desc(Languages.id)).all()
        rr = []
        for i in lang:
            rr.append(i.language)
        res["success"] = True
        res["msg"] = rr
        res["count"] = len(rr)
    except:
        res["msg"] = '请求错误'
    return res


if __name__ == '__main__':
    get_api()
