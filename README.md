PortingChecker
==============

For android customization, check the accuracy of porting applications

adb shell pm list packages -f
adb shell pm dump com.jrdcom.FMRadioWidget|grep versionName
adb shell pm dump package com.google.android.apps.maps|grep versionName
