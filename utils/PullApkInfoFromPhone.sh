#!/bin/sh
#PullApkInfoFromPhone.sh

#ying.tan@tcl.com

adb shell pm list packages -f > ./output/apkList.txt

res=`echo $?`   # get return result

if [ $res -eq '255' ];then
    echo 'Please connect your phone to PC by USB.'
    rm ./apkList.txt
elif [ $res -eq '0' ];then
    echo 'Pull Apk path Info successfully'
fi