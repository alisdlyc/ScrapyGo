import pymysql

# 建立连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='pygo',
    charset='utf8',
)

# 获取游标
cursor = conn.cursor()

# 执行sql语句
usr = 'qwq'
pwd = 'qwq'
sql = "select * from pyusr where `name`='%s' and `password`='%s'" % (usr, pwd)
print(sql)
# 受影响的行数
rows = cursor.execute(sql)
print(cursor.fetchall())
print(rows)

# 增、删、改
sql = "insert into pyusr(`name`, `password`) values(%s, %s)"
rows = cursor.execute(sql, ('ovo', '123'))
conn.commit()

cursor.close()
conn.close()

# 判断
if rows:
    print("登陆成功")
else:
    print("qwq")