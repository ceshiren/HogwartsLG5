import argparse
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--str', type=str, default = None)
parser.add_argument('--int', type=int, default=32)
parser.add_argument('--list', type=list, default=[])

args = parser.parse_args()
Gpus=list(args.str.strip("]").strip("[").split(';'))
print(Gpus)
print(args.str, type(args.str))
print(args.int, type(args.int))
print(args.list, type(args.list))
'''
parser.add_argument 方法的type参数理论上可以是任何合法的类型， 但有些参数传入格式比较麻烦，例如list，
所以一般使用bool, int, str, float这些基本类型就行了，更复杂的需求可以通过str传入，然后手动解析。
bool类型的解析比较特殊，传入任何值都会被解析成True，传入空值时才为False.
通过这个方法还能指定命令的帮助信息。具体请看API文档：https://docs.python.org/2/library/argparse.html

python test_get_argument.py --str=[0;1;2] --list="1"2"

['0', '1', '2']
[0;1;2] <class 'str'>
32 <class 'int'>
['1', '2'] <class 'list'>

'''
