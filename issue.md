# 编写框架中遇到的问题点及解决方案

## app运行过程中出现闪退问题
### 滑动查找过程中出现app应用闪退
### 单个测试项（case）完成后应用闪退
### 测试过程中遇到超过60s的应用场景，测试应用退出。导致测试失败
- 解决：Appium在没有收到下一个命令时，默认超时时间是60s，超时后应用将会自动关闭session，所以你接下来的所有操作都将失败。
- capabilities 中添加：'newCommandTimeout': "时间/s",
### urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=4700): Max retries exceeded with url: /wd/hub/session/2e7de681-94c9-442d-8eab-c9d065182bc4 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000000000453C3C8>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。'))

   

