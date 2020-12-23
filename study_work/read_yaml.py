import yaml
def read_yaml(file='../config/work.yaml'):
    with open(file,'r') as fs :
        rs = yaml.load(fs,Loader=yaml.FullLoader)
        return rs


if __name__ == '__main__':
    res = read_yaml()
    print(type(res),res)
