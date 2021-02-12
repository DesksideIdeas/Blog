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
        "name": "James Clear",
        "url": "https://jamesclear.com",
        "brief": "一位在「习惯」方面帮助了我很多的作者"
    },
    {
        "name": "David Perell",
        "url": "https://perell.com",
        "brief": "一位在我的理想道路上走得很远的先行者"
    },
    {
        "name": "Bullet Journal",
        "url": "https://bulletjournal.com",
        "brief": "一种值得能让你静下心来的笔记法"
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
