PortingChecker
==============

For checking the accuracy of porting applications

配置文件: 
    config/3rd.json 键和值必须用双引号包含,不得用单引号
    config/gms.json
输出文件: 
    output/apkList.txt  从手机中获取到的包路径
    output/compareResult.txt 手机和配置文件的比较结果
    output/PortingChecker.log 日志文件
 
启动比较:
    python PortingChecker
修改配置文件:
   python PortingChecker --config gms
   python PortingChecker --config 3rd
   
http://pydoc.org/2.2.3/SimpleHTTPServer.html
