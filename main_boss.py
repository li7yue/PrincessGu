#coding:utf-8 
# 编码格式, 不能删

# boss板块的流程
# 初始界面
# 各孙板块的input

# Note:
# 和knight不一样, boss采用直接在boss实例中建立boss_code作为属性, knight则是没有code属性(需要在recruit时设置编号)
# 看看哪种效果好, 可以将两种统一
# updAllHits算完记得存, 尤其是对于autoupdate所需刀数
# 如果要做core()函数, 就要考虑全局和局部变量的问题

import boss_bossdata
import boss_bosspool
import boss_calhits
import knights_hitspool

def welcome():
    print('欢迎: 进入boss应用模块\n任务: boss池初始化...完成\n魔王大人您好, 请浏览命令列表 ------------------------ help:')
    return boss_bosspool.BossPool()

def cmdlist():
    print(
        '设置boss池路径 -------------------------------------- setdir;\n读取已有boss池 -------------------------------------- load;\n储存当前boss池 -------------------------------------- save;\n创建一只boss ---------------------------------------- create;\n检查当前会战boss ------------------------------------ presnt;\n查看boss的信息 -------------------------------------- stats;\n查看及修改一只boss的当前所需刀数 -------------------- hits;\n对当前boss池中所有boss的[curHitsNeed]属性, 进行更新 - updAllHits;\n查看及修改一只boss的当前血量 ------------------------ bosscurhp')

def core():
    cmd = input('命令: ')
    if cmd == 'help':
        cmdlist()

    elif cmd == 'setdir':
        cmd_filename = input('请输入文件名称, 以.pkl结尾: ')
        bossPool.setAddress(cmd_filename)

    elif cmd == 'load':
        try:
            bossPool.getBossPool()
            print('读取成功...')
        except (AttributeError, FileNotFoundError) as reason:
            print('你必须先通过 setdir 设置正确的文件名: ' + str(reason))

    elif cmd == 'save':
        try:
            bossPool.saveBossPool()
            print('保存成功...')
        except AttributeError:
            print('你必须先通过 setdir 设置正确的文件名')

    elif cmd == 'create':
        print('注意: 非狂暴与狂暴boss需要作为创造两个boss实例, 举例: 非狂暴巨蟹 A5 10000000, 狂暴巨蟹 A6 10000000')        
        cmd_code = input('请您为这只怪物赋予一个编号(code): ')
        if cmd_code not in bossPool.pool:
            cmd_name = input('请问我该如何呼唤这只怪物? ')
            cmd_health = input('请问这这只boss的基础血量是多少? ')
            boss = boss_bossdata.Boss(cmd_name, cmd_code, int(cmd_health))
            print('[%s]诞生了' % boss.name)                
            bossPool.pool[cmd_code] = boss
            print('恭喜编号[%s] - [%s], 成功进入boss池, 愿它大杀四方' % (cmd_code, boss.name))
            boss.getBoss()
        else:
            print('我暂时无法为您覆盖/替换已经存在的boss, 命令失败...')

    elif cmd == 'stats':
        cmd_code = input('请输入boss编号(code): ')
        if cmd_code in bossPool.pool:
            print('您选中的boss的信息如下: ')
            bossPool.pool[cmd_code].getBoss()
        else:
            print('无法在boss池中找到这只boss')

    elif cmd == 'presnt':
        for each in bossPool.pool:
            check = bossPool.pool[each]
            if check.currentHealth > 0:
                print('骑士们正在对抗boss: [%s] - [%s], 当前血量 - [%d]/[%d]' % (check.code, check.name, check.currentHealth, check.health))
                break
            else:
                print('boss: [%s] - [%s], 已被击败, 正在体检下一个boss...' % (check.code, check.name))

    elif cmd == 'hits':
        cmd_code = input('请输入boss编号(code): ')
        if cmd_code in bossPool.pool:
            cmd_curHitsNeed = input('请输入击杀这个boss的目前血量所需的刀数: ')
            bossPool.pool[cmd_code].curHitsNeed = int(cmd_curHitsNeed)
            print('更新成功')
        else:
            print('无法在boss池中找到这个boss')

    elif cmd == 'updAllHits':
        hitsPool_filename = input('请输入!骑士!刀池的文件名称, 以.pkl结尾(用于计算): ')
        hitsPool = knights_hitspool.Hitspool()
        hitsPool.setAddress(hitsPool_filename)
        hitsPool.getHitsPool()
        for each in bossPool.pool:
            try:
                curHtsNd, curHp = boss_calhits.calulate(each, bossPool.pool, hitsPool)
                bossPool.pool[each].curHitsNeed = curHtsNd
                print('Boss: [%s] - [%s], 被击败预计还需要[%d]刀, 出完[%d]刀后的预计剩余血量为: [%d / %d]' % (bossPool.pool[each].code, bossPool.pool[each].name, curHtsNd, curHtsNd, curHp, bossPool.pool[each].health))
            except TypeError as reason:
                print('数据解析出错: ', str(reason))
        print('属性: [击败boss当前血量所需刀数]; 状态: boss池中所有boss的该属性已完成更新')

    elif cmd == 'bosscurhp':
        cmd_code = input('请输入boss编号(code): ')
        if cmd_code in bossPool.pool:
            cmd_curHp = input('请输入这只boss的当前血量: ')
            bossPool.pool[cmd_code].currentHealth = int(cmd_curHp)
            print('更新成功')
        else:
            print('无法在boss池中找到这个boss')

    else:
        print('我不明白魔王大人的命令, 难道是让妾身...?')

if __name__ == '__main__':
    bossPool = welcome()
    cmdlist()
    while 1:
        core()
        # 这里可以添加默认保存功能