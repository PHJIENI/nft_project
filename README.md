GIT使用
1、在远程GitHub创建新项目
2、上传代码需要密钥创建密钥
    1、电脑端下载git：https://git-scm.com/download/
    2、点击项目文件夹git bush here
    3、本机生成ssh密钥输入: ssh-keygen -t rsa -C "504551754@qq.com"
    4、进入github将密钥粘贴进去
    5、配置谁上传代码
        git config --global user.name "hao.pan1"
        git config --global user.email "504551754@qq.com"
    6、初始化项目
        git init
