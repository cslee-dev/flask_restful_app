from sqlalchemy import create_engine
from .settings import DATABASE
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

DB_URL = None
engine = None
postgre = DATABASE.get('postgre')

if postgre is not None:
    DB_URL = "postgresql://{id}:{passwd}@{host}:{port}/{name}".format(
        port=postgre.get('port'), id=postgre.get('id'), passwd=postgre.get('passwd'),
        host=postgre.get('host'), name=postgre.get('name')
    )

if DB_URL is not None:
    engine = create_engine(DB_URL, isolation_level=postgre.get('isolation_level'), implicit_returning=False, echo=False)
else:
    raise ConnectionError('DB를 설정해주세요')

Session = sessionmaker(bind=engine)

# 테이블 생성 코드
# from models import Base
# Base.metadata.create_all(engine)

@contextmanager
def session_scope(session=None):
    if session:
        yield session
    else:
        session = Session()
    try:
        yield session
        session.commit()
        session.flush()
    except Exception as e:
        session.rollback()
        print('error : ', e)
        raise
    finally:
        session.close()