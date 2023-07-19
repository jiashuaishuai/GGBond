#!/bin/bash
echo "执行上班任务中~~~~"
/Users/jss/Library/Android/sdk/platform-tools/adb -s WRU6R20428002766 shell input keyevent 224
/Users/jss/Library/Android/sdk/platform-tools/adb -s WRU6R20428002766 shell input swipe 1358 1458 1358 300
/Users/jss/Library/Android/sdk/platform-tools/adb -s WRU6R20428002766 shell input text 777777
/Users/jss/Library/Android/sdk/platform-tools/adb -s WRU6R20428002766 shell am force-stop com.tencent.wework
/Users/jss/Library/Android/sdk/platform-tools/adb -s WRU6R20428002766 shell am start com.tencent.wework/com.tencent.wework.launch.LaunchSplashActivity
sleep 9
/Users/jss/Library/Android/sdk/platform-tools/adb -s WRU6R20428002766 shell input keyevent 26
echo "执行上班任务成功！！！！"
