# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "DesksideIdeas/Blog@gh-pages"
}

# 站点设置
site_name = "桌沿奇思"
site_logo = "${site_prefix}static/newlogo.png"
site_build_date = "2020-07-01T09:00+08:00"
author = "谢卓彦"
email = "xiezhuoyan1999@hotmail.com"
author_homepage = "https://desksideideas.github.io/Blog/"
description = "欢迎来到我的个人作品集。"
key_words = ['谢卓彦', '个人作品集', '桌沿奇思', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "知乎",
        "url": "https://www.zhihu.com/people/yan-shen-diao-yan-37",
        "brief": "了解我的更多回答"
    }
]
nav = [
    {
        "name": "进入首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "文章汇总",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "了解桌沿",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [

    {
        "name": "Weibo",
        "url": "https://weibo.com/7413289427/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
