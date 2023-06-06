#!/bin/bash
echo "执行上班任务中~~~~"
/Users/jss/Library/Android/sdk/platform-tools/adb shell input keyevent 224
/Users/jss/Library/Android/sdk/platform-tools/adb shell input swipe 1358 1458 1358 300 
/Users/jss/Library/Android/sdk/platform-tools/adb shell input text 777777
/Users/jss/Library/Android/sdk/platform-tools/adb shell am force-stop com.tencent.wework
/Users/jss/Library/Android/sdk/platform-tools/adb shell am start com.tencent.wework/com.tencent.wework.launch.LaunchSplashActivity
sleep 9
/Users/jss/Library/Android/sdk/platform-tools/adb shell input keyevent 26
echo "执行上班任务成功！！！！"
