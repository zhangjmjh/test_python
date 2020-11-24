

# 获取某个字符串出现的位置和次数
def getStrInfo(str, target):
    count = 0
    for j, i in enumerate(str):
        if target == i:
            count += 1
            print(target, '出现的位置:', j)  # 出现的位置
    print(target, '出现的次数:', count)  # 出现的次数
getStrInfo("asfafaadfa", "a")
