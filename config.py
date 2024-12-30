import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db')) #DB 접속 정보
SQLALCHEMY_TRACK_MODIFICATIONS = False #이벤트 처리 옵션이나, 불필요하기에 비활성화
SECRET_KEY = "dev"