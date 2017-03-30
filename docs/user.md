### 用户注册

POST    /user/signup/       # 初始化用户信息 profile

request

```json
{
    "username":"zhan", // length: 6-30; union
    "password":"123456",  // length: 6-30
    "email":"example@qq.com"  // format: email, union
}
```

response

```json
{
    "result":true,
    "detail":"用户名已经被注/邮箱已经被注册"
}
```

### 邮箱激活

GET    /user/active/?username=zhan&userencrpy=sdhfosdhlkhfiodsfsdasd

response

```json
{
    "result":true,
    "detail":"激活成功"
}

### 修改密码

PUT    /user/password/update/

request

```json
{
    "origin_password":"1234546",
    "new_password":"123qwe"
}
```
response

```json
{
    "return":false,
    "detail":"修改成功"
}
```
```json
{
    "result":false,
    "detail":"原始密码错误,修改失败"
}
```

### 找回密码

POST    /user/password/find

request

```json
{
    "email":"example@qq.com"
}
```

response

```json
{
    "return": false,
    "detail":"邮箱不存在"
}
```

PUT    /user/password/set

request

```json
{
    "userencrpy": "xxxxxxxxxxxxxxxx",
    "password":"123456"
}
```

response
```json
{
    "return":true,
    "detail":"重设密码成功"
}
```

### 用户登陆

POST    /user/signin/

login info with http request:  Authorization: JWT <response.token>

request

```json
{
    "username": "username  | email@xx.com",
    "password": "edx406406"
}
```

response

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjExMTExMSIsIm9yaWdfaWF0IjoxNDYyOTQxODM5LCJ1c2VyX2lkIjoyLCJlbWFpbCI6IjExMTExMUB3ZWl3ZWkuY29tIiwiZXhwIjoxNDYzMjAxMDM5fQ.WvowBTbhyezkjfl9Bkc-fk6X71VBQV5pY03bb7NmAwY"
    "detail": "login successful."
}
```

### 获取用户信息

GET /user/profile/

response

```json
{
    "real_name":"刘萌",
    "photo":"liu.jpg",
    "sex":"true",
    "birthday":"1986-12-03",
    "location":"湖北省-武汉市-洪山区",
    "interest":"计算机,音乐，电影",
    "introduce":"好好学习，天天向上",
    "education":[{"id":12,"organization":"中南大学", "start_date":"2002-09-01","end_date":"2006-06-01","major":"computer","degree":"bachelor"},
                  {"id": 13, "organization":"中南大学","start_date":"2002-09-01","end_date":"2006-06-01","major":"computer","degree":"bachelor"}
                ]

}
```

### 编辑用户信息

PUT   /user/profile/update/

request

```json
{
    "real_name":"刘萌",
    "photo":"liu.jpg",
    "sex":"true",
    "birthday":"1986-12-03",
    "location":"湖北省-武汉市-洪山区",
    "interest":"计算机,音乐，电影",
    "introduce":"好好学习，天天向上",
    "education":[12, 13]
}
```

response

```json
{
    "real_name":"刘萌",
    "photo":"liu.jpg",
    "sex":"true",
    "birthday":"1986-12-03",
    "location":"湖北省-武汉市-洪山区",
    "interest":"计算机,音乐，电影",
    "introduce":"好好学习，天天向上",
    "education":[
      {"id":12,"organization":"中南大学", "start_date":"2002-09-01","end_date":"2006-06-01","major":"computer","degree":"bachelor"},
      {"id": 13, "organization":"中南大学","start_date":"2002-09-01","end_date":"2006-06-01","major":"computer","degree":"bachelor"}
    ]
}
```


### 新建/编辑 学校信息

POST/PUT   /user/org/

request

```json
{
    "id": 13,  // PUT 时必须
    "organization":"中南大学",
    "start_date":"2002-09-01",
    "end_date":"2006-06-01",
    "major":"computer",
    "degree":"bachelor"

}
```
