### TextSafeApi

基于fastapi 实现的敏感词识别 开发版本

#### 安装测试使用
```shell
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0
```

#### 测试使用
```shell
curl -X POST -H 'content-type: application/json' -d '{"text": "你是个大傻子谢谢谢谢","uid": "11111","info": true}' http://127.0.0.1:8000/check/message
```
#### 结果如下
```json
{"message":{"text":"你是个大傻子谢谢谢谢","uid":"11111","info":true},"result":[[4,"傻子","wfc"]],"block":true}
```