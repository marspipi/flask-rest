import os
#获取settings.py所在目录
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
# 获取settings.py
STATIC_DIR = os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(STATIC_DIR,'uploads')

class Config():
    DEBUG: True
    ENV = 'development'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.35.163.38:3306/users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'SOGKJDFGKJDFSKGDFPPJG'
