DEBUG=True  #是否开启Dubug
HOST='0.0.0.0' #0.0.0.0表示访问权限为全网
PORT=80 #访问端口号

# mysql连接，比如 SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:root@localhost:3306/movie'
SQLALCHEMY_DATABASE_URI='mysql+cymysql://root:199866@localhost:3306/movie'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SECRET_KEY='cxz'
# redis服务器地址  比如  REDIS_URL = "redis://127.0.0.1:6379/10"
REDIS_URL = "redis://127.0.0.1:6379/10"