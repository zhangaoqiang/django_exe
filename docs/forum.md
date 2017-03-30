###用户发帖子

POST    /forum/topic/

request

```json
{
    "course_id":"4189",
    "title":"Photoshop-CS6",
    "content":"<html>神一般的技术</html>"
}
```
response

```json
{
    "result":true,
    "detail":"or false 添加成功或失败",
    "create_time":"2016-05-12 18:20:36",
    "publish_time":"2016-05-12 18:20:59"
}
```

###查询帖子

GET     /forum/topic/<:tid>/      #tid:topic_id

request

```json
{
     "topic_id":"11"

}
```

###修改帖子

PUT    /forum/topic/<:tid>/   #tid:topic_id

request

```json
{
    "title":"Photoshop-CS6",
    "content":"<html>神一般的技术</html>",
    "course_id":"2"
}
```
response

```json
{
    "result":true,
    "detail":"or false 添加成功或失败",
    "modify_time":"2016-05-12 19:00:00",
    "publish_time":"2016-05-12 19:00:59"
}
```

###用户回帖子

POST     /forum/topic/<:tid>/reply/   #tid:topic_id

request

```json
{
     "content":"<html>确实不错</html>",
     "reply_self_id":"16"

}
```
response

```json
{
   "result":true,
    "detail":"or false 添加成功或失败"
}
```

###查询课程回帖

GET 　　/forum/topic/<:tid>/reply/    #tid:topic_id

request

```json
{
     "topic_id":"11"
}
```

###修改回复的帖子

PUT   /forum/topic/<:tid>/reply/<:pk>/    #tid:topic_id    pk:reply_id

request

```json
{
     "content":"<html>确实不错</html>",
     "reply_self_id":"12"

}
```
response
```json
{
   "result":true,
    "detail":"or false 添加成功或失败"
}
```
