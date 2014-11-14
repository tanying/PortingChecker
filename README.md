# PortingChecker

For checking the accuracy of porting applications
用来检查预置的应用是否符合预期.

## 获取文件:
    https://github.com/tanying/PortingChecker/archive/pygui.zip

    或者通过git:
    git clone -b pygui https://github.com/tanying/PortingChecker.git
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

    python pchk [perso] 
    指定perso比较， perso名目前仅支持tmo和mps
    tmo表示Tmobile
    mps表示MetroPCS 

## 修改服务器地址:
    由于比较过程中有一个从服务器远程拷贝3rd.json和gms.json的动作。
    通过修改./config/server.json可以修改服务器的ip地址，分支名，项目名和版本名
    也可以通过指定参数修改服务器地址。
    例如：
    python pchk -v vA12  表示将版本名修改为vA12

    -i      更改ip
    -b      更改branch
    -p      更改project
    -v      更改version
    
    例如：
    172.24.219.164:/local/build/alto_4.5_tmous-release/vA12/custo_wimdata_ng/wcustores/jrdsh6752_lw_kk/App/3rd.json
    ip = 172.24.219.164
    branch = alto_4.5_tmous-release
    project = jrdsh6752_lw_kk
    version = vA12

    如果不输入这些参数，工具会默认使用上一次拷贝文件的服务器的地址 

## 修改配置文件:
    python pchk --gen gms.json
    python pchk --gen 3rd.json

    前提是config目录下包含gms.json和3rd.json两个文件
    通过运行本条命令只会载入需要进行修改的json文件,并在html页面生成修改后的json.
    真正的改动json操作需要手动copy已经生成好的页面json到config目录下.
    
## 通过文件夹生成json
    python pchk --gen 需要生成json的路径 文件名




