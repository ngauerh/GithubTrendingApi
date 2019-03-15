from config import DB
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, Sequence
from sqlalchemy import func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?charset={CHARSET}'.format(
    USERNAME=DB['USER'],
    PASSWORD=DB['PASSWORD'],
    HOST=DB['HOST'],
    PORT=DB['PORT'],
    DB_NAME=DB['DB_NAME'],
    CHARSET=DB['CHARSET'],
), convert_unicode=True, echo=False)


DBSession = scoped_session(sessionmaker(autocommit=True, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = DBSession.query_property()

Base = declarative_base()


def init_db(db_engine):
    Base.metadata.create_all(bind=db_engine)


class Api(Base):
    __tablename__ = 'api'
    id = Column(Integer, Sequence('api_id_seq'), primary_key=True)
    repo = Column(String(128))  # repository name
    language = Column(String(128))  # repository language
    user = Column(String(128))    # user
    about = Column(Text,)   # repository description
    link = Column(Text)  # link
    stars = Column(String(128))
    forks = Column(String(128))
    avatars = Column(Text)  # avatar
    new_stars = Column(String(128))
    sincedate = Column(String(30))
    update_time = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return "<Api(id='%s')>" % self.id


class DevApi(Base):
    __tablename__ = 'dev'
    id = Column(Integer, Sequence('dev_id_seq'), primary_key=True)
    avatar = Column(Text)
    username = Column(String(128))
    userlink = Column(Text)
    repo = Column(String(128))
    repo_about = Column(Text)
    lang = Column(String(128))
    sincedate = Column(String(30))
    update_time = Column(DateTime(timezone=True), default=func.now())


class Languages(Base):
    __tablename__ = 'languages'
    id = Column(Integer, Sequence('lang_id_seq'), primary_key=True)
    language = Column(String(128))  # github all languages

    def __repr__(self):
        return "<Languages(id='%s')>" % self.language


if __name__ == '__main__':
    init_db(engine)
