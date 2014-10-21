# PortingChecker

For checking the accuracy of porting applications
用来检查预置的应用是否符合预期.

## 获取文件:
    https://github.com/tanying/PortingChecker/archive/pygui.zip

    或者通过git:
    git clone -b pygui git@git.oschina.net:tanying/otscli.git
    更新代码:
    git pull origin pygui

## 配置文件: 
    config/3rd.json 键和值必须用双引号包含,不得用单引号
    config/gms.json

## 输出文件: 
    output/apkList.txt  从手机中获取到的包路径
    output/compareResult.txt 手机和配置文件的比较结果
    output/PortingChecker.log 日志文件
 
## 启动比较:
    python pchk
    pc需要连上手机, USB调试已打开
    需要保证config目录下有3rd.json和gms.json两个文件

## 修改配置文件:
    python pchk --gen gms.json
    python pchk --gen 3rd.json

    通过运行本条命令只会载入需要进行修改的json文件,并在html页面生成修改后的json.
    真正的改动json操作需要手动copy已经生成好的页面json到config目录下.
    
## 通过gms文件夹生成gms.json
    python pchk --gen dir

    Please input the Project directory path: 输入包含GMS和GMS_pri的文件夹
    例如:
    /local/android/soul4/custo_wimdata_ng/wcustores/App/Unremoveable



