# coding:utf-8

import requests
from lxml import html
import re
import json
import time

url = 'http://www.lagou.com/jobs/positionAjax.json'
headers = {
    "X-Requested-With": 'XMLHttpRequest',
    "User-Agent": 'xxxx',
    "Origin": 'https://www.lagou.com',
    "Cookie": 'xxxxxx',
    "Connection": 'keep-alive'
}

city = [u'全国', u'北京', u'上海', u'广州', u'深圳', u'杭州']
city2 = [u'全国']
job = ['Java', 'Python', 'PHP', 'C++/C', '.NET', 'C#', 'Node.js', 'Android', 'iOS', u'前端开发']
job_2 = [u'技术', u'设计', u'产品', u'运营', u'市场', u'销售', u'金融', u'职能']
for j_kd in job:
    print u'%s 各城市职位情况:' % j_kd
    for j_city in city2:
        data = {'first': True, 'pn': 1, 'kd': j_kd, 'city': j_city}
        session = requests.Session()
        content = session.post(url, headers=headers, data=data).content
        result = json.loads(content)
        count = result['content']['positionResult']['totalCount']
        print u'%s(%s) ' % (j_city, count)
        time.sleep(1)
    print '=================================='
