### 保存用户的请求日志

request

```json
{
  "user":"1", //存用户id
  "user_agent":"chrome", //用户使用的浏览器
  "user_origin":"http://0.0.0.0:8000", //用户初始的URL
  "user_refer":"http://0.0.0.0:8000/user/signin/", //用户重定向的URL
  "visit_time":"2016-12-20-08:08:08", //用户访问时间
  "visit_ip":"10.224.16.123", //用户访问ip

}
```

### 保存用户的学习进度数据


request
```json
{
    "user": "1", // 保存用户id
    "course": "1", //课程id
    "process": "50%", //进度
    "learning_time": "2.6" //学习时长
 }
```

