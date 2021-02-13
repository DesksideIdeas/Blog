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
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "DesksideIdeas/Blog@gh-pages"
}

# 站点设置
site_name = "桌沿奇思"
site_logo = "${site_prefix}static/newlogo.png"
site_build_date = "2020-02-01T09:00+08:00"
author = "All rights reserved by XieZhuoYan."
email = "xiezhuoyan1999@hotmail.com"
author_homepage = "https://desksideideas.github.io/Blog/"
description = "欢迎来到谢卓彦的个人作品集。"
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
        "brief": "一位在我的理想道路上率先远航的先行者"
    },
    {
        "name": "Bullet Journal",
        "url": "https://bulletjournal.com/pages/learn",
        "brief": "一种值得学习、能让你静下心来的笔记法"
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
        "name": "我看的书",
        "url": "https://www.notion.so/deskside/78a19a0830674fe88b92b519f12efcc0?v=410e925d970048bd9700030cc81baeac",
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
