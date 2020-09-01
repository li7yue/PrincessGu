# Hits Pool: 刀池, 一个集合所有骑士类实例的列表, 骑士实例中包含个人及刀信息
# 调用实例中的属性, 构成刀池, 但是Hits Pool首先是一个数据的集合库
# init: 生成最初始的list
# getHitsPool: 从data文件夹读取Hits Pool
# 和update不同, 这里是掌管Hits Pool的地方, 拥有对起修改的最高权限
# modHitsPool: 管理员也可以在这里对数据进行调整(原始数据来源于update孙板块)
# saveHitsPool: 保存pickle数据
# Log: 生成一个贯穿始终的Log(操作到这里才被记入Log, 避免骑士的不规范操作污染数据)

# Notes:
# 如果init没有input, 则初始一个空pool作为实例
# 如果init有input, 可以直接调用已有pool进行实例化
# 当前路径需要提前定义(默认是os当前路径)
# 文件名需要提前设置
# 要提前对文件夹路径进行设定后才能应用get 和 save


# log待定
# 路径提前设定
# 设置路径的类方法独立


import pickle
import os

class Hitspool:
    def __init__(self, pool=dict()):
        self.pool = pool

    def setAddress(self, file_name, file_address=os.path.dirname(os.path.abspath(__file__))):
        self.file_address = file_address + '\\knights_data\\'
        self.file_name = file_name 

    def getHitsPool(self):
        with open(self.file_address + self.file_name, 'rb') as pickle_pool:
            self.pool = pickle.load(pickle_pool)
    
    def saveHitsPool(self):
        with open(self.file_address + self.file_name, 'wb') as pickle_pool:
            pickle.dump(self.pool, pickle_pool)

if __name__ == '__main__':
    pass