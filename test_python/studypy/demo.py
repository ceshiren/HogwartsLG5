import requests

print('张琴的作业by-2020-12-24')
listDemo = [1,2,3]

print(type(listDemo))

demo = requests.get("http://www.baidu.com")
demo.encoding = 'utf-8'
print(demo.status_code)
print(demo.text)

