import hashlib
import hmac

# 这2个模块都i是用来进行数据加密
# hashlib 模块主要支持2个算法  md5和sha加密
# 加密方式：单向加密：只有加密的过程，不能解密md5/sha 对称加密：  非对称加密rsa

# 需要将加密的内容转换成为二进制
x = hashlib.md5()  # 生成一个md5对象
x.update('abc'.encode('utf8'))
print(x.hexdigest())  # 900150983cd24fb0d6963f7d28e17f72