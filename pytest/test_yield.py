#yield生成器
def t_yield():
    for i in range(5):
        print('开始操作')
        yield i
        print('结束操作')

t = t_yield()
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
for i in t:
    print(i)