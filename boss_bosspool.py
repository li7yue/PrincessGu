# boss类实例化的集合
# 用一个字典集合所有boss的实例
# 初始一个字典
# getBossPool: 从data读取boss实例列表, 既Boss Pool
# saveBossPool: 存储bosspool至data

# Note:
# 最终还是list调整成了dict, 认为功能更加丰富
# log可以考虑和knights的log sync
# 当前路径需要提前定义, 文件名待定
# 要提前对文件夹路径进行设定后才能应用get 和 save
# 尽量删除了冗余的编码, 例如:如果需要修改boss属性, 或新加boss, 直接选择池中boss用bossdata中boss类属性修改, 或者直接在pool字典中加入已经设置好的boss实例

import pickle
import os

class BossPool:
    def __init__(self, pool=dict()):
        self.pool = pool
    
    def setAddress(self, file_name, file_address=os.path.dirname(os.path.abspath(__file__))):
        self.file_address = file_address + '\\boss_data\\'
        self.file_name = file_name
    
    def getBossPool(self):
        with open(self.file_address + self.file_name, 'rb') as pickle_pool:
            self.pool = pickle.load(pickle_pool)

    def saveBossPool(self):
        with open(self.file_address + self.file_name, 'wb') as pickle_pool:
            pickle.dump(self.pool, pickle_pool)

if __name__ == '__main__':
    pass