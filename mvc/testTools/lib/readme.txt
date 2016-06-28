需要安装xdeploy
git 地址:http://gitlab.alipay-inc.com/antcloud/xdeploy.git

注意内容：
1. python需要2.7及其以上版本.centos命令如下
wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz
tar xf Python-2.7.8.tgz
cd Python-2.7.8
./configure --prefix=/usr/local
make && make install
(shell需要退出再进入)

2. 安装 setuptools + pip
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
sudo python ez_setup.py
sudo easy_install pip

3. 安装  Sqlite 数据库: sudo yum install sqlite-devel -y

4. 安装django
sudo pip install Django==1.9.1

5. 安装xdeploy

6. 安装oss

7. 安装rest_framwork
使用提供的tar.gz
或者
pip install djangorestframework

8. 

8. 启动需要 python manager.py runserver 0.0.0.0:8000来接收所有ip对8000端口的请求
