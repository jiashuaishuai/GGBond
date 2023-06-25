import datetime
import json
import os
import random
import sys
import time

import git
from chinese_calendar import is_workday

offsetTime = random.randint(1, 7)
print("延迟%s分钟" % offsetTime)
time.sleep(offsetTime * 60)

date = datetime.datetime.now().date()
path = sys.path[0]  # 当前文件目录
path = os.path.dirname(path)  # 工程目录
ggBondProject = git.Repo.init(path)  # 初始化git仓库

if is_workday(date):
    print("%s 是工作日" % date)
    remote = ggBondProject.remote()
    remote.pull()
    print("代码拉取成功")
    jsonFile = open(path + "/holidaysAtGGBond.json", 'r')
    jsonJ = json.load(jsonFile)
    print(jsonJ)
    jsonFile.close()
    if jsonJ["GG"]:
        delay = jsonJ["sleep"]
        if delay > 0:
            time.sleep(delay * 60)
        result = os.popen(path + "/sh/toWork.sh")
        print(result.read())
    else:
        print("请假啦~~~~~")
else:
    print("%s是休息日粗去玩~~~" % date)

# remote = ggBondProject.remote()
# ggBondProject.index.add("log")
# ggBondProject.index.add("py")
# ggBondProject.index.add("sh")
# ggBondProject.index.commit(date.__str__())
# remote.push()
ggBondProject.close()
print("日志更新")
print("\n")
