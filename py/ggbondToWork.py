import datetime
import json
import os
import sys

import git
from chinese_calendar import is_workday

date = datetime.datetime.now().date()
path = sys.path[0]  # 当前文件目录
path = os.path.dirname(path)  # 工程目录
ggBondProject = git.Repo.init(path)  # 初始化git仓库

if is_workday(date):
    print("%s是工作日" % date)
    remote = ggBondProject.remote()
    remote.pull()
    print("代码拉取成功")
    jsonFile = open(path + "/holidaysAtGGBond.json", 'r')
    jsonJ = json.load(jsonFile)
    print(jsonJ)
    jsonFile.close()
    if jsonJ["GG"]:
        result = os.popen(path + "/sh/ggbondTest.sh")
        print(result.read())
    else:
        print("请假啦~~~~~")
else:
    print("%s是休息日粗去玩~~~" % date)

remote = ggBondProject.remote()
ggBondProject.index.add("log")
ggBondProject.index.add("py")
ggBondProject.index.add("sh")
ggBondProject.index.commit(date.__str__())
pushInfoList = remote.push()
for pushInfo in pushInfoList:
    print(pushInfo.__str__())
print("日志更新")
print("\n")
