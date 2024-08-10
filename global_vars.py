active = None   #调用数据库的对象
flag=None       #用于判断身份
with open("api_key.txt",'r',encoding='utf-8') as fp:
    api_key = fp.read()
login_flag = False  #用于判断是否登录
