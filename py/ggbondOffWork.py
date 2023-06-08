import datetime
import json
import os
import random
import sys
import time

from chinese_calendar import is_workday

offsetTime = random.randint(1, 2)
print("延迟%s分钟" % offsetTime)
time.sleep(offsetTime * 60)
path = sys.path[0]  # 当前文件目录
path = os.path.dirname(path)  # 工程目录
date = datetime.datetime.now().date()
if is_workday(date):
    print("%s是工作日" % date)
    jsonFile = open(path + "/holidaysAtGGBond.json", 'r')
    jsonJ = json.load(jsonFile)
    print(jsonJ)
    jsonFile.close()
    if jsonJ["GG"]:
        delay = jsonJ["sleep"]
        if delay > 0:
            time.sleep(delay * 60)
        result = os.popen(path + "/sh/offWork.sh")
        print(result.read())
    else:
        print("请假啦~~~~~")
else:
    print("%s是休息日粗去玩~~~" % date)
