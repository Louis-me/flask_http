__author__ = "shikun"
# 数据库的常用字段

FIND_BY_SQL = "findBySql" # 根据sql查找
COUNT_BY_SQL = "countBySql" # 自定义sql 统计影响行数
INSERT = "insert" # 插入
UPDATE_BY_ATTR = "updateByAttr" # 更新数据
DELETE_BY_ATTR = "deleteByAttr" # 删除数据
FIND_BY_ATTR = "findByAttr" # 根据条件查询一条记录
FIND_ALL_BY_ATTR = "findAllByAttr"  #根据条件查询多条记录
COUNT = "count" # 统计行
EXIST = "exist" # 是否存在该记录
FIND_BY_ALL = "findbyall"
t = [{'header': '23312312', 'port': 27, 'id': 1, 'host': '127.0.0.1', 'title': '登陆'}]
for i in t:
  print(i["host"])