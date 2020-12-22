import yaml
def read_yaml(key,file='../config/work.yaml'):
    with open(file,'r') as fs :
        rs = yaml.load(fs,Loader=yaml.FullLoader)
        return rs[key]


if __name__ == '__main__':
    res = read_yaml('sub_ids')
    res2 = read_yaml('sub')
    print(type(res),res)
    print(type(res2), res2)
