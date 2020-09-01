# 这里生成重要的限定条件(用于mgt的算法)
# 通过调用bosspool, 查看currenthp类属性
# 通过调用hitspool, 查看刀平均伤害, 计算刀数(实时)
# 然后可以将current boss hits needed属性更新回bosspool每个boss实例下

# Note:
# setAddr和getData这一段 跟boss_presentpool是一样的, 可以考虑摘出来

import pickle
from numpy import mean

def calulate(boss_code, boss_pool, knights_pool):
    curHp = boss_pool[boss_code].currentHealth
    dmg = list()
    for each in knights_pool.pool:# 这里有双重判定, 骑士的刀池中有没有这个boss; 以及, 这一刀是不是0
        try:
            dmg_temp = knights_pool.pool[each].hitsDamage[boss_code]
            if dmg_temp != 0:
                dmg.append(dmg_temp)
            else:
                print('[%s]的刀池中针对Boss:[%s]的数据为0, 不计入均值' % (each, boss_code))
        except KeyError:
            print('[%s]的刀池中没有针对Boss:[%s]的数据, 跳过' % (each, boss_code))
    if dmg != []:
        return curHp//mean(dmg), (curHp-(curHp//mean(dmg))*mean(dmg))# 返还所需刀数, 和剩余血量

    else:
        print('警告: 针对此boss的刀的库存为0')

if __name__ == '__main__':
    pass