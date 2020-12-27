import logging
from logging import handlers
import os
"""
解决乱码问题两种方式：
1、修改底层代码logging的init文件FileHandler(StreamHandler)，encoding默认给utf-8格式
2、通过输出流来读取文件，filename= 替换stream=file来打开文件，弊端，文件需一直打开，操作的时候
# file = open('../log/runlog.log',encoding="utf-8", mode="a")#修改输出流，防止中文乱码
"""
logging.basicConfig(filename= '../log/runlog.log',level=logging.INFO,
                    format="%(asctime)s ""%(filename)s [line:%(lineno)d] ""%(levelname)s>""%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                    ,filemode='a'
                    )
logger = logging.getLogger()
logger.setLevel(logging.INFO)

"""
1、更高级的日志切割封装，目前为了展示效果按S切割日志
2、按每S切割，每次最新日志输出到runlog.log里面，就的日志进行时间切割
"""
def _logging(**kwargs):
  level = kwargs.pop('level', None)
  filename = kwargs.pop('filename', None)
  datefmt = kwargs.pop('datefmt', None)
  format = kwargs.pop('format', None)
  if level is None:
    level = logging.DEBUG
  if filename is None:
    filename = '../log/runlog.log'
  if datefmt is None:
    datefmt = '%Y-%m-%d %H:%M:%S'
  if format is None:
    format = '%(asctime)s [%(filename)s] [%(lineno)d] %(levelname)s %(message)s'
  log = logging.getLogger(filename)
  format_str = logging.Formatter(format, datefmt)
  def split_namer(filename):
    return filename.split('runlog.log.')[1]
  # backupCount 保存日志的数量，过期自动删除
  # when 按什么日期格式切分(这里方便测试使用的秒)
  if not os.path.exists('../log'):#判断目录是否存在
    os.makedirs('../log')
  th_debug = handlers.TimedRotatingFileHandler(filename=filename, when='S', backupCount=3,
                                               encoding='utf-8')
  th_debug.namer = split_namer
  th_debug.suffix = '../log/'+"%Y-%m-%d_%H-%M-%S.log"
  th_debug.setFormatter(format_str)
  th_debug.setLevel(logging.DEBUG)
  log.addHandler(th_debug)
  log.setLevel(level)
  #判断目录是否存在
  return log
