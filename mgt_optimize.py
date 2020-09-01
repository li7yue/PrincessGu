# 收集算法所需的数据
# Hits left array: 从hitspool的每个骑士的属性中收集他们的hits left(剩余刀数), 组成array
# Hits needed array: 从bosspool的每个boss数据中收集他们currenthp/averagedmg计算出的所需hits, 组成array
# Damage Matrix: 从hitspool中收集所有骑士未出的刀, 组成目标函数的系数矩阵
# Arrangement: 算法也被整合到这里了, 精简安排编码
# 以及其他特殊条件: 待补充

# Note:
# 0. opt = Optimize(hitsPool, bossPool)
# 1. opt.getHitsLeft
# 2. opt.getHitsNeed
# 3. opt.getDmgMatrix
# 4. res = opt.arrangment_problem
# 5. res['var']
# 6. pprint(res['var']) 

import numpy as np
import pulp

class Optimize:
    def __init__(self, hitsPool, bossPool):
        self.hitsPool = hitsPool
        self.bossPool = bossPool
        self.knightslist = list()
        self.hitsLeft = list()
        self.bossList = list()
        self.hitsNeed = list()
        self.dmgMatrix = [[]]

    def getHitsLeft(self, date):
        for each in self.hitsPool.pool:
            self.knightslist.append(each)
            self.hitsLeft.append(self.hitsPool.pool[each].hitsLeft[date])

    def getHitsNeed(self):
        for each in self.bossPool.pool:
            self.bossList.append(each)
            self.hitsNeed.append(self.bossPool.pool[each].curHitsNeed)

    def getDmgMatrix(self):
        for eachknight in self.knightslist:
            rowOfDmg = list()
            for eachboss in self.bossList:
                try:
                    rowOfDmg.append(self.hitsPool.pool[eachknight].hitsDamage[eachboss])
                except KeyError:
                    rowOfDmg.append(0)
            try:
                self.dmgMatrix = np.concatenate((self.dmgMatrix,[rowOfDmg]),axis=0)
            except ValueError:
                self.dmgMatrix = [rowOfDmg]

    def arrangement_problem(self):
        row = len(self.dmgMatrix)
        col = len(self.dmgMatrix[0])
        prob = pulp.LpProblem('Arrangement Problem', sense=pulp.LpMaximize)
        var = [[pulp.LpVariable(f'x{i}{j}', lowBound=0, cat=pulp.LpBinary) for j in range(col)] for i in range(row)]
        flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]

        prob += pulp.lpDot(flatten(var), self.dmgMatrix.flatten())
        for i in range(row):
            prob += (pulp.lpSum(var[i]) <= self.hitsLeft[i])
        for j in range(col):
            prob += (pulp.lpSum([var[i][j] for i in range(row)]) <= self.hitsNeed[j])

        prob.solve()
        print('优化结果:', pulp.LpStatus[prob.status])
        return {'objective':pulp.value(prob.objective), 'var': [[pulp.value(var[i][j]) for j in range(col)] for i in range(row)]}

if __name__ == '__main__':
    pass
    # import boss_bosspool
    # import knights_hitspool
    # hitsPool = knights_hitspool.Hitspool()
    # hitsPool.setAddress('pool0823.pkl')
    # bossPool = boss_bosspool.BossPool()
    # bossPool.setAddress('pool0823.pkl')
    # hitsPool.getHitsPool()
    # bossPool.getBossPool()

    # opt = Optimize(hitsPool, bossPool)

    # opt.getHitsLeft('day1')
    # opt.getHitsNeed()
    # opt.getDmgMatrix()
    # res = opt.arrangement_problem()
    # from pprint import pprint
    # pprint(res['var'])
