#MongoDB For Centos:

## 安装MongoDB
* Create a /etc/yum.repos.d/mongodb-org-4.0.repo


		[mongodb-org-4.0]
		name=MongoDB Repository
		baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
		gpgcheck=1
		enabled=1
		gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc

* sudo yum install -y mongodb-org

### 启动默认MongoDB

* sudo service mongod start 

* sudo service mongod stop

* sudo service mongod restart

### 查看MongoDB是否启动
* netstat -lanp | grep "mongod"

### 配置MongoDB文件
* /etc/mongod.conf

### 指定config文件启动&关闭
####  启动&并开启认证
* sudo mongod  --auth --config /root/kysc/mongodb_env/mongod.conf

#### 关闭
* sudo mongod --config /root/kysc/mongodb_env/mongod.conf --shutdown

### 启动MongoDB Shell
* mongo --port 27017

### 安装mongodb可视化工具
* https://robomongo.org/download
