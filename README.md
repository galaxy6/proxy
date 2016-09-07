#Proxy

##proxy.py

这个脚本的主要作用是获取每天的最新的可用的ip代理列表。




##Introduce

1.环境python2.7，直接运行在服务器上，每天10点自动获取当天ip代理列表。

2.每日代理ip存放在iplist目录下。

3.日志存放在log目录下，程序运行实时状态可用通过日志查看。

4.protect文件的目的是保护进程，当主进程出现错误退出时，protect会重新启动这个进程。


##Usage

Usage: 
   
   python task.py	
   python protect.py
        
