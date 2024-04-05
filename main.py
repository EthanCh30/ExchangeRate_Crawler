from datetime import datetime
import re
import requests

url = 'http://www.boc.cn/sourcedb/whpj/index.html'  # 网址
html = requests.get(url).content.decode('utf8')  # 获取网页源码

a = html.index('<td>澳大利亚元</td>')  # 取得“澳大利亚元”当前位置
s = html[a:a + 300]  # 截取澳大利亚元汇率那部分内容（从a到a+300位置）
result = re.findall('<td>(.*?)</td>', s)  # 正则获取
rate = result[3] if len(result) > 3 else None #设置：银行现汇卖出价
today_date = datetime.now().strftime("%Y-%m-%d") #设置：今日时间

print(today_date, "中行现汇卖出价:", rate)

