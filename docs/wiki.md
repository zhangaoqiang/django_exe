# 根据课程id获取所有wiki

	GET	/wiki/course/<:cid>/article/ #cid:course_id

request

```json
{
"course_id":"课程id"
}
```

response

```json
[
{
"id":"uuid",
"title":"标题",
"richText":"<html>...</html>",
"outline":"徐潇创建",
"create_time":"2015-12-2 12:00",
"modify_time":"2016-4-22 11:30",
"is_verify":True,
"user":{"id":"uuid",
"username":"用户名",},
"course":{"id":"uuid",
"name":"课程名称",},
},
{"id":"uuid",
"title":"标题",
"richText":"<html>...</html>",
"outline":"杨恒创建",
"create_time":"2015-12-2 12:00",
"modify_time":"2016-4-22 11:30",
"is_verify":True,
"user":{"id":"uuid",
"username":"用户名",},
"course":{"id":"uuid",
"name":"课程名称",},
},
]
```
#根据文章wikiID获取wiki
	GET	/wiki/course/article/<:aid>/ #aid:article_id
request

```json
{
"wikiId":"维基ID"
}
```

response

```json
{
"id":"uuid",
"title":"标题",
"richText":"<html>...</html>",
"outline":"徐潇创建",
"create_time":"2015-12-2 12:00",
"modify_time":"2016-4-22 11:30",
"is_verify":True,
"user":{"id":"uuid",
"username":"用户名",},
"course":{"id":"uuid",
"name":"课程名称",},
}
```
# 教师新建wiki(只能是教师做的事情)
    POST /wiki/add
    
request

```json
{
"title":"标题",
"richText":"<html>...</html>",
"outline":"徐潇创建",
"courseId":"课程id",
}
```
response

```json
"update":"success",
```

#保存提交wiki的修改
	PUT /wiki/modify_article/<:wid> #wid:wiki_id

request

```json
{
"id":"uuid",
"title":"标题",
"richText":"<html>...</html>",
"outline":"徐潇创建",
"wikiID":"课程id"
}
```

response

```json
{
"update":"success",
}
```
# 通过wikiId获取该wiki下的待审核的wiki

    GET /wiki/pre_article/<:wid>

request

```json
{
"wikiId":"uuid",
}
```
response

```json
{
"id":"uuid",
"title":"标题",
"richText":"<html>...</html>",
"outline":"徐潇创建",
"create_time":"2015-12-2 12:00",
"modify_time":"2016-4-22 11:30",
"is_verify":True,
"user":{"id":"uuid",
"username":"用户名",},
}
```
# 教师审核提交的wiki
    PUT /wiki/pass/<:wid>#wid:wiki_id
    
request

```json
{
"wikiId":"uuid",
}
```
response

```json
{
"update":"success",
}
```
# 教师获取wiki版本信息列表
    GET /wiki/versions/<:wid>#wid:wiki_id

request

```json
{
"wikiId":"uuid",
}
```

response

```json
{
"id":"uuid",
"title":"标题",
"richText":"<html>...</html>",
"outline":"徐潇创建",
"version_num":"v2015-12-2",
"create_time":"2015-12-2 12:00",
"modify_time":"2016-4-22 11:30",
"user":{"id":"uuid",
"username":"用户名",},
},
{"id":"uuid",
"title":"标题",
"richText":"<html>...</html>",
"outline":"杨恒创建",
"version_num":"v2015-12-2",
"create_time":"2015-12-2 12:00",
"modify_time":"2016-4-22 11:30",
"user":{"id":"uuid",
"username":"用户名",},
},
]
```
# 教师合并wiki版本
    POST    /wiki/<:wid>/merge/
    
request

```json
{
"wikiId":"uuid",
}
```
response

```json
{
"update":"success",
}
```









