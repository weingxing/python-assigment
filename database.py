import pymysql as mysql
import configparser


class DB:
    """
    数据库类，提供 增删改查 操作
    @author weingxing
    @since 2020/04/02
    """
    def __init__(self):
        try:
            # 解析配置文件
            configer = configparser.ConfigParser()
            configer.read('config.ini')
            database = configer['DataBase']
            # 取得数据库连接
            self.conn = mysql.connect(host=database['host'], port=int(database['port']),
                                      user=database['user'], password=database['password'],
                                      database=database['db'], charset='utf8')
            # 获取游标
            self.cursor = self.conn.cursor()
        except mysql.Error:
            raise Exception('数据库连接失败')
        except configparser.Error:
            raise Exception('配置文件解析失败')

        # SQL 语句
        self._select = 'SELECT * FROM info;'
        self._insert = 'INSERT INTO info(sno, name, sex, college, clazz) VALUES(%s, %s, %s, %s, %s);'
        self._delete = 'DELETE FROM info WHERE sno=%s;'
        self._update = 'UPDATE info SET name=%s, sex=%s, college=%s, clazz=%s WHERE sno=%s;'
        self._search = 'SELECT * FROM info WHERE sno LIKE %s OR name LIKE %s OR sex LIKE %s' \
                       'OR college LIKE %s OR clazz LIKE %s;'
        self._login = 'SELECT * FROM user;'
        self._register = 'INSERT INTO user(username, password) VALUES(%s, %s);'

    def __del__(self):
        try:
            self.cursor.close()
            self.conn.close()
        except mysql.Error:
            pass

    # 添加信息
    def insert(self, **kwargs):
        try:
            param = [kwargs['sno'], kwargs['name'], kwargs['sex'], kwargs['college'], kwargs['clazz']]
            self.cursor.execute(self._insert, param)
            self.conn.commit()
            return True
        except mysql.Error:
            return False

    # 查找全部信息
    def select(self):
        try:
            self.cursor.execute(self._select)
            result = self.cursor.fetchall()
            return result
        except mysql.Error:
            return None

    # 按学号删除信息
    def delete(self, sno):
        try:
            self.cursor.execute(self._delete, [sno])
            self.conn.commit()
            effect_row = self.cursor.rowcount
            if effect_row > 0:
                return True
            return False
        except mysql.Error:
            return False

    # 按学号修改信息
    def update(self, **kwargs):
        try:
            param = [kwargs['name'], kwargs['sex'], kwargs['college'], kwargs['clazz'], kwargs['sno']]
            self.cursor.execute(self._update, param)
            self.conn.commit()
            return True
        except mysql.Error:
            return False

    # 按关键词查找信息
    def search(self, key):
        try:
            param = ['%' + str(key) + '%' for i in range(5)]
            self.cursor.execute(self._search, param)
            result = self.cursor.fetchall()
            return result
        except mysql.Error:
            return None

    def login(self):
        try:
            self.cursor.execute(self._login)
            result = self.cursor.fetchall()
            return result
        except mysql.Error:
            return None

    def register(self, **kwargs):
        try:
            param = [kwargs['username'], kwargs['password']]
            self.cursor.execute(self._register, param)
            self.conn.commit()
            return True
        except mysql.Error:
            return False


if __name__ == '__main__':
    # 测试
    db = DB()
    db.insert(sno='1', name='张三', sex='男', college='信息科学技术学院', clazz='计科181')
    print(db.select())
    db.update(sno='1', name='张三', sex='女', college='信息科学技术学院', clazz='计科181')
    print(db.search('张'))
    print(db.search('123'))
