import requests

url = "https://weathernew.pae.baidu.com/weathernew/pc?query=%E6%B1%9F%E8%8B%8F%E8%8B%8F%E5%B7%9E%E5%A4%A9%E6%B0%94&srcid=4982&forecast=long_day_forecast"  # 爬虫打开的浏览器上的网页
resp = requests.get(url)  # 打开浏览器并打开网址
resp.encoding = 'utf-8'
print(resp.text)  # 响应对象
