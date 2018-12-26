# GithubTrendingApi


## 获取热门项目
请求地址 http://132.232.132.144:8009/api

请求结果:
<pre>
{
  "success": true,
  "count": 25,
  "msg": [
    {
      # 仓库名称
      "repo": "Librefox",
      # 项目语言
      "language": "JavaScript",
      # 项目拥有着
      "user": "intika",
      # 项目简介
      "about": "Librefox: Firefox with privacy enhancements",
      # 项目地址
      "link": "https://github.com/intika/Librefox",
      # 项目star数
      "stars": "495",
      # 项目fork数
      "forks": "14",
      # 新增star数
      "new_stars": "117 stars today",
      # 项目维护者头像地址
      "avatars": [
        "https://avatars2.githubusercontent.com/u/6892180?s=40&v=4",
        "https://avatars0.githubusercontent.com/u/152493?s=40&v=4",
        "https://avatars3.githubusercontent.com/u/2353785?s=40&v=4",
        "https://avatars3.githubusercontent.com/u/38463143?s=40&v=4"
      ]
    },
    ...
</pre>


## 获取热门开发者
请求地址 http://132.232.132.144:8009/api/developers

请求结果
<pre>
{
success: true,
count: 25,
msg: [
  {
    # 开发者用户名
    username: "thunlp (THUNLP)",
    # 开发者头像
    avatar: "https://avatars1.githubusercontent.com/u/18389035?s=96&v=4",
    # 开发者主页
    userlink: "https://github.com/thunlp",
    # 开发者热门项目
    repo: "NRLPapers",
    # 热门项目简介
    repo_about: "Must-read papers on network representation learning (NRL) / network embedding (NE)"
  },
</pre>


## 获取某种语言或开发者在某段时间内的trending
请求路径：

  http://132.232.132.144:8009/api?lang=python&since=daily

  http://132.232.132.144:8009/api/developers?lang=python&since=daily


- 请求参数
  - lang   语言

  - since   日期  
      daily  每天 &nbsp;&nbsp;&nbsp; weekly  每周&nbsp;&nbsp;&nbsp;monthly  每月
      

## 获取GitHub上的所有trending 语言。

请求地址 http://132.232.132.144:8009/api/languages

返回结果

<pre>
{
  "success": true,
  "count": 490,
  "msg": [
    "Zimpl",
    "Zephir",
    "YASnippet",
    "YARA",
    "YANG",
    "YAML",
    "Yacc",
    "Xtend",
    "XSLT",
    "XS",
    ...
</pre>


##  请求出错
当请求的lang或since不存在时，请求出错。错误结果为：
<pre>
{
  "success": false,
  "count": 0,
  "msg": "请求错误"
}
</pre>


# 安装本项目
1. pip install -r requirements.txt

2. 修改config.py 文件

3. 运行models.py 生成数据表(数据库格式需要为utf8mb4)

3. 运行run.py