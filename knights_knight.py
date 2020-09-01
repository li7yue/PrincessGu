# 骑士的核心类, 包含所有骑士及其刀的信息, 实例化后在Hits Pool集合(经过中转站)
# Maintian: 骑士维护个人刀池
# 编号不可修改, 可以维护内容包括: 姓名, 对每个boss(编号)的伤害, 每天剩余刀数(报刀时修改)
# Apply: 骑士申请出刀
# Report: 骑士报刀
# Update: 发出更新请求, 打包需要更新的数据, maintain>report>apply
# Browse: 浏览会战其他数据和信息

# Notes: 
# Knight init时, 会战默认是6天, 改变需要修改编码
# 剩余刀数默认每次减一, 需要编写错误提醒
# report可以更新刀池, 剩余刀数, boss当前血量

# update 通过骑士自己的实例中的函数, 调用HitsPool数据, 进行更新
# apply 和 report待定

import os
import boss_bosspool

class Knight:
    def __init__(self, name):
        self.name = name
        self.hitsDamage = dict()
        self.hitsLeft = {'day1':3, 'day2':3, 'day3':3, 'day4':3, 'day5':3, 'day6':3}
    
    def modHitDamage(self, boss_code, damage):
        self.hitsDamage[boss_code] = damage
    
    def modHitsLeft(self, date, count=1):
        if count <= self.hitsLeft[date]:
            self.hitsLeft[date] -= count
        else:
            print('出刀数量超出了剩余刀的数量')

    def report(self, name, date, time, boss_code, damage, boss_file_update, damage_update=True, hits_update=True):
        print('[%s], 在[%s-%s], 对boss编号:[%s]出刀完毕, 结算伤害:[%s]' % (name, date, time, boss_code, damage))
        
        if boss_file_update != '\'\'':
            currentHp = self.updateCurHp(boss_code, damage, boss_file_update)
            print('boss当前血量已更新, boss剩余血量为[%d]' % currentHp)
        else:
            print('boss当前血量未更新, 请手动通过 updateCurHp 更新boss当前血量')
        
        if damage_update == True:
            self.modHitDamage(boss_code, 0)
            print('骑士刀池已更新 (已出刀的伤害将会被记为0)')
        else:
            print('骑士刀池未更新, 如需更新请通过 modHitDamage 更新刀池中这一刀伤害')

        if hits_update == True:
            self.modHitsLeft(date)
            print('骑士出刀次数已更新, 今天剩余[%d/3]刀' % self.hitsLeft[date])
        else:
            print('骑士出刀次数未更新, 请手动通过 modHitsLeft 更新剩余刀数')
        # 修改log

    def updateCurHp(self, boss_code, damage, boss_file):
        temp_bosspool = boss_bosspool.BossPool()
        temp_bosspool.setAddress(os.path.dirname(os.path.abspath(__file__)), boss_file)
        temp_bosspool.getBossPool()
        curHp = temp_bosspool.pool[boss_code].damageCurrentHealth(damage)
        temp_bosspool.saveBossPool()
        return curHp

    def apply(self):
        pass
        # 申请出刀信号
        # 申请优化算法
        # 获取结果, 对比申请, 判断自己申请的刀是否被算法选出, 决定是否可以出刀

    def update(self):
        pass
        # apply和report待定

if __name__ == '__main__':
    pass