# knights板块的流程
# 初始界面
# 各孙板块的input

# Notes:
# 尚未添加默认保存功能
# 如果要做core()函数, 就要考虑全局和局部变量的问题

import knights_knight
import knights_hitspool
import os

# initialize
def welcome():
    print('欢迎: 进入骑士应用模块\n任务: 骑士刀池初始化...完成\n骑士长您好, 请浏览命令列表 - help:')
    return knights_hitspool.Hitspool()

def cmdlist():
    print('设置刀池路径 --------------- setdir;\n读取已有刀池 --------------- load;\n储存当前刀池 --------------- save;\n创建一名骑士 --------------- create;\n查看骑士信息 --------------- stats;\n报刀 ----------------------- reprt;\n添加或修改骑士的模拟刀池 --- simu;\n修改骑士的剩余刀数量 ------- hits;\n手动更新boss当前血量 ------- bosscurhp')

def getStats(knight_instance):
    return knight_instance.name, knight_instance.hitsDamage, knight_instance.hitsLeft

def log(log_name, log_date, log_time, log_bosscode, log_damage, log_team):
    with open(os.path.dirname(os.path.abspath(__file__))+'\\knights_data\\log.txt', 'a') as log_file:
        log_file.write(log_date+','+log_time+','+log_name+','+log_bosscode+','+str(log_damage)+','+log_team+'\n')

def core():
    cmd = input('命令: ')
    if cmd == 'help':
        cmdlist()

    elif cmd == 'setdir':
        cmd_filename = input('请输入文件名称, 以.pkl结尾: ')
        hitspool.setAddress(cmd_filename)

    elif cmd == 'load':
        try:
            hitspool.getHitsPool()
            print('读取成功...')
        except (AttributeError, FileNotFoundError) as reason:
            print('你必须先通过 setdir 设置正确的文件名: ' + str(reason))

    elif cmd == 'save':
        try:
            hitspool.saveHitsPool()
            print('保存成功...')
        except AttributeError:
            print('你必须先通过 setdir 设置正确的文件名')

    elif cmd == 'stats':
        cmd_id = input('请输入骑士编号(id): ')
        if cmd_id in hitspool.pool:
            print('当前骑士的信息如下: \n', getStats(hitspool.pool[cmd_id]))
        else:
            print('无法在刀池中找到这名骑士')

    elif cmd == 'create':
        cmd_name = input('请问我该如何称呼这名新人? ')
        cmd_id = input('请您为这名骑士赋予一个编号(id), 例如: k001: ')
        if cmd_id not in hitspool.pool:
            knight = knights_knight.Knight(cmd_name)
            print('[%s]诞生了' % knight.name)
            hitspool.pool[cmd_id] = knight
            print('恭喜编号[%s] - [%s], 成功加入行会(的刀池)' % (cmd_id, knight.name))
        else:
            print('已经有另一名骑士拥有这个编号, 命令失败...')

    elif cmd == 'simu':
        cmd_id = input('请输入骑士编号(id): ')
        if cmd_id in hitspool.pool:
            cmd_bosscode = input('请输入boss编号, 例如: A1: ')
            cmd_damage = input('请输入模拟战伤害, 例如: 1213076: ')
            hitspool.pool[cmd_id].modHitDamage(cmd_bosscode, int(cmd_damage))
        else:
            print('行会(的刀池)中没有这个编号, 你可以通过recruit为当前骑士赋予编号加入行会')

    elif cmd == 'hits':
        cmd_id = input('请输入骑士编号(id): ')
        cmd_date = input('请输入日期, 例如: day1: ')
        if cmd_id in hitspool.pool:
            hitspool.pool[cmd_id].modHitsLeft(cmd_date)
            print('骑士出刀次数已更新, [%s]剩余[%d/3]刀' % (cmd_date, hitspool.pool[cmd_id].hitsLeft[cmd_date]))
        else:
            print('行会(的刀池)中没有这个编号, 你可以通过recruit为当前骑士赋予编号加入行会')

    elif cmd == 'reprt':
        cmd_id = input('请输入骑士编号(id): ')
        if cmd_id in hitspool.pool:
            knight_report = hitspool.pool[cmd_id]
        else:
            print('行会(的刀池)中没有这个编号, 你可以通过recruit为当前骑士赋予编号加入行会')
        cmd_name = input('请输入骑士的名字(注意,不是编号id): ')
        cmd_date = input('请输入出刀的日期, 例如: day1: ')
        cmd_time = input('请输入结算的事件, 例如: 12:34: ')
        cmd_bosscode = input('请输入boss代码, 例如: A1: ')
        cmd_damage = input('请输入结算伤害, 例如: 1213076: ')
        cmd_team = input('请输入队伍的刀型, 例如: 暴击弓深月狗黑骑-借狼: ')
        cmd_bossfileupdate = input('如果需要自动扣减boss当前血量, 请输入bosspool文件名称(以.pkl结尾), 否则请输入\'\': ')
        knight_report.report(cmd_name, cmd_date, cmd_time, cmd_bosscode, int(cmd_damage), cmd_bossfileupdate)
        # 存log
        log(cmd_name, cmd_date, cmd_time, cmd_bosscode, int(cmd_damage), cmd_team)

    elif cmd == 'bosscurhp':
        cmd_bosscode = input('请输入boss代码, 例如: A1: ')
        cmd_damage = input('请输入结算伤害, 例如: 1213076: ')
        cmd_bossfileupdate = input('请输入bosspool文件名称(以.pkl结尾): ')
        currentHp = knights_knight.Knight('骑士长').updateCurHp(cmd_bosscode, cmd_damage, cmd_bossfileupdate)
        print('骑士长对boss造成了[%d], boss剩余血量为[%d]' % (cmd_damage, currentHp))

    else:
        print('我不明白骑士长的命令, 请调教我...')
    
if __name__ == '__main__':
    hitspool = welcome()
    cmdlist()
    while 1:
        core()
        # 这里可以添加默认保存功能