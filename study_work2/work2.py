class Demo():
    def add(self,a,b):
        rs = a+b
        if isinstance(rs,float):
            rs = round(rs,2)
        return rs

    def sub(self,a,b):
        rs = a-b
        if isinstance(rs,float):
            rs = round(rs,2)
        return rs

    def mul(self,a,b):
        rs = a*b
        if isinstance(rs,float):
            rs = round(rs,2)
        return a*b

    def divi(self,a,b):
        rs = a/b
        if isinstance(rs,float):
            rs = round(rs,2)
        return a/b

if __name__ == '__main__':
    demo = Demo()