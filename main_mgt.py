# mgt板块的流程
# 初始界面
# 各孙板块的input
# 这里包含了最关键的算法流程的引导: Optimize
# 以及其他管理功能: 
# Browse: 查看算法/优化结果
# Adjust: 手动调整优化结果
# Timer: 时间
# Approve: 这个功能是针对knight的apply, 是个手动审批功能, 后续再更新

import mgt_optimize
from pprint import pprint

def welcome(hitsPool, bossPool):
    print('欢迎: 进入排刀计算应用模块\n任务: 算法功能初始化...完成\n先知您好, 请浏览法术列表 - help:')
    return mgt_optimize.Optimize(hitsPool, bossPool)

def cmdlist():
    print('开始排刀 - cal')

def calculate(date):
    opt.getHitsLeft(date)
    opt.getHitsNeed()
    opt.getDmgMatrix()
    res = opt.arrangement_problem()
    return res['var']

def core():
        cmd = input('法术: ')
        if cmd == 'help':
            cmdlist()

        elif cmd == 'cal':
            cmd_date = input('选择需要排刀的日期, 例如: day1: ')
            opt_var = calculate(cmd_date)
            pprint(opt_var)

        else:
            print('您还没有习得这个法术...')

if __name__ == '__main__':
    import boss_bosspool
    import knights_hitspool
    hitsPool = knights_hitspool.Hitspool()
    bossPool = boss_bosspool.BossPool()
    hitsPool.setAddress('pool0823.pkl')
    bossPool.setAddress('pool0823.pkl')
    hitsPool.getHitsPool()
    bossPool.getBossPool()

    opt = welcome(hitsPool, bossPool)
    cmdlist()
    while 1:
        core()
    