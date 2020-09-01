# 每个boss的类
# 关键的类属性包括:
# Name: boss全称
# Boss Code: boss代码, 周目+序号: A1-A6(非狂暴为5 狂暴为6), B1-B6, AA-AZ
# Hp: boss血量
# Current Hp: 初始boss时对boss血量进行deepcopy, 然后用于与报刀伤害的相减
# 这里注意, 如果把currenthp做成私有化属性, 就必须匹配修改它的def
# 否则外部无法修改私有化类属性
# current boss hits needed: 剩余血量所需刀数, 由calhits计算
# 这里可以是一个预估, 或初始值
# Retain: 需要留存的血量(合刀用)
# Boss Stats: 可以getbossdata, 查看boss所有数据

# Note:
# 把当前血量需要的刀数设置成了boss的类实例的属性, 默认为0刀, 在calhit里调用修改
# currentHp是一个频繁调用的属性, 这里单独做一个类函数, 以防未来要做成也难怪私有化函数, 只能通过def修改
# damageCurrentHp因为包含判断, 所以单独写一个函数

import copy

class Boss:
    def __init__(self, name, code, health, retain=0, curHitsNeed=0):
        self.name = name
        self.code = code
        self.health = health
        self.currentHealth = copy.deepcopy(health)
        self.retain = retain
        self.curHitsNeed = curHitsNeed
    
    def modCurrentHealth(self, currenthp):
        self.currentHealth = currenthp
    
    def damageCurrentHealth(self, damage):
        if damage <= self.currentHealth:
            self.currentHealth -= damage
        else:
            self.currentHealth = 0
            print('这一刀的伤害, 超出了当前boss的血量')
        return self.currentHealth
    
    def getBoss(self):
        print('boss的编号是[%s], 名称是[%s], 当前血量[%d]/[%d](包含保留血量[%d]), 当前血量还需要[%d]刀' % (self.code, self.name, self.currentHealth, self.health, self.retain, self.curHitsNeed))
        return [self.code, self.name, self.currentHealth, self.health, self.retain, self.curHitsNeed]

if __name__ == '__main__':
    pass