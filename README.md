PortingChecker
==============

For android customization, check the accuracy of porting applications

adb shell pm list packages -f
adb shell pm dump com.jrdcom.FMRadioWidget|grep versionName
