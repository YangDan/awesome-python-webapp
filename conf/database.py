# coding=utf-8

import MySQLdb


class MysqlClient():
    def __init__(self,param):
        self.connect(param)


    def connect(self,param):
        if param.has_key('port') == False:
            param['port'] = 3306
        self.conn = MySQLdb.connect()


    def close(self):
        self.conn.close()


    def query(self, sql):
        if self.conn != None:
            cursor = self.conn.cursor()
            cursor.execute('set names utf-8')
            cursor.execute(sql)
            self.insertId = cursor.lastrowid
            cursor.close()
        return False

    def getResults(self, sql):
        if self.conn != None:
            cursor = self.conn.cursor()
            cursor.execute('set names utf-8')
            cursor.execute(sql)
            res = cursor.fetchall()
            cursor.close()
            return  res
        return False

# //将元组数据转换为列表类型,每个条数据元素为字典类型:[{'字段1':'字段1的值', '字段2':'字段2的值','字段3':'字段3的值',...},{第二条数据},...]



